from aif360.datasets import BinaryLabelDataset, StandardDataset
from aif360.metrics import BinaryLabelDatasetMetric
import pandas as pd

df = pd.read_csv("output/test_run/before_normalization.csv")

# Load dataset and prepare for fairness analysis
# dataset = BinaryLabelDataset(
#     df=df,
#     label_names=["income"],
#     protected_attribute_names=["gender"],
#     unfavorable_label=0,
#     favorable_label=1,
# )

dataset = StandardDataset(
    df=df,
    label_name="income",
    favorable_classes=[1],
    protected_attribute_names=["age"],
    privileged_classes=[[1]],
)

# Define privileged/unprivileged groups based on encoded gender values
privileged_groups = [
    {"age": 1}
]  # Encoded value for privileged group
unprivileged_groups = [
    {"age": 0}
]  # Encoded value for unprivileged group

# Calculer les métriques
metric = BinaryLabelDatasetMetric(
    dataset,
    privileged_groups=privileged_groups,
    unprivileged_groups=unprivileged_groups,
)

# Afficher les métriques
print(f"Disparate Impact: {metric.disparate_impact():.3f}")
print(f"Statistical Parity Difference: {metric.statistical_parity_difference():.3f}")
# print(f"Average Odds Difference: {metric.average_odds_difference():.3f}")
# print(f"Equal Opportunity Difference: {metric.equal_opportunity_difference():.3f}")
