from AutoClean import AutoClean
import pandas as pd
from ai_agent import risky_feature_detector
import ydata_profiling
import pathlib
import json
import os
from ai_agent.main import risky_feature_detector
import csv
from fairness.mitage_bias import FairnessAnalyzer
import pprint
csv_file = open("Student_performance_10k.csv", 'r')

temp_lines = csv_file.readline() + '\n' + csv_file.readline()
dialect = csv.Sniffer().sniff(temp_lines, delimiters=';,')

df = pd.read_csv('Student_performance_10k.csv',delimiter=dialect.delimiter)

configs = json.load(open("configs.json"))

output_folder = pathlib.Path(__file__).parent / "output"
if not pathlib.Path.exists(output_folder):
    os.mkdir(output_folder)
    

#TODO: check the size of the dataframe to know what type of profiler to use
if df.shape[0] < 10000:
    profile = ydata_profiling.ProfileReport(df, title="Before data preprocessing", explorative=True)
else:
    profile = ydata_profiling.ProfileReport(df.sample(1000), title="Before data preprocessing", explorative=True)
profile.to_file(output_folder / "before_preprocessing_profile.html")
profile.to_file(output_folder / "before_preprocessing_profile.json")

output=AutoClean(df)
# print(output.output.head(10))
print('==========')
print(profile.description_set.variables.keys())
print('==========')
results = {}
for variable in df.columns:
    if variable not in profile.description_set.variables.keys():
        continue
    else:
        agent_input = {}
        # agent_input[variable] = {}
        x = profile.description_set.variables[variable]
        # try:
        #     agent_input[variable]["percentage_distinct"] = profile.description_set.variables[variable]["p_distinct"]
        #     agent_input[variable]["percentage_unique"] = profile.description_set.variables[variable]["p_unique"]
        #     agent_input[variable]["type"] = profile.description_set.variables[variable]["type"]
        #     value_counts_without_nan : dict = profile.description_set.variables[variable]["value_counts_without_nan"]
        #     if len(value_counts_without_nan.keys()) <= 10:
        #         agent_input[variable]["value_counts_without_nan"] = value_counts_without_nan
        #     # if agent_input[variable]["type"] != "Boolean":
        #     #     agent_input[variable]["chi_squared"] = profile.description_set.variables[variable]["chi_squared"]
        #     agent_input['all_variables'] = profile.description_set.variables.keys()
        #     print(agent_input)
        #     print('\n')
        # except:
        #     continue
        agent_input['name'] = variable
        agent_input['content'] = df[variable].sample(5).to_list()
        agent_input['context'] = {}
        agent_input['context']['dataset_summary'] = configs['dataset']
        agent_input['variable_infos'] = configs['columns'][variable]
        print(agent_input)
        try:
            result = risky_feature_detector.run_sync(str(agent_input))
            results[variable] = result.data.model_dump()
        except:
            continue
        

print('=====result=====')
pprint.pprint(results,indent=3)
with open('ai_response.json', 'w+') as f:
    f.write(json.dumps(results))

print('=====result=====')
output.output.to_csv("german_credit_data_cleaned.csv")


# ---------------------------fairness check

analyzer = FairnessAnalyzer(
        data=output.output,
        sensitive_features=['gender'],
        target='grade',
        # features=['parental_level_of_education']
    )
    
    # Préparer les données
X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = analyzer.prepare_data()

# Analyser et mitiger les biais
results, mitigators = analyzer.mitigate_bias(
    X_train, y_train, sensitive_train,
    X_test, y_test, sensitive_test
)

# print("\nRésultats:")
# pprint.pprint(results)

# print("\nMitigators:")
# pprint.pprint(mitigators)

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


















