"""Fairness analysis module for FairAutoCleaner using AI Fairness 360."""
from typing import Dict, List, Tuple, Any, Optional
import pandas as pd
import numpy as np
from datetime import datetime
from loguru import logger
from dataclasses import dataclass
from aif360.datasets import BinaryLabelDataset, StandardDataset, StructuredDataset
from aif360.metrics import BinaryLabelDatasetMetric, SampleDistortionMetric, DatasetMetric
from aif360.algorithms.preprocessing import Reweighing, DisparateImpactRemover
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from .config import Config
from .code_analyzer import CodeBiasAnalyzer, CodeBiasResult
from .ai_code_analyzer import AICodeAnalyzer

@dataclass
class FairnessMetrics:
    """Container for fairness metrics."""
    disparate_impact: float
    statistical_parity_difference: float
    equal_opportunity_difference: Optional[float] = None
    average_odds_difference: Optional[float] = None
    group_metrics: Dict[str, Any] = None
    is_biased: bool = False
    bias_reasons: List[str] = None

class FairnessAnalyzer:
    """Analyzes and mitigates bias in datasets using AI Fairness 360."""
    
    def __init__(
        self,
        data: pd.DataFrame,
        target: str,
        sensitive_features: Optional[List[str]] = None,
        features: Optional[List[str]] = None,
        favorable_values = None,
        unfavorable_values = None,
        privileged_values: Optional[Dict[str, Any]] = None,
        audit_logger: Optional[Any] = None,
        config: Optional[Config] = None
    ):
        """Initialize the FairnessAnalyzer.
        
        Args:
            data: Input DataFrame
            target: Name of the target column
            sensitive_features: List of sensitive feature names. If None, will use AI to detect.
            features: List of feature names to use. If None, uses all columns.
            favorable_values: The favorable label in binary classification
            unfavorable_values: The unfavorable label in binary classification
            privileged_values: Dictionary mapping sensitive features to their privileged values
            audit_logger: Logger for audit trail
            config: Configuration object
        """
        self.data = data
        self.target = target
        self.features = features or [col for col in data.columns if col != target]
        if favorable_values is None:
            unique_vals = self.data[target].unique()
            # print("=== Configuration des valeurs favorables ===")
            # print(f"Valeurs uniques pour '{target}': {unique_vals}")
            if len(unique_vals) == 2:
                # Si binaire, suggérer la valeur la plus élevée comme favorable
                favorable_values = [max(unique_vals)]
                print(f"Pour '{target}', valeur favorable considérée: {favorable_values[0]}")
            else:
                # Pour les cas non binaires, nous devons définir explicitement
                print(f"Pour '{target}', par defaut, la valeur favorable est la dernière valeur: {unique_vals[-1]}")
                favorable_values = [unique_vals[-1]]  # Par défaut, dernière valeur
        self.favorable_values = favorable_values
        self.unfavorable_values = list(set(self.data[target].unique()) - set(favorable_values))
        self.audit_logger = audit_logger
        self.config = config
        self.privileged_values = privileged_values or {}
        
        # If sensitive features not provided, use AI to detect them
        if not sensitive_features:
            self.sensitive_features = self._detect_sensitive_features()
        else:
            self.sensitive_features = sensitive_features
            
        # Display information about key columns
        self._log_column_info()
        
        # Auto-detect privileged values if not provided
        self._detect_privileged_values()
            
        # Create privileged and unprivileged groups
        self.privileged_groups, self.unprivileged_groups = self._create_groups()
        
        # try:
        #     self.code_biases = self.analyze_code_biases()
        # except Exception as e:
        #     logger.error(f"Error in code bias analysis: {str(e)}")
        #     self.code_biases = []
            
    def _log_column_info(self):
        """Log information about key columns."""
        logger.info("=== Informations sur les colonnes clés ===")
        for attr in self.sensitive_features:
            logger.info(f"Attribut protégé '{attr}' - valeurs uniques: {self.data[attr].unique()}")
        logger.info(f"Colonne cible '{self.target}' - valeurs uniques: {self.data[self.target].unique()}")
            
    def _detect_privileged_values(self):
        """Auto-detect privileged values for sensitive features if not provided."""
        logger.info("=== Configuration des valeurs privilégiées ===")
        for attr in self.sensitive_features:
            if attr in self.privileged_values:
                continue
                
            feature_data = self.data[attr]
            unique_vals = feature_data.unique()
            
            # Vérifier si la feature est continue
            if len(unique_vals) > 2:
                # Utiliser la moyenne comme seuil pour les features continues
                threshold = np.mean(feature_data)
                self.privileged_values[attr] = {'threshold': threshold}
                logger.info(f"Feature continue '{attr}' - seuil automatique: {threshold:.2f}")
            elif len(unique_vals) == 2:
                # Cas binaire
                suggested = max(unique_vals)
                self.privileged_values[attr] = suggested
                logger.info(f"Feature binaire '{attr}' - valeur privilégiée: {suggested}")
            else:
                # Cas catégoriel avec plusieurs valeurs
                self.privileged_values[attr] = unique_vals[0]
                logger.warning(f"Feature catégorielle '{attr}' - valeur privilégiée par défaut: {unique_vals[0]} (à vérifier manuellement)")
            
    def _create_groups(self):
        """Create privileged and unprivileged groups from protected attributes."""
        privileged_groups = []
        unprivileged_groups = []
        
        for attr in self.sensitive_features:
            priv_spec = self.privileged_values[attr]
            
            # Gestion des features continues avec seuil
            if isinstance(priv_spec, dict) and 'threshold' in priv_spec:
                threshold = priv_spec['threshold']
                
                # Calculer la distribution des groupes
                n_privileged = np.sum(self.data[attr] >= threshold)
                n_total = len(self.data)
                percent_priv = (n_privileged / n_total) * 100
                
                privileged_groups.append({attr: (threshold, '>=')})
                unprivileged_groups.append({attr: (threshold, '<')})
                
                logger.info(f"Feature continue '{attr}' - seuil à {threshold:.2f}")
                logger.info(f"Privilégié (>= {threshold:.2f}): {n_privileged} entrées ({percent_priv:.1f}%)")
                logger.info(f"Non-privilégié (< {threshold:.2f}): {n_total - n_privileged} entrées ({100 - percent_priv:.1f}%)")
            
            # Gestion des valeurs discrètes
            else:
                priv_value = priv_spec
                unique_vals = self.data[attr].unique()
                
                if priv_value in [0, 1]:  # Cas binaire
                    unpriv_value = 1 - priv_value
                    n_privileged = np.sum(self.data[attr] == priv_value)
                else:  # Cas catégoriel
                    non_priv_values = [v for v in unique_vals if v != priv_value]
                    unpriv_value = non_priv_values[0] if non_priv_values else None
                    n_privileged = np.sum(self.data[attr] == priv_value)
                
                n_total = len(self.data)
                percent_priv = (n_privileged / n_total) * 100
                
                privileged_groups.append({attr: priv_value})
                if unpriv_value is not None:
                    unprivileged_groups.append({attr: unpriv_value})
                
                logger.info(f"Feature discrète '{attr}'")
                logger.info(f"Valeur privilégiée: {priv_value} ({n_privileged} entrées, {percent_priv:.1f}%)")
                if unpriv_value is not None:
                    logger.info(f"Valeur non-privilégiée: {unpriv_value} ({n_total - n_privileged} entrées, {100 - percent_priv:.1f}%)")
        
        return privileged_groups, unprivileged_groups
        
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
            context = self.config.get("dataset_config", {}).get("dataset", {})
            detected_features = []
            for column in self.features:
                agent_input = {
                    'name': column,
                    'content': self.data[column].sample(5).to_list(),
                    'context': context
                }
                
                result = risky_feature_detector.run_sync(str(agent_input))
                result_dict = result.data.model_dump() 
                result_dict['column'] = column
                result_dict['is_sensitive'] = False if result_dict['is_sensitive'] <= 5 else True
                result.data.is_sensitive = False if result.data.sensibility_level <= 5 else True
                results.append(result_dict)
                logger.info(f"Column: {column}: {result_dict}")
                if result.data.is_sensitive:
                    detected_features.append(column)
                    logger.info(f"Detected {column} as a sensitive feature")
                    
            self.audit_logger.complete_operation(
                name="Sensitive Feature Detection",
                start_time=start_time,
                description="Use AI to detect potentially sensitive features",
                parameters={},
                changes_made={"sensitive_features": detected_features, "results": results},
                input_df=self.data,
                output_df=self.data
            )
            return detected_features
        except Exception as e:
            logger.error(f"Error in sensitive feature detection: {str(e)}")
            self.audit_logger.complete_operation(
                name="Sensitive Feature Detection",
                start_time=start_time,
                description="Use AI to detect potentially sensitive features",
                parameters={},
                changes_made={"sensitive_features": [], "results": []},
                error=str(e),
                input_df=self.data,
                output_df=self.data
            )
            return []
            
    def _prepare_aif360_dataset(self, sensitive_feature: str) -> BinaryLabelDataset:
        """Prepare dataset in aif360 format for a single sensitive feature."""
        try:
            df = self.data.copy()
            priv_spec = self.privileged_values[sensitive_feature]
            
            # Convert continuous features to binary based on threshold
            if isinstance(priv_spec, dict) and 'threshold' in priv_spec:
                threshold = priv_spec['threshold']
                # Create temporary binary feature
                df[sensitive_feature] = np.where(df[sensitive_feature] >= threshold, 1, 0)
                logger.info(f"Converted continuous feature '{sensitive_feature}' to binary using threshold {threshold:.2f}")
            
            if len(df[self.target].unique()) != 2:
                logger.error(f"Target column '{self.target}' must have exactly 2 unique values for fairness analysis")
                raise ValueError(f"Target column '{self.target}' must have exactly 2 unique values for fairness analysis")
                
            # Determine if we need to use BinaryLabelDataset or StandardDataset
            if len(df[sensitive_feature].unique()) == 2:
                # Get privileged value (might be converted from threshold)
                priv_value = priv_spec if not isinstance(priv_spec, dict) else 1
                
                # Convert feature values to binary (1 for privileged, 0 otherwise)
                df[sensitive_feature] = np.where(
                    df[sensitive_feature] == priv_value, 1, 0
                )
                logger.info(f"Converted binary feature '{sensitive_feature}' to 1/0 based on privileged value {priv_value}")
                
                # Binary case: use BinaryLabelDataset
                aif_dataset = BinaryLabelDataset(
                    df=df,
                    label_names=[self.target],
                    protected_attribute_names=[sensitive_feature],
                    privileged_protected_attributes=[[1]],
                    unprivileged_protected_attributes=[[0]],
                    favorable_label=self.favorable_values[0],
                    unfavorable_label=self.unfavorable_values[0]
                )
                # aif_dataset = StructuredDataset(
                #     df=df,
                #     label_names=[self.target],
                #     protected_attribute_names=[sensitive_feature],
                #     privileged_protected_attributes=[[1]],
                #     unprivileged_protected_attributes=[[0]],
                #     # favorable_label=self.favorable_values[0],
                #     # unfavorable_label=self.unfavorable_values[0]
                # )
                
                # favorable_classes = [self.favorable_values]
                # aif_dataset = StandardDataset(
                #     df=df,
                #     label_name=self.target,
                #     favorable_classes=favorable_classes,
                #     protected_attribute_names=[sensitive_feature],
                #     privileged_classes=[[self.privileged_values[sensitive_feature]]]
                # )
            else:
                # Complex case: use StandardDataset
                favorable_classes = [self.favorable_values]
                aif_dataset = StandardDataset(
                    df=df,
                    label_name=self.target,
                    favorable_classes=favorable_classes[0],
                    protected_attribute_names=[sensitive_feature],
                    privileged_classes=[[self.privileged_values[sensitive_feature]]]
                )
            
            return aif_dataset
        except Exception as e:
            logger.error(f"Error preparing aif360 dataset: {str(e)}")
            raise
            
    def detect_bias(self, dataset, privileged_groups, unprivileged_groups) -> FairnessMetrics:
        """Detect bias in dataset and return a verdict on bias presence."""
        metrics_obj = BinaryLabelDatasetMetric(
            dataset, 
            unprivileged_groups=unprivileged_groups,
            privileged_groups=privileged_groups
        )
        # metrics_obj = DatasetMetric(
        #     dataset, 
        #     unprivileged_groups=unprivileged_groups,
        #     privileged_groups=privileged_groups
        # )
        
        # Calculate bias metrics
        logger.info("=== Métriques de biais ===")
        di = metrics_obj.disparate_impact()
        spd = metrics_obj.statistical_parity_difference()
        
        # # Additional metrics when possible
        # try:
        #     eod = metrics_obj.equal_opportunity_difference()
        #     aod = metrics_obj.average_odds_difference()
        #     logger.info(f"Equal Opportunity Difference: {eod:.4f}")
        #     logger.info(f"Average Odds Difference: {aod:.4f}")
        # except Exception as e:
        #     eod = None
        #     aod = None
        #     logger.info(f"Note: Equal Opportunity et Average Odds ne peuvent pas être calculés : {e}")
        
        logger.info(f"Disparate Impact: {di:.4f}")
        logger.info(f"Statistical Parity Difference: {spd:.4f}")
        
        # Determine if dataset is biased
        is_biased = False
        bias_reasons = []
        
        # Check Disparate Impact (80% rule)
        if di < 0.8 or di > 1.25:
            is_biased = True
            if di < 0.8:
                bias_reasons.append(f"Disparate Impact de {di:.4f} < 0.8 (sous-représentation du groupe non privilégié)")
            else:
                bias_reasons.append(f"Disparate Impact de {di:.4f} > 1.25 (sur-représentation du groupe non privilégié)")
        
        # Check Statistical Parity Difference
        if abs(spd) > 0.05:
            is_biased = True
            bias_reasons.append(f"Statistical Parity Difference de {abs(spd):.4f} > 0.05")
        
        # Check other metrics if available
        # if eod is not None and abs(eod) > 0.05:
        #     is_biased = True
        #     bias_reasons.append(f"Equal Opportunity Difference de {abs(eod):.4f} > 0.05")
        
        # if aod is not None and abs(aod) > 0.05:
        #     is_biased = True
        #     bias_reasons.append(f"Average Odds Difference de {abs(aod):.4f} > 0.05")
        
        # Create group metrics as in original code
        group_metrics = self._calculate_group_metrics(dataset, list(privileged_groups[0].keys())[0])
        
        # Return metrics in our dataclass format
        return FairnessMetrics(
            disparate_impact=di,
            statistical_parity_difference=spd,
            # equal_opportunity_difference=eod,
            # average_odds_difference=aod,
            group_metrics=group_metrics,
            is_biased=is_biased,
            bias_reasons=bias_reasons
        )
            
    def analyze_and_mitigate(self):
        """Analyze and mitigate bias for each sensitive feature."""
        results = {}
        best_datasets = {}

        self.audit_logger.start_operation(
            name="Fairness Analysis",
            description="Analyze and mitigate bias for each sensitive feature",
            parameters={},
            df=self.data
        )
        df_copy = self.data.copy()
        start_time = datetime.now() 
        
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
                # Create privileged and unprivileged groups for this feature
                privileged_groups = [{feature: self.privileged_values[feature]}]
                if self.privileged_values[feature] in [0, 1]:
                    unprivileged_groups = [{feature: 1 - self.privileged_values[feature]}]
                else:
                    unique_vals = self.data[feature].unique()
                    non_priv = [v for v in unique_vals if v != self.privileged_values[feature]][0]
                    unprivileged_groups = [{feature: non_priv}]
                
                # Create aif360 dataset
                dataset = self._prepare_aif360_dataset(feature)
                
                # Calculate original metrics
                original_metrics = self.detect_bias(dataset, privileged_groups, unprivileged_groups)
                
                # Display verdict on bias presence
                logger.info("=== VERDICT SUR LA PRÉSENCE DE BIAIS ===")
                if original_metrics.is_biased:
                    logger.info(f"VERDICT: Le dataset est BIAISÉ pour la feature {feature} pour les raisons suivantes:")
                    for reason in original_metrics.bias_reasons:
                        logger.info(f"- {reason}")
                    
                    # Apply Reweighing mitigation
                    logger.info("=== Mitigation avec Reweighing ===")
                    reweighing = Reweighing(
                        unprivileged_groups=unprivileged_groups,
                        privileged_groups=privileged_groups
                    )
                    dataset_reweighed = reweighing.fit_transform(dataset)
                    
                    # Calculate metrics after Reweighing
                    reweighed_metrics = self.detect_bias(dataset_reweighed, privileged_groups, unprivileged_groups)
                    logger.info("Après mitigation Reweighing:")
                    logger.info(f"Disparate Impact: {reweighed_metrics.disparate_impact:.4f}")
                    logger.info(f"Statistical Parity Difference: {reweighed_metrics.statistical_parity_difference:.4f}")
                    
                    # If still biased, try Disparate Impact Remover
                    if reweighed_metrics.is_biased:
                        logger.info("Essai d'une méthode alternative...")
                        # Apply Disparate Impact Remover
                        logger.info("=== Mitigation avec Disparate Impact Remover ===")
                        dir_mitigator = DisparateImpactRemover(repair_level=0.8)
                        dataset_dir = dir_mitigator.fit_transform(dataset)
                        
                        # Calculate metrics after DIR
                        dir_metrics = self.detect_bias(dataset_dir, privileged_groups, unprivileged_groups)
                        logger.info("Après mitigation DIR:")
                        logger.info(f"Disparate Impact: {dir_metrics.disparate_impact:.4f}")
                        logger.info(f"Statistical Parity Difference: {dir_metrics.statistical_parity_difference:.4f}")
                        
                        # Choose best mitigation method
                        if dir_metrics.is_biased and reweighed_metrics.is_biased:
                            logger.info("Les deux méthodes n'ont pas complètement éliminé les biais.")
                            # Choose method with better metrics
                            if abs(1 - dir_metrics.disparate_impact) < abs(1 - reweighed_metrics.disparate_impact):
                                mitigated_metrics = dir_metrics
                                best_datasets[feature] = dataset_dir
                                method = "DisparateImpactRemover"
                            else:
                                mitigated_metrics = reweighed_metrics
                                best_datasets[feature] = dataset_reweighed
                                method = "Reweighing"
                        elif dir_metrics.is_biased:
                            mitigated_metrics = reweighed_metrics
                            best_datasets[feature] = dataset_reweighed
                            method = "Reweighing"
                        else:
                            mitigated_metrics = dir_metrics
                            best_datasets[feature] = dataset_dir
                            method = "DisparateImpactRemover"
                    else:
                        mitigated_metrics = reweighed_metrics
                        best_datasets[feature] = dataset_reweighed
                        method = "Reweighing"
                    
                    # Add results to output dictionary
                    results[feature] = {
                        'original': original_metrics,
                        'mitigated': mitigated_metrics,
                        'method': method
                    }
                    
                    # Evaluate model impact if requested
                    if self.config and getattr(self.config, 'evaluate_model_impact', False):
                        acc_orig, acc_mitigated = self._evaluate_model(dataset, best_datasets[feature])
                        results[feature]['model_accuracy_original'] = acc_orig
                        results[feature]['model_accuracy_mitigated'] = acc_mitigated
                else:
                    logger.info(f"VERDICT: Le dataset n'est PAS BIAISÉ pour la feature {feature}.")
                    results[feature] = {
                        'original': original_metrics,
                        'mitigated': None,
                        'method': None
                    }
                    best_datasets[feature] = dataset
                
                # Log results
                self._log_feature_results(feature, results[feature])

                self.audit_logger.complete_operation(
                    name=f"Fairness Analysis {feature}",
                    start_time=start_time_2,
                    description=f"Analyze and mitigate bias for feature {feature}",
                    parameters={},
                    changes_made={"results": results[feature]},
                    input_df=df_copy,
                    output_df=self.data,
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
            start_time=start_time,
            description="Analyze and mitigate bias for each sensitive feature",
            parameters={},
            changes_made={"results": results},
            input_df=df_copy,
            output_df=self.data,
        )
        return results, best_datasets
        
    def _calculate_group_metrics(self, dataset: BinaryLabelDataset, feature: str) -> Dict[str, float]:
        """Calculate metrics for each group in a sensitive feature."""
        metrics = {}
        for value in [0, 1]:  # Only binary values after preprocessing
            mask = dataset.protected_attributes[:, 0] == value
            positive_rate = np.mean(dataset.labels[mask] == self.favorable_values)
            metrics[f'group_{value}_positive_rate'] = float(positive_rate)
        return metrics
        
    def _log_feature_results(self, feature: str, result: Dict[str, Any]) -> None:
        """Log fairness analysis results for a feature."""
        logger.info(f"Fairness Analysis Results for {feature}:")
        
        if 'original' in result:
            logger.info(f"Original Disparate Impact: {result['original'].disparate_impact:.4f}")
            logger.info(f"Original Statistical Parity Difference: {result['original'].statistical_parity_difference:.4f}")
            if result['original'].equal_opportunity_difference is not None:
                logger.info(f"Original Equal Opportunity Difference: {result['original'].equal_opportunity_difference:.4f}")
            if result['original'].average_odds_difference is not None:
                logger.info(f"Original Average Odds Difference: {result['original'].average_odds_difference:.4f}")
            
            for group, rate in result['original'].group_metrics.items():
                logger.info(f"Original {group}: {rate:.4f}")
        
        if 'mitigated' in result and result['mitigated'] is not None:
            logger.info(f"Mitigated Disparate Impact: {result['mitigated'].disparate_impact:.4f}")
            logger.info(f"Mitigated Statistical Parity Difference: {result['mitigated'].statistical_parity_difference:.4f}")
            if result['mitigated'].equal_opportunity_difference is not None:
                logger.info(f"Mitigated Equal Opportunity Difference: {result['mitigated'].equal_opportunity_difference:.4f}")
            if result['mitigated'].average_odds_difference is not None:
                logger.info(f"Mitigated Average Odds Difference: {result['mitigated'].average_odds_difference:.4f}")
            
            for group, rate in result['mitigated'].group_metrics.items():
                logger.info(f"Mitigated {group}: {rate:.4f}")
            
            logger.info(f"Mitigation method used: {result.get('method', 'Unknown')}")
        
        if 'model_accuracy_original' in result and 'model_accuracy_mitigated' in result:
            logger.info(f"Model accuracy before mitigation: {result['model_accuracy_original']:.4f}")
            logger.info(f"Model accuracy after mitigation: {result['model_accuracy_mitigated']:.4f}")
            impact = result['model_accuracy_mitigated'] - result['model_accuracy_original']
            logger.info(f"Accuracy impact: {impact:.4f} points")

    def _evaluate_model(self, original_dataset, transformed_dataset):
        """Evaluate model performance before and after mitigation."""
        logger.info("=== Évaluation de l'impact sur les performances d'un modèle ===")
        
        try:
            # Prepare original data
            X_orig = original_dataset.features
            y_orig = original_dataset.labels.ravel()
            X_train_orig, X_test_orig, y_train_orig, y_test_orig = train_test_split(
                X_orig, y_orig, test_size=0.3, random_state=42
            )
            
            # Prepare transformed data
            X_trans = transformed_dataset.features
            y_trans = transformed_dataset.labels.ravel()
            X_train_trans, X_test_trans, y_train_trans, y_test_trans = train_test_split(
                X_trans, y_trans, test_size=0.3, random_state=42
            )
            
            # Check if binary or multiclass problem
            unique_classes = np.unique(y_orig)
            if len(unique_classes) == 2:
                model_type = "binaire"
            else:
                model_type = "multiclasse"
            
            logger.info(f"Type de problème détecté: {model_type} avec {len(unique_classes)} classes")
            
            # Train and evaluate original model
            model_orig = RandomForestClassifier(n_estimators=100, random_state=42)
            model_orig.fit(X_train_orig, y_train_orig)
            y_pred_orig = model_orig.predict(X_test_orig)
            
            # Train and evaluate transformed model
            model_trans = RandomForestClassifier(n_estimators=100, random_state=42)
            model_trans.fit(X_train_trans, y_train_trans)
            y_pred_trans = model_trans.predict(X_test_trans)
            
            # Display results
            acc_orig = accuracy_score(y_test_orig, y_pred_orig)
            acc_trans = accuracy_score(y_test_trans, y_pred_trans)
            
            logger.info("Modèle original:")
            logger.info(f"Précision: {acc_orig:.4f}")
            logger.info("Matrice de confusion:")
            logger.info(confusion_matrix(y_test_orig, y_pred_orig))
            
            logger.info("Modèle après mitigation:")
            logger.info(f"Précision: {acc_trans:.4f}")
            logger.info("Matrice de confusion:")
            logger.info(confusion_matrix(y_test_trans, y_pred_trans))
            
            # Check if mitigation maintained performance
            performance_drop = acc_orig - acc_trans
            if performance_drop > 0.05:
                logger.info(f"Attention: La mitigation a réduit la précision du modèle de {performance_drop:.4f} points")
            else:
                logger.info(f"La mitigation a eu un impact limité sur la précision ({performance_drop:.4f} points)")
            
            return acc_orig, acc_trans
            
        except Exception as e:
            logger.error(f"Erreur lors de l'évaluation du modèle: {e}")
            logger.info("L'évaluation du modèle n'a pas pu être effectuée, possiblement en raison de la complexité des données.")
            return None, None

    def analyze_code_biases(self):
        """Analyze code paths for potential ethical biases using either syntax or AI analysis.
        
        Returns:
            List of analysis results (either CodeBiasResult or AI analysis results)
        """
        results = []
        try:
            if not self.config or not self.config.get("code_analysis_paths", None):
                logger.info("No code paths specified for analysis")
                return []

            analysis_type = self.config.get("code_analysis_type", "ai").lower()
            if analysis_type not in ['syntax', 'ai']:
                logger.warning(f"Invalid analysis type '{analysis_type}'. Defaulting to 'ai'")
                analysis_type = 'ai'

            logger.info(f"Starting code bias analysis using {analysis_type} analysis...")
            self.audit_logger.start_operation(
                name="Code Bias Analysis",
                description=f"Analyzing code paths for potential ethical biases using {analysis_type} analysis",
                parameters={
                    "paths": self.config.get("code_analysis_paths", None),
                    "analysis_type": analysis_type
                },
                df=self.data
            )
            start_time = datetime.now()

            if analysis_type == 'syntax':
                analyzer = CodeBiasAnalyzer()
                for path in self.config.get("code_analysis_paths", None):
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
                for path in self.config.get("code_analysis_paths", None):
                    path_results = analyzer.analyze_path(path)
                    results.extend(path_results)

                    for result in path_results:
                        # result = result.data.model_dump()
                        if result['analysis']['is_problematic']:
                            logger.warning(
                                f"Found potential biases in {result['file']}:"
                                f"| Sensitivity Level: {result['analysis']['sensitivity_level']}/10"
                                # f"Recommendations: {', '.join(result['analysis']['recommendations'])}"
                            )

            self.audit_logger.complete_operation(
                name="Code Bias Analysis",
                start_time=start_time,
                description=f"Completed {analysis_type} code bias analysis",
                parameters={
                    "paths": self.config.get("code_analysis_paths", {}),
                    "analysis_type": analysis_type
                },
                changes_made={"results": results},
                input_df=self.data,
                output_df=self.data
            )
        except Exception as e:
            logger.error(f"Error in code bias analysis: {str(e)}")
        return results
