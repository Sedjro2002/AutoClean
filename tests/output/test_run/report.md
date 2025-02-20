# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-02-19T17:05:24.056276
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 74.24 ms
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
- **Duration**: 53.50 ms
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
- **Duration**: 2.53 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **credit_score**: 
        - **before**: int64
        - **after**: Int64
    - **age**: 
        - **before**: int64
        - **after**: Int64
    - **churn**: 
        - **before**: int64
        - **after**: Int64
    - **products_number**: 
        - **before**: int64
        - **after**: Int64
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
- **Duration**: 51.22 ms
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
- **Duration**: 45.46 ms
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
- **Duration**: 97.47 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **credit_card**: 
        - **before**: int64
        - **after**: Int64
    - **active_member**: 
        - **before**: int64
        - **after**: Int64
    - **gender**: 
        - **before**: int64
        - **after**: Int64
    - **country**: 
        - **before**: int64
        - **after**: Int64
    - **customer_id**: 
        - **before**: int64
        - **after**: Int64
    - **tenure**: 
        - **before**: int64
        - **after**: Int64

---

### Fairness Analysis gender
_Analyze and mitigate bias for feature gender_

#### Parameters

#### Metrics
- **Duration**: 47.57 ms
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
- **Duration**: 47.57 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
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

---
