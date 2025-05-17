from FairAutoCleaner import process_dataset

# Run the demo
# cleaned_df, report_path = process_dataset(
#     config_path="demo/input/german_credit/configs.json",
#     dataset_path="demo/input/german_credit/german_credit_data.csv",
#     output_path="demo/output/german_credit"
# )
cleaned_df, report_path = process_dataset(
    config_path="demo/input/bank_customer_churn/configs.json", 
    dataset_path="demo/input/bank_customer_churn/Bank Customer Churn Prediction.csv",
    output_path="demo/output/bank_customer_churn"
)
# cleaned_df, report_path = process_dataset(
#     config_path="demo/input/student_performance/configs.json",
#     dataset_path="demo/input/student_performance/Student_performance_10k.csv",
#     output_path="demo/output/student_performance"
# )

print(f"Cleaned data saved to {report_path}")