from pathlib import Path
from FairAutoCleaner import process_dataset

def test_data():
    test_dir = Path(__file__).parent / "tests"
    return {
        "config_path": test_dir / "configs.json",
        "dataset_path": test_dir / "datasets/Bank Customer Churn Prediction.csv",
        "output_path": test_dir / "output/test_run"
    }
    
if __name__ == "__main__":
    test_data = test_data()
    cleaned_df, report_path = process_dataset(
        config_path=str(test_data["config_path"]),
        dataset_path=str(test_data["dataset_path"]),
        output_path=str(test_data["output_path"])
    )
    print(cleaned_df.head())
    print(report_path)