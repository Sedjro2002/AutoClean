import json
from pathlib import Path
from FairAutoCleaner.report_generator import ReportGenerator

def generate_report_from_audit():
    # Path to the audit trail file
    audit_path = Path("tests/output/test_run/audit_trail.json")
    
    # Create report generator
    generator = ReportGenerator(str(audit_path))
    
    # Generate report
    report_path = generator.generate_report(output_dir="tests/output/test_run")
    
    print(f"Report successfully generated at: {report_path}")
    print("You can view the report by opening it in your text editor or browser")

if __name__ == "__main__":
    generate_report_from_audit()
