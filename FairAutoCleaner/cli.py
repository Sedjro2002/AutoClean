"""Command-line interface for FairAutoClean."""
import argparse
from pathlib import Path
from .interface import process_dataset

def main():
    """Main entry point for the command-line interface."""
    parser = argparse.ArgumentParser(description='FairAutoClean - Automated Fair Data Preprocessing & Cleaning')
    parser.add_argument('--config', type=str, required=True, help='Path to the JSON configuration file')
    parser.add_argument('--dataset', type=str, required=True, help='Path to the dataset CSV file')
    parser.add_argument('--output', type=str, required=True, help='Path to output directory where all generated files will be saved')
    
    args = parser.parse_args()
    
    try:
        cleaned_data, report_path = process_dataset(args.config, args.dataset, args.output)
        print(f"Dataset processed successfully.")
        print(f"- Cleaned dataset saved to: {Path(args.output) / 'cleaned_data.csv'}")
        print(f"- Audit trail saved to: {Path(args.output) / 'audit_trail.json'}")
        print(f"- Report generated at: {report_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
