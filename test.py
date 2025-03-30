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
        "dataset_path": test_dir / "datasets/german_credit_data.csv",
        "output_path": test_dir / "output/test_run"
    }

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
    print("All imports successful - tests ready to run")
    pytest.main(["-v", __file__])
