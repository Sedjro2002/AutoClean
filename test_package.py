from AutoClean import process_dataset

# Process the dataset
cleaned_df, report_path = process_dataset(
    config_path="configs.json",
    dataset_path="./datasets/Bank Customer Churn Prediction.csv",
    output_path="./output/test_run"
)

print("Shape of cleaned dataset:", cleaned_df.shape)
print("\nFirst few rows of cleaned dataset:")
print(cleaned_df.head())
print("\nReport generated at:", report_path)
