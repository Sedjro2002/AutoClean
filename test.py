"""Main script for running AutoClean data processing pipeline."""
from pathlib import Path
from typing import Dict, Any, Optional, List
import json
from loguru import logger
from datetime import datetime
import pandas as pd
from AutoClean import AutoClean
from AutoClean.config import Config
from AutoClean.audit import AutoCleanAudit, AuditLogger
from AutoClean.data_processor import DataProcessor
from AutoClean.fairness_analyzer import FairnessAnalyzer

def main():
    """Main execution function."""
    try:
        start_time = datetime.now()
        audit = AutoCleanAudit(
            start_time=start_time.isoformat(),
            # input_file=str(input_data),
            # configuration={
            #     "mode": mode,
            #     "duplicates": duplicates,
            #     "missing_num": missing_num,
            #     "missing_categ": missing_categ,
            #     "encode_categ": encode_categ,
            #     "extract_datetime": extract_datetime,
            #     "outliers": outliers,
            #     "outlier_param": outlier_param,
            #     "custom_config": config
            # }
        )
        audit_logger = AuditLogger(audit)

        # Load configuration
        config = Config.from_file("configs.json")
        
        # Initialize data processor
        processor = DataProcessor(config, audit_logger=audit_logger)
        
        # Load and process data
        df = processor.load_csv("Student_performance_10k.csv")
        
        # Generate profiles
        # profile = processor.generate_profile(df, "before_preprocessing")
        
        # Run AutoClean
        cleaned_data = AutoClean(df, audit_logger=audit_logger).output
        
        # Run fairness analysis
        sensitive_features = config.dataset_config.get('dataset', {}).get('sensitive_features')
        fairness_results = analyze_fairness(cleaned_data, 
                                          config.dataset_config['dataset']['target'],
                                          sensitive_features, audit_logger=audit_logger, config=config)
        
        # Save fairness results
        with open(config.output_dir / 'fairness_results.json', 'w') as f:
            json.dump(fairness_results, f, indent=2, default=lambda x: x.__dict__)
        
        # Save cleaned data
        cleaned_data.to_csv(config.output_dir / "cleaned_data.csv", index=False)
        
        # Save audit trail
        end_time = datetime.now()
        audit.end_time = end_time.isoformat()
        audit.complete_audit()
        audit.save(config.output_dir / "audit_trail.json")


    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise

def analyze_fairness(data: pd.DataFrame, target: str, sensitive_features: Optional[List[str]] = None, audit_logger: Optional[Any] = None, config: Optional[Config] = None) -> Dict:
    """Run fairness analysis on the dataset."""
    analyzer = FairnessAnalyzer(
        data=data,
        target=target,
        sensitive_features=sensitive_features,
        audit_logger=audit_logger,
        config=config
    )
    
    return analyzer.analyze_and_mitigate()

if __name__ == "__main__":
    main()
