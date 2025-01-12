# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-01-12T22:32:45.450635
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 46.09 ms
- **Input Shape**: 199 rows x 12 columns
- **Output Shape**: 199 rows x 12 columns
- **Success**: True

#### Changes Made

---

### missing_value_handling
_Handle missing values in the dataset_

#### Parameters
- **numerical_method**: knn
- **categorical_method**: knn

#### Metrics
- **Duration**: 361.45 ms
- **Input Shape**: 199 rows x 12 columns
- **Output Shape**: 199 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **writing_score**: 
        - **before**: float64
        - **after**: Int64
    - **reading_score**: 
        - **before**: float64
        - **after**: Int64
    - **test_preparation_course**: 
        - **before**: float64
        - **after**: Int64
    - **science_score**: 
        - **before**: float64
        - **after**: Int64
- **missing_values**: 
    - **before**: 53
    - **after**: 0
    - **difference**: 53
- **statistics_changes**: 
    - **lunch**: 
        - **mean_change**: 0.010154398937693654
        - **std_change**: -0.0036761172660405017
        - **min_change**: 0.0
        - **max_change**: 0.0
    - **test_preparation_course**: 
        - **mean_change**: -0.009972543128011158
        - **std_change**: -0.002245458656442323
        - **min_change**: 0.0
        - **max_change**: 0.0
    - **math_score**: 
        - **mean_change**: -0.1613997824172415
        - **std_change**: -0.08003956071659957
        - **min_change**: 0.0
        - **max_change**: 0.0
    - **reading_score**: 
        - **mean_change**: 0.13021063868565363
        - **std_change**: -0.16916929196295172
        - **min_change**: 0.0
        - **max_change**: 0.0
    - **writing_score**: 
        - **mean_change**: 0.035696617804049424
        - **std_change**: 0.23350129669362119
        - **min_change**: 0.0
        - **max_change**: 13.0
    - **science_score**: 
        - **mean_change**: 0.015101279593842776
        - **std_change**: -0.03322592611109698
        - **min_change**: 0.0
        - **max_change**: 0.0
    - **total_score**: 
        - **mean_change**: 0.05579177940987279
        - **std_change**: -0.2996398919506902
        - **min_change**: 0.0
        - **max_change**: 0.0

---

### outlier_handling
_Handle outliers in numerical features_

#### Parameters
- **method**: winz
- **outlier_param**: 1.5

#### Metrics
- **Duration**: 40.09 ms
- **Input Shape**: 199 rows x 12 columns
- **Output Shape**: 199 rows x 12 columns
- **Success**: True

#### Changes Made

---

### datetime_conversion
_Convert and extract datetime features_

#### Parameters
- **granularity**: s

#### Metrics
- **Duration**: 46.91 ms
- **Input Shape**: 199 rows x 12 columns
- **Output Shape**: 199 rows x 12 columns
- **Success**: True

#### Changes Made

---

### categorical_encoding
_Encode categorical features_

#### Parameters
- **method**: 
    - auto

#### Metrics
- **Duration**: 43.42 ms
- **Input Shape**: 199 rows x 12 columns
- **Output Shape**: 199 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **roll_no**: 
        - **before**: object
        - **after**: int64
    - **race_ethnicity**: 
        - **before**: object
        - **after**: int64
    - **parental_level_of_education**: 
        - **before**: object
        - **after**: int64
    - **grade**: 
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
- **Duration**: 79.75 ms
- **Input Shape**: 199 rows x 12 columns
- **Output Shape**: 199 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
    - **roll_no**: 
        - **before**: int64
        - **after**: Int64
    - **lunch**: 
        - **before**: float64
        - **after**: Int64
    - **race_ethnicity**: 
        - **before**: int64
        - **after**: Int64
    - **parental_level_of_education**: 
        - **before**: int64
        - **after**: Int64
    - **grade**: 
        - **before**: int64
        - **after**: Int64
    - **total_score**: 
        - **before**: float64
        - **after**: Int64
    - **math_score**: 
        - **before**: float64
        - **after**: Int64
    - **gender**: 
        - **before**: int64
        - **after**: Int64

---
