import pytest
from pathlib import Path
from FairAutoCleaner import process_dataset
import pandas as pd
from unittest.mock import patch

@pytest.fixture
def test_data():
    test_dir = Path(__file__).parent
    return {
        "config_path": test_dir / "configs.json",
        "dataset_path": test_dir / "datasets/Bank Customer Churn Prediction.csv",
        "output_path": test_dir / "output/test_run"
    }

def mock_analyze_code_biases(self):
    """Mock version of analyze_code_biases that returns empty list"""
    return []

@patch('FairAutoCleaner.fairness_analyzer.FairnessAnalyzer.analyze_code_biases', mock_analyze_code_biases)
def test_process_dataset_success(test_data):
    """Test that process_dataset runs successfully with valid inputs"""
    cleaned_df, report_path = process_dataset(
        config_path=str(test_data["config_path"]),
        dataset_path=str(test_data["dataset_path"]),
        output_path=str(test_data["output_path"])
    )
    
    # Verify outputs
    assert isinstance(cleaned_df, pd.DataFrame)
    assert cleaned_df.shape[0] > 0  # Should have rows
    assert cleaned_df.shape[1] > 0  # Should have columns
    assert Path(report_path).exists()  # Report file should exist

def test_process_dataset_invalid_config(test_data):
    """Test handling of invalid config file"""
    with pytest.raises(Exception):
        process_dataset(
            config_path="invalid_path.json",
            dataset_path=str(test_data["dataset_path"]),
            output_path=str(test_data["output_path"])
        )

def test_process_dataset_invalid_data(test_data):
    """Test handling of invalid dataset file"""
    with pytest.raises(Exception):
        process_dataset(
            config_path=str(test_data["config_path"]),
            dataset_path="invalid_path.csv",
            output_path=str(test_data["output_path"])
        )

@patch('FairAutoCleaner.fairness_analyzer.FairnessAnalyzer.analyze_code_biases', mock_analyze_code_biases)
def test_output_files_created(test_data):
    """Verify that output files are created correctly"""
    # Clean up previous test output
    output_dir = test_data["output_path"]
    for f in output_dir.glob("*"):
        f.unlink()
    
    # Run process
    cleaned_df, report_path = process_dataset(
        config_path=str(test_data["config_path"]),
        dataset_path=str(test_data["dataset_path"]),
        output_path=str(test_data["output_path"])
    )
    
    # Verify files exist
    assert (output_dir / "cleaned_data.csv").exists()
    assert (output_dir / "audit_trail.json").exists()
    assert Path(report_path).exists()

if __name__ == "__main__":
    pytest.main(["-v", __file__])
