"""Main interface module for FairAutoClean package."""

from datetime import datetime
import json
import pandas as pd
from pathlib import Path
from typing import Optional, Union, Tuple

from .config import Config
from .audit import AutoCleanAudit, AuditLogger
from .data_processor import DataProcessor
from .autoclean import AutoClean
from .report_generator import ReportGenerator
from .fairness_analyzer import FairnessAnalyzer


def process_dataset(
    config_path: Union[str, Path],
    dataset_path: Union[str, Path],
    output_path: Union[str, Path],
) -> Tuple[pd.DataFrame, str]:
    """Process a dataset using FairAutoClean.

    Args:
        config_path: Path to the JSON configuration file
        dataset_path: Path to the input dataset (CSV format)
        output_path: Path to the output directory where all generated files will be saved

    Returns:
        Tuple[pd.DataFrame, str]: The cleaned dataset and path to the generated report
    """
    try:
        # Convert paths to Path objects
        output_path = Path(output_path)
        output_path.mkdir(parents=True, exist_ok=True)

        # Start audit
        start_time = datetime.now()
        audit = AutoCleanAudit(start_time=start_time.isoformat())
        audit_logger = AuditLogger(audit)

        # Load configuration
        config = Config.from_file(config_path,output_dir=output_path)

        # Initialize data processor
        processor = DataProcessor(config, audit_logger=audit_logger)

        # Load and process data
        df = processor.load_csv(dataset_path)

        # Run AutoClean
        cleaned_data = AutoClean(
            df, audit_logger=audit_logger, output_folder=output_path
        ).output
        
        # Save cleaned dataset
        cleaned_data_path = output_path / "cleaned_data.csv"
        cleaned_data.to_csv(cleaned_data_path, index=False)

        # Run fairness analysis
        sensitive_features = config.dataset_config.get("dataset", {}).get(
            "sensitive_features", []
        )
        analyser = FairnessAnalyzer(
            data=cleaned_data,
            target=config.dataset_config.get("dataset", {}).get("target"),
            sensitive_features=sensitive_features,
            audit_logger=audit_logger,
            config=config,
        )
        results, mitigated_data = analyser.analyze_and_mitigate()
        
        # Save the mitigated dataset
        if mitigated_data is not None:
            mitigated_data_path = output_path / "mitigated_data.csv"
            # mitigated_data.to_csv(mitigated_data_path, index=False)


        # Run code analysis
        results = analyser.analyze_code_biases()
    
        # Save audit trail
        audit_trail = audit.to_dict()
        audit_trail_path = output_path / "audit_trail.json"
        with open(audit_trail_path, "w") as f:
            json.dump(audit_trail, f, indent=4)

        # Generate report
        report_generator = ReportGenerator(str(audit_trail_path))
        report_path = report_generator.generate_report(str(output_path))

        return cleaned_data, report_path

    except Exception as e:
        print(f"Error: {str(e)}")
        raise
