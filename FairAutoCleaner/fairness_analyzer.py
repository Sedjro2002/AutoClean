"""Fairness analysis module for FairAutoCleaner using AI Fairness 360."""
from typing import Dict, List, Tuple, Any, Optional
import pandas as pd
from datetime import datetime
from loguru import logger
from dataclasses import dataclass
from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric, SampleDistortionMetric
from aif360.algorithms.preprocessing import Reweighing
import numpy as np
from .config import Config
from .code_analyzer import CodeBiasAnalyzer, CodeBiasResult
from .ai_code_analyzer import AICodeAnalyzer

@dataclass
class FairnessMetrics:
    """Container for fairness metrics."""
    disparate_impact: float
    statistical_parity_difference: float
    group_metrics: Dict[str, Any]

class FairnessAnalyzer:
    """Analyzes and mitigates bias in datasets using AI Fairness 360."""
    
    def __init__(
        self,
        data: pd.DataFrame,
        target: str,
        sensitive_features: Optional[List[str]] = None,
        features: Optional[List[str]] = None,
        favorable_label: Any = 1,
        unfavorable_label: Any = 0,
        audit_logger: Optional[Any] = None,
        config: Optional[Config] = None
    ):
        """Initialize the FairnessAnalyzer.
        
        Args:
            data: Input DataFrame
            target: Name of the target column
            sensitive_features: List of sensitive feature names. If None, will use AI to detect.
            features: List of feature names to use. If None, uses all columns.
            favorable_label: The favorable label in binary classification
            unfavorable_label: The unfavorable label in binary classification
        """
        self.data = data
        self.target = target
        self.features = features or [col for col in data.columns if col != target]
        self.favorable_label = favorable_label
        self.unfavorable_label = unfavorable_label
        self.audit_logger = audit_logger
        self.config = config
        
        # If sensitive features not provided, use AI to detect them
        if not sensitive_features:
            self.sensitive_features = self._detect_sensitive_features()
        else:
            self.sensitive_features = sensitive_features
        try:
            import asyncio
            # Create new event loop for Windows compatibility
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self.code_biases = loop.run_until_complete(self.analyze_code_biases())
            loop.close()
        except Exception as e:
            logger.error(f"Error in code bias analysis: {str(e)}")
            self.code_biases = []
            
    def _detect_sensitive_features(self) -> List[str]:
        """Use AI to detect potentially sensitive features."""

        logger.info("Detecting potentially sensitive features...")
        self.audit_logger.start_operation(
            name="Sensitive Feature Detection",
            description="Use AI to detect potentially sensitive features",
            parameters={},
            df=self.data
        )
        start_time = datetime.now()     
        results = []
        try:
            from .ai_agent.main import risky_feature_detector
            context = self.config.dataset_config['dataset']
            context.pop('preprocessing')
            detected_features = []
            for column in self.features:
                agent_input = {
                    'name': column,
                    'content': self.data[column].sample(5).to_list(),
                    # 'context': {'dataset_summary': 'Analyzing for sensitive attributes'}
                    'context': context
                }
                
                result = risky_feature_detector.run_sync(str(agent_input))
                result_dict = result.data.model_dump() 
                result_dict['column'] = column
                results.append(result_dict)
                logger.info(result_dict)
                if result.data.is_sensitive:  # Threshold for sensitivity
                # if result.data.sensibility_level > 5:  # Threshold for sensitivity
                    detected_features.append(column)
                    logger.info(f"Detected {column} as a sensitive feature")
                    

            self.audit_logger.complete_operation(
                name="Sensitive Feature Detection",
                start_time= start_time,
                description="Use AI to detect potentially sensitive features",
                parameters={},
                changes_made={ "sensitive_features": detected_features, "results": results },
                input_df= self.data,
                output_df= self.data
            )
            return detected_features
        except Exception as e:
            logger.error(f"Error in sensitive feature detection: {str(e)}")
            self.audit_logger.complete_operation(
                name="Sensitive Feature Detection",
                start_time= start_time,
                description="Use AI to detect potentially sensitive features",
                parameters={},
                changes_made={ "sensitive_features": [], "results": [] },
                error=str(e),
                input_df= self.data,
                output_df= self.data
            )
            return []
            
    def _prepare_aif360_dataset(self, sensitive_feature: str) -> BinaryLabelDataset:
        """Prepare dataset in aif360 format for a single sensitive feature."""
        try:
            # Convert target to binary if needed
            if self.data[self.target].nunique() > 2:
                logger.warning(f"Target {self.target} has >2 classes. Converting to binary.")
                median = self.data[self.target].median()
                binary_target = (self.data[self.target] > median).astype(int)
            else:
                binary_target = self.data[self.target]
            
            # Convert sensitive feature to binary if needed
            if self.data[sensitive_feature].nunique() > 2:
                logger.warning(f"Feature {sensitive_feature} has >2 classes. Using median split.")
                median = self.data[sensitive_feature].median()
                binary_protected = (self.data[sensitive_feature] > median).astype(int)
            else:
                # Ensure values are 0 and 1
                unique_vals = sorted(self.data[sensitive_feature].unique())
                value_map = {unique_vals[0]: 0, unique_vals[1]: 1}
                binary_protected = self.data[sensitive_feature].map(value_map)
            
            # Prepare data for aif360
            df = pd.DataFrame({
                'label': binary_target,
                sensitive_feature: binary_protected
            })
            
            privileged_groups = [{sensitive_feature: 1}]
            unprivileged_groups = [{sensitive_feature: 0}]
            
            return BinaryLabelDataset(
                df=df,
                label_names=['label'],
                protected_attribute_names=[sensitive_feature],
                privileged_protected_attributes=[[1]],
                unprivileged_protected_attributes=[[0]],
                favorable_label=self.favorable_label,
                unfavorable_label=self.unfavorable_label
            )
        except Exception as e:
            logger.error(f"Error preparing aif360 dataset: {str(e)}")
            raise
            
    def analyze_and_mitigate(self):
        """Analyze and mitigate bias for each sensitive feature."""
        results = {}

        self.audit_logger.start_operation(
            name="Fairness Analysis",
            description="Analyze and mitigate bias for each sensitive feature",
            parameters={},
            df=self.data
        )
        df_copy = self.data.copy()
        start_time = datetime.now() 
        dataset_transformed = None
        for feature in self.sensitive_features:
            logger.info(f"Analyzing and mitigating bias for feature {feature}")
            self.audit_logger.start_operation(
                name=f"Fairness Analysis {feature}",
                description=f"Analyze and mitigate bias for feature {feature}",
                parameters={},
                df=self.data
            )
            start_time_2 = datetime.now() 
            try:
                # Create aif360 dataset
                dataset = self._prepare_aif360_dataset(feature)
                
                # Calculate original metrics
                metrics = BinaryLabelDatasetMetric(
                    dataset,
                    unprivileged_groups=[{feature: 0}],
                    privileged_groups=[{feature: 1}]
                )
                
                original_metrics = FairnessMetrics(
                    disparate_impact=metrics.disparate_impact(),
                    statistical_parity_difference=metrics.statistical_parity_difference(),
                    group_metrics=self._calculate_group_metrics(dataset, feature)
                )
                
                # Apply mitigation
                mitigator = Reweighing(
                    unprivileged_groups=[{feature: 0}],
                    privileged_groups=[{feature: 1}]
                )
                dataset_transformed = mitigator.fit_transform(dataset)
                
                # Calculate metrics after mitigation
                metrics_transformed = BinaryLabelDatasetMetric(
                    dataset_transformed,
                    unprivileged_groups=[{feature: 0}],
                    privileged_groups=[{feature: 1}]
                )
                
                mitigated_metrics = FairnessMetrics(
                    disparate_impact=metrics_transformed.disparate_impact(),
                    statistical_parity_difference=metrics_transformed.statistical_parity_difference(),
                    group_metrics=self._calculate_group_metrics(dataset_transformed, feature)
                )
                
                results[feature] = {
                    'original': original_metrics,
                    'mitigated': mitigated_metrics
                }
                
                # Log results
                self._log_feature_results(feature, results[feature])

                self.audit_logger.complete_operation(
                    name=f"Fairness Analysis {feature}",
                    start_time= start_time_2,
                    description=f"Analyze and mitigate bias for feature {feature}",
                    parameters={},
                    changes_made={ "results": results[feature] },
                    input_df= df_copy,
                    output_df= self.data,
                )
                
            except ValueError as ve:
                logger.error(f"Value error analyzing feature {feature}: {str(ve)}")
                continue
            except KeyError as ke:
                logger.error(f"Key error analyzing feature {feature}: {str(ke)}")
                continue
            except Exception as e:
                logger.error(f"Unexpected error analyzing feature {feature}: {str(e)}")
                raise
                
        self.audit_logger.complete_operation(
            name="Fairness Analysis",
            start_time= start_time,
            description="Analyze and mitigate bias for each sensitive feature",
            parameters={},
            changes_made={ "results": results },
            input_df= df_copy,
            output_df= self.data,
        )
        return results, dataset_transformed
        
    def _calculate_group_metrics(self, dataset: BinaryLabelDataset, feature: str) -> Dict[str, float]:
        """Calculate metrics for each group in a sensitive feature."""
        metrics = {}
        for value in [0, 1]:  # Only binary values after preprocessing
            mask = dataset.protected_attributes[:, 0] == value
            positive_rate = np.mean(dataset.labels[mask] == self.favorable_label)
            metrics[f'group_{value}_positive_rate'] = float(positive_rate)
        return metrics
        
    def _log_feature_results(self, feature: str, result: Dict[str, FairnessMetrics]) -> None:
        """Log fairness analysis results for a feature."""
        logger.info(f"\nFairness Analysis Results for {feature}:")
        logger.info(f"Original Disparate Impact: {result['original'].disparate_impact:.4f}")
        logger.info(f"Original Statistical Parity Difference: {result['original'].statistical_parity_difference:.4f}")
        logger.info(f"Mitigated Disparate Impact: {result['mitigated'].disparate_impact:.4f}")
        logger.info(f"Mitigated Statistical Parity Difference: {result['mitigated'].statistical_parity_difference:.4f}")
        
        for group, rate in result['original'].group_metrics.items():
            logger.info(f"Original {group}: {rate:.4f}")
        for group, rate in result['mitigated'].group_metrics.items():
            logger.info(f"Mitigated {group}: {rate:.4f}")

    async def analyze_code_biases(self) -> List[Any]:
        """Analyze code paths for potential ethical biases using either syntax or AI analysis.
        
        Returns:
            List of analysis results (either CodeBiasResult or AI analysis results)
        """
        if not self.config or not self.config.code_analysis_paths:
            logger.info("No code paths specified for analysis")
            return []

        analysis_type = self.config.code_analysis_type.lower()
        if analysis_type not in ['syntax', 'ai']:
            logger.warning(f"Invalid analysis type '{analysis_type}'. Defaulting to 'syntax'")
            analysis_type = 'syntax'

        logger.info(f"Starting code bias analysis using {analysis_type} analysis...")
        self.audit_logger.start_operation(
            name="Code Bias Analysis",
            description=f"Analyzing code paths for potential ethical biases using {analysis_type} analysis",
            parameters={
                "paths": self.config.code_analysis_paths,
                "analysis_type": analysis_type
            },
            df=self.data
        )
        start_time = datetime.now()

        results = []
        if analysis_type == 'syntax':
            analyzer = CodeBiasAnalyzer()
            for path in self.config.code_analysis_paths:
                path_results = analyzer.analyze_path(path)
                results.extend(path_results)
                
                for result in path_results:
                    if result.potential_biases:
                        logger.warning(
                            f"Found potential biases in {result.file_path}:\n"
                            f"Risk Level: {result.risk_level}\n" if result.risk_level else ""
                            f"Recommendations: {', '.join(result.recommendations)}\n" if result.recommendations else ""
                        )
        else:  # AI analysis
            analyzer = AICodeAnalyzer()
            for path in self.config.code_analysis_paths:
                path_results = await analyzer.analyze_path(path)
                results.extend(path_results)
                
                for result in path_results:
                    # result = result.data.model_dump()
                    if result['analysis']['is_problematic']:
                        logger.warning(
                            f"Found potential biases in {result['file']}:\n"
                            f"Sensitivity Level: {result['analysis']['sensitivity_level']}/10\n"
                            # f"Recommendations: {', '.join(result['analysis']['recommendations'])}"
                        )

        self.audit_logger.complete_operation(
            name="Code Bias Analysis",
            start_time=start_time,
            description=f"Completed {analysis_type} code bias analysis",
            parameters={
                "paths": self.config.code_analysis_paths,
                "analysis_type": analysis_type
            },
            changes_made={"results": results},
            input_df=self.data,
            output_df=self.data
        )

        return results
