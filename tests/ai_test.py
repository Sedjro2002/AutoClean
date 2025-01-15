
import pandas as pd
from ai_agent.main import risky_feature_detector
import csv
import pprint
csv_file = open("german_credit_data.csv", 'r')

temp_lines = csv_file.readline() + '\n' + csv_file.readline()
dialect = csv.Sniffer().sniff(temp_lines, delimiters=';,')

df = pd.read_csv('german_credit_data.csv',delimiter=dialect.delimiter)

df_sample = df["OwnsProperty"].sample(5).to_csv(index=False)

pprint.pprint(df_sample)

result = risky_feature_detector.run_sync(df_sample)


pprint.pprint(result.data)