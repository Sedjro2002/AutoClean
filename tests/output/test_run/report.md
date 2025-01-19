# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-01-19T03:31:10.756598
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 60.37 ms
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
- **Duration**: 55.47 ms
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
- **Duration**: 60.17 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **gender**: 
        - **before**: object
        - **after**: int64
    - **country**: 
        - **before**: object
        - **after**: int64

---

### value_rounding
_Round numerical values to appropriate precision_

#### Parameters

#### Metrics
- **Duration**: 90.08 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **gender**: 
        - **before**: int64
        - **after**: Int64
    - **age**: 
        - **before**: int64
        - **after**: Int64
    - **credit_card**: 
        - **before**: int64
        - **after**: Int64
    - **products_number**: 
        - **before**: int64
        - **after**: Int64
    - **customer_id**: 
        - **before**: int64
        - **after**: Int64
    - **active_member**: 
        - **before**: int64
        - **after**: Int64
    - **churn**: 
        - **before**: int64
        - **after**: Int64
    - **country**: 
        - **before**: int64
        - **after**: Int64
    - **tenure**: 
        - **before**: int64
        - **after**: Int64
    - **credit_score**: 
        - **before**: int64
        - **after**: Int64

---

### Sensitive Feature Detection
_Use AI to detect potentially sensitive features_

#### Parameters

#### Metrics
- **Duration**: 36.75 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **sensitive_features**: 
    - credit_score
    - gender
    - balance
    - credit_card
    - estimated_salary
- **results**: 
    - **customer_id**
        - **is_sensitive**: False
        - **sensibility_level**: 2
        - **justification**: None
        - **recommendation**: None
        - **column**: customer_id
    - **credit_score**
        - **is_sensitive**: True
        - **sensibility_level**: 7
        - **justification**: Credit score is a financial attribute that can reveal sensitive information about an individual's financial health and creditworthiness. It can be used to discriminate against individuals in financial services and other areas.
        - **recommendation**: Anonymize or aggregate credit score data to reduce the risk of re-identification. Ensure compliance with financial data protection regulations such as GDPR or CCPA. Limit access to this data to authorized personnel only.
        - **column**: credit_score
    - **country**
        - **is_sensitive**: False
        - **sensibility_level**: 1
        - **justification**: None
        - **recommendation**: None
        - **column**: country
    - **gender**
        - **is_sensitive**: True
        - **sensibility_level**: 6
        - **justification**: Gender is a protected characteristic and can be used to discriminate against individuals. It can also lead to bias in downstream applications such as customer churn prediction.
        - **recommendation**: Consider anonymizing or aggregating gender data to prevent direct identification. Ensure that any models using this feature are regularly audited for bias and fairness.
        - **column**: gender
    - **age**
        - **is_sensitive**: False
        - **sensibility_level**: 2
        - **justification**: Age is a demographic attribute that is generally considered non-sensitive and public information. It does not directly reveal personal or confidential information.
        - **recommendation**: None
        - **column**: age
    - **tenure**
        - **is_sensitive**: False
        - **sensibility_level**: 1
        - **justification**: None
        - **recommendation**: None
        - **column**: tenure
    - **balance**
        - **is_sensitive**: True
        - **sensibility_level**: 6
        - **justification**: The 'balance' feature contains financial data, which is considered sensitive. While it does not directly identify individuals, it could potentially be used in combination with other features to re-identify customers or infer financial status.
        - **recommendation**: Anonymize or aggregate the data to reduce the risk of re-identification. Ensure that access to this feature is restricted and that it is used in compliance with financial data protection regulations.
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
        - **justification**: The 'credit_card' feature contains binary data indicating the presence or absence of a credit card. While it does not directly reveal personal information, it is a financial attribute that could be used in conjunction with other data to re-identify individuals or infer financial status, which is sensitive.
        - **recommendation**: Consider anonymizing or aggregating this data to reduce the risk of re-identification. Ensure that access to this feature is restricted and that it is used in compliance with financial data protection regulations.
        - **column**: credit_card
    - **active_member**
        - **is_sensitive**: False
        - **sensibility_level**: 1
        - **justification**: None
        - **recommendation**: None
        - **column**: active_member
    - **estimated_salary**
        - **is_sensitive**: True
        - **sensibility_level**: 6
        - **justification**: The 'estimated_salary' feature contains financial data, which is considered sensitive. While it does not directly identify individuals, it could potentially be used in combination with other data to re-identify individuals or infer personal financial status.
        - **recommendation**: Consider anonymizing or aggregating the salary data to reduce the risk of re-identification. Implement access controls and ensure compliance with financial data protection regulations.
        - **column**: estimated_salary

---

### Code Bias Analysis
_Completed ai code bias analysis_

#### Parameters
- **paths**: 
    - C:/Users/habib/Documents/AutoClean/tests/preprocessing
- **analysis_type**: ai

#### Metrics
- **Duration**: 3 minutes 43.54 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - value:
        - **file**: C:\Users\habib\Documents\AutoClean\tests\preprocessing\data_cleaner.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 
            - **severity**: low
    - value:
        - **file**: C:\Users\habib\Documents\AutoClean\tests\preprocessing\feature_engineering.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 
            - **severity**: low
    - value:
        - **file**: C:\Users\habib\Documents\AutoClean\tests\preprocessing\sampling.py
        - **analysis**: 
            - **is_problematic**: False
            - **sensitivity_level**: 0
            - **problematic_sections**: 
            - **recommendations**: 
            - **severity**: low

