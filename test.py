from AutoClean import AutoClean
import pandas as pd
import ydata_profiling
import pathlib
import os
import csv
from fairness.mitage_bias import FairnessAnalyzer
csv_file = open("german_credit_data.csv", 'r')

temp_lines = csv_file.readline() + '\n' + csv_file.readline()
dialect = csv.Sniffer().sniff(temp_lines, delimiters=';,')

df = pd.read_csv('german_credit_data.csv',delimiter=dialect.delimiter)

output=AutoClean(df)

# output_folder = pathlib.Path(__file__).parent / "output"
# if not pathlib.Path.exists(output_folder):
#     os.mkdir(output_folder)
#     
# 
# #TODO: check the size of the dataframe to know what type of profiler to use
# profile = ydata_profiling.ProfileReport(df, title="Before data preprocessing")
# profile.to_file(output_folder / "before_preprocessing_profile.html")
# profile.to_file(output_folder / "before_preprocessing_profile.json")

print(output.output.head(10))

output.output.to_csv("german_credit_data_cleaned.csv")


# ---------------------------fairness check

analyzer = FairnessAnalyzer(
        data=output.output,
        sensitive_features=['Sex'],
        target='Risk',
        #features=['age', 'income']
    )
    
    # Préparer les données
X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = analyzer.prepare_data()

# Analyser et mitiger les biais
results, mitigators = analyzer.mitigate_bias(
    X_train, y_train, sensitive_train,
    X_test, y_test, sensitive_test
)

# Afficher les résultats
for feature, result in results.items(): 
    print(f"\nRésultats pour {feature}:")
    print("\nAvant mitigation:")
    print(f"Disparité démographique: {result['original']['demographic_parity']:.4f}")
    print("Métriques par groupe:")
    print(result['original']['by_group'])
    
    print("\nAprès mitigation:")
    print(f"Disparité démographique: {result['mitigated']['demographic_parity']:.4f}")
    print("Métriques par groupe:")
    print(result['mitigated']['by_group'])


















