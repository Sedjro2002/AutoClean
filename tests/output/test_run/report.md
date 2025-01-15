# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-01-13T01:00:43.769224
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 55.94 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made

---

### missing_value_handling
_Handle missing values in the dataset_

#### Parameters
- **numerical_method**: auto
- **categorical_method**: auto

#### Metrics
- **Duration**: 67.61 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made

---

### outlier_handling
_Handle outliers in numerical features_

#### Parameters
- **method**: winz
- **outlier_param**: 1.5

#### Metrics
- **Duration**: 1.49 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **statistics_changes**: 
    - **credit_score**: 
        - **mean_change**: 0.0324999999999136
        - **std_change**: -0.09459638046455154
        - **min_change**: 33.0
        - **max_change**: 0.0
    - **age**: 
        - **mean_change**: -0.2609999999999957
        - **std_change**: -0.7411022300551995
        - **min_change**: 0.0
        - **max_change**: -30.0
    - **products_number**: 
        - **mean_change**: -0.006000000000000005
        - **std_change**: -0.020721363263916825
        - **min_change**: 0.0
        - **max_change**: -1.0
    - **churn**: 
        - **mean_change**: -0.2037
        - **std_change**: -0.4027685839948609
        - **min_change**: 0.0
        - **max_change**: -1.0

---

### datetime_conversion
_Convert and extract datetime features_

#### Parameters
- **granularity**: s

#### Metrics
- **Duration**: 59.97 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made

---

### categorical_encoding
_Encode categorical features_

#### Parameters
- **method**: 
    - auto

#### Metrics
- **Duration**: 55.83 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **country**: 
        - **before**: object
        - **after**: int64
    - **gender**: 
        - **before**: object
        - **after**: int64

---

### value_rounding
_Round numerical values to appropriate precision_

#### Parameters

#### Metrics
- **Duration**: 89.60 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **tenure**: 
        - **before**: int64
        - **after**: Int64
    - **country**: 
        - **before**: int64
        - **after**: Int64
    - **credit_card**: 
        - **before**: int64
        - **after**: Int64
    - **gender**: 
        - **before**: int64
        - **after**: Int64
    - **products_number**: 
        - **before**: int64
        - **after**: Int64
    - **credit_score**: 
        - **before**: int64
        - **after**: Int64
    - **active_member**: 
        - **before**: int64
        - **after**: Int64
    - **customer_id**: 
        - **before**: int64
        - **after**: Int64
    - **age**: 
        - **before**: int64
        - **after**: Int64
    - **churn**: 
        - **before**: int64
        - **after**: Int64

---

### Sensitive Feature Detection
_Use AI to detect potentially sensitive features_

#### Parameters

#### Metrics
- **Duration**: 36.23 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **sensitive_features**: 
    - credit_score
    - gender
    - credit_card
    - estimated_salary
- **results**: 
    - **customer_id**
        - **is_sensitive**: False
        - **sensibility_level**: 0
        - **justification**: The 'customer_id' feature is a unique identifier for each customer and does not contain any personal, confidential, or sensitive information that could be used to discriminate against individuals or reveal sensitive characteristics.
        - **recommendation**: None
        - **column**: customer_id
    - **credit_score**
        - **is_sensitive**: True
        - **sensibility_level**: 8
        - **justification**: The credit_score feature contains financial data that can be used to infer a person's financial health and creditworthiness. This information is sensitive as it can be used to discriminate against individuals in financial decisions.
        - **recommendation**: Consider anonymizing or aggregating the credit_score data to reduce the risk of misuse. Ensure that access to this feature is restricted and that it is used in compliance with data protection regulations.
        - **column**: credit_score
    - **country**
        - **is_sensitive**: False
        - **sensibility_level**: 0
        - **justification**: The 'country' feature contains numerical codes that do not directly reveal personal, confidential, or sensitive information about individuals. It does not indicate ethnic origin, political opinions, health, financial data, or other sensitive characteristics.
        - **recommendation**: None
        - **column**: country
    - **gender**
        - **is_sensitive**: True
        - **sensibility_level**: 8
        - **justification**: The 'gender' feature can be used to discriminate against certain groups based on gender. It is a sensitive characteristic that could lead to bias in the analysis or predictions.
        - **recommendation**: Consider anonymizing or removing the 'gender' feature if it is not essential for the analysis. If it must be included, ensure that the model is regularly audited for bias and that the data is handled in compliance with privacy regulations.
        - **column**: gender
    - **age**
        - **is_sensitive**: False
        - **sensibility_level**: 2
        - **justification**: Age is generally not considered highly sensitive, but it can be used in combination with other features to infer sensitive information. In this context, it is used to predict customer churn, which does not directly reveal sensitive personal details.
        - **recommendation**: None
        - **column**: age
    - **tenure**
        - **is_sensitive**: False
        - **sensibility_level**: 2
        - **justification**: The 'tenure' feature represents the number of months a customer has been with the bank. While it is not directly sensitive, it could potentially be used in combination with other features to infer customer behavior or loyalty, which might have indirect implications.
        - **recommendation**: None
        - **column**: tenure
    - **balance**
        - **is_sensitive**: False
        - **sensibility_level**: 0
        - **justification**: The 'balance' feature represents the account balance of bank customers. This information is not inherently sensitive as it does not reveal personal, confidential, or discriminatory details about individuals.
        - **recommendation**: None
        - **column**: balance
    - **products_number**
        - **is_sensitive**: False
        - **sensibility_level**: 0
        - **justification**: None
        - **recommendation**: None
        - **column**: products_number
    - **credit_card**
        - **is_sensitive**: True
        - **sensibility_level**: 9
        - **justification**: The 'credit_card' feature indicates whether a customer has a credit card or not. This information can be sensitive as it relates to financial data, which is personal and confidential. It could potentially be used to discriminate against certain groups based on their financial status.
        - **recommendation**: Consider anonymizing or encrypting this feature to protect customer privacy. Additionally, ensure that access to this data is restricted to authorized personnel only.
        - **column**: credit_card
    - **active_member**
        - **is_sensitive**: False
        - **sensibility_level**: 0
        - **justification**: The 'active_member' feature indicates whether a customer is an active member of the bank. This information is not personal, confidential, or likely to reveal sensitive characteristics that could be used to discriminate against certain groups.
        - **recommendation**: None
        - **column**: active_member
    - **estimated_salary**
        - **is_sensitive**: True
        - **sensibility_level**: 7
        - **justification**: The 'estimated_salary' feature contains financial data, which is considered sensitive as it can reveal personal financial status and potentially be used for discriminatory practices.
        - **recommendation**: Anonymize or aggregate the salary data to reduce the risk of identifying individuals. Ensure that access to this data is restricted and comply with relevant data protection regulations.
        - **column**: estimated_salary