---

### Fairness Analysis credit_score
_Analyze and mitigate bias for feature credit_score_

#### Parameters

#### Metrics
- **Duration**: 22.51 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: 1.1172327737252843
        - **statistical_parity_difference**: 0.02254930491594087
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.21489572989076464
            - **group_1_positive_rate**: 0.19234642497482377
    - **mitigated**: 
        - **disparate_impact**: 1.0
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.21489572989076464
            - **group_1_positive_rate**: 0.19234642497482377

---

### Fairness Analysis gender
_Analyze and mitigate bias for feature gender_

#### Parameters

#### Metrics
- **Duration**: 14.37 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: 1.5235566404076464
        - **statistical_parity_difference**: 0.08615610465201876
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.2507153863086066
            - **group_1_positive_rate**: 0.16455928165658787
    - **mitigated**: 
        - **disparate_impact**: 1.0
        - **statistical_parity_difference**: 0.0
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.2507153863086066
            - **group_1_positive_rate**: 0.16455928165658787

---

### Fairness Analysis balance
_Analyze and mitigate bias for feature balance_

#### Parameters

#### Metrics
- **Duration**: 14.22 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: 0.6309047237790232
        - **statistical_parity_difference**: -0.0922
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.1576
            - **group_1_positive_rate**: 0.2498
    - **mitigated**: 
        - **disparate_impact**: 1.0000000000000002
        - **statistical_parity_difference**: 2.7755575615628914e-17
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.1576
            - **group_1_positive_rate**: 0.2498

---

### Fairness Analysis credit_card
_Analyze and mitigate bias for feature credit_card_

#### Parameters

#### Metrics
- **Duration**: 13.52 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: 1.0312458270540432
        - **statistical_parity_difference**: 0.006306740995741661
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.20814940577249574
            - **group_1_positive_rate**: 0.20184266477675408
    - **mitigated**: 
        - **disparate_impact**: 0.9999999999999998
        - **statistical_parity_difference**: -5.551115123125783e-17
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.20814940577249574
            - **group_1_positive_rate**: 0.20184266477675408

---

### Fairness Analysis estimated_salary
_Analyze and mitigate bias for feature estimated_salary_

#### Parameters

#### Metrics
- **Duration**: 13.62 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **original**: 
        - **disparate_impact**: 0.9548944337811901
        - **statistical_parity_difference**: -0.009399999999999992
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.199
            - **group_1_positive_rate**: 0.2084
    - **mitigated**: 
        - **disparate_impact**: 0.9999999999999998
        - **statistical_parity_difference**: -5.551115123125783e-17
        - **group_metrics**: 
            - **group_0_positive_rate**: 0.199
            - **group_1_positive_rate**: 0.2084

---

### Fairness Analysis
_Analyze and mitigate bias for each sensitive feature_

#### Parameters

#### Metrics
- **Duration**: 80.66 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
    - **credit_score**: 
        - **original**: 
            - **disparate_impact**: 1.1172327737252843
            - **statistical_parity_difference**: 0.02254930491594087
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.21489572989076464
                - **group_1_positive_rate**: 0.19234642497482377
        - **mitigated**: 
            - **disparate_impact**: 1.0
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.21489572989076464
                - **group_1_positive_rate**: 0.19234642497482377
    - **gender**: 
        - **original**: 
            - **disparate_impact**: 1.5235566404076464
            - **statistical_parity_difference**: 0.08615610465201876
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.2507153863086066
                - **group_1_positive_rate**: 0.16455928165658787
        - **mitigated**: 
            - **disparate_impact**: 1.0
            - **statistical_parity_difference**: 0.0
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.2507153863086066
                - **group_1_positive_rate**: 0.16455928165658787
    - **balance**: 
        - **original**: 
            - **disparate_impact**: 0.6309047237790232
            - **statistical_parity_difference**: -0.0922
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.1576
                - **group_1_positive_rate**: 0.2498
        - **mitigated**: 
            - **disparate_impact**: 1.0000000000000002
            - **statistical_parity_difference**: 2.7755575615628914e-17
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.1576
                - **group_1_positive_rate**: 0.2498
    - **credit_card**: 
        - **original**: 
            - **disparate_impact**: 1.0312458270540432
            - **statistical_parity_difference**: 0.006306740995741661
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.20814940577249574
                - **group_1_positive_rate**: 0.20184266477675408
        - **mitigated**: 
            - **disparate_impact**: 0.9999999999999998
            - **statistical_parity_difference**: -5.551115123125783e-17
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.20814940577249574
                - **group_1_positive_rate**: 0.20184266477675408
    - **estimated_salary**: 
        - **original**: 
            - **disparate_impact**: 0.9548944337811901
            - **statistical_parity_difference**: -0.009399999999999992
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.199
                - **group_1_positive_rate**: 0.2084
        - **mitigated**: 
            - **disparate_impact**: 0.9999999999999998
            - **statistical_parity_difference**: -5.551115123125783e-17
            - **group_metrics**: 
                - **group_0_positive_rate**: 0.199
                - **group_1_positive_rate**: 0.2084

---