---

### Code Bias Analysis
_Completed ai code bias analysis_

#### Parameters
- **paths**: 
    - c:/Users/habib/Documents/trywindsurf/preprocessing
- **analysis_type**: ai

#### Metrics
- **Duration**: 7.87 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - value:
        - **file**: c:\Users\habib\Documents\trywindsurf\preprocessing\data_cleaner.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 
    - value:
        - **file**: c:\Users\habib\Documents\trywindsurf\preprocessing\feature_engineering.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 
    - value:
        - **file**: c:\Users\habib\Documents\trywindsurf\preprocessing\sampling.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 

---

### Fairness Analysis credit_score
_Analyze and mitigate bias for feature credit_score_

#### Parameters

#### Metrics
- **Duration**: 1 minutes 30.41 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: nan
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.0
            - **group_1_positive_rate**: 0.0
    - **mitigated**: 
        - **disparate_impact**: nan
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.0
            - **group_1_positive_rate**: 0.0

---

### Fairness Analysis gender
_Analyze and mitigate bias for feature gender_

#### Parameters

#### Metrics
- **Duration**: 10.26 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: nan
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.0
            - **group_1_positive_rate**: 0.0
    - **mitigated**: 
        - **disparate_impact**: nan
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.0
            - **group_1_positive_rate**: 0.0

---

### Fairness Analysis credit_card
_Analyze and mitigate bias for feature credit_card_

#### Parameters

#### Metrics
- **Duration**: 24.75 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: nan
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.0
            - **group_1_positive_rate**: 0.0
    - **mitigated**: 
        - **disparate_impact**: nan
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.0
            - **group_1_positive_rate**: 0.0

---

### Fairness Analysis estimated_salary
_Analyze and mitigate bias for feature estimated_salary_

#### Parameters

#### Metrics
- **Duration**: 13.12 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: nan
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.0
            - **group_1_positive_rate**: 0.0
    - **mitigated**: 
        - **disparate_impact**: nan
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.0
            - **group_1_positive_rate**: 0.0

---

### Fairness Analysis
_Analyze and mitigate bias for each sensitive feature_

#### Parameters

#### Metrics
- **Duration**: 1 minutes 40.72 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **credit_score**: 
        - **original**: 
            - **disparate_impact**: nan
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.0
                - **group_1_positive_rate**: 0.0
        - **mitigated**: 
            - **disparate_impact**: nan
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.0
                - **group_1_positive_rate**: 0.0
    - **gender**: 
        - **original**: 
            - **disparate_impact**: nan
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.0
                - **group_1_positive_rate**: 0.0
        - **mitigated**: 
            - **disparate_impact**: nan
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.0
                - **group_1_positive_rate**: 0.0
    - **credit_card**: 
        - **original**: 
            - **disparate_impact**: nan
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.0
                - **group_1_positive_rate**: 0.0
        - **mitigated**: 
            - **disparate_impact**: nan
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.0
                - **group_1_positive_rate**: 0.0
    - **estimated_salary**: 
        - **original**: 
            - **disparate_impact**: nan
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.0
                - **group_1_positive_rate**: 0.0
        - **mitigated**: 
            - **disparate_impact**: nan
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.0
                - **group_1_positive_rate**: 0.0

---

### Code Bias Analysis
_Completed ai code bias analysis_

#### Parameters
- **paths**: 
    - c:/Users/habib/Documents/trywindsurf/preprocessing
- **analysis_type**: ai

#### Metrics
- **Duration**: 6.45 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - value:
        - **file**: c:\Users\habib\Documents\trywindsurf\preprocessing\data_cleaner.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 
    - value:
        - **file**: c:\Users\habib\Documents\trywindsurf\preprocessing\feature_engineering.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 
    - value:
        - **file**: c:\Users\habib\Documents\trywindsurf\preprocessing\sampling.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 

---
