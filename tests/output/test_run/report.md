# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-01-19T21:35:00.327813
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 65.37 ms
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
- **Duration**: 70.07 ms
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
- **Duration**: 61.94 ms
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
- **Duration**: 112.60 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **credit_score**: 
		- **before**: int64
		- **after**: Int64
	- **products_number**: 
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
	- **churn**: 
		- **before**: int64
		- **after**: Int64
	- **age**: 
		- **before**: int64
		- **after**: Int64
	- **tenure**: 
		- **before**: int64
		- **after**: Int64
	- **credit_card**: 
		- **before**: int64
		- **after**: Int64
	- **active_member**: 
		- **before**: int64
		- **after**: Int64

---

### normalization
_Normalize numerical features_

#### Parameters
- **enabled**: True
- **method**: standard
- **exclude_features**: 

#### Metrics
- **Duration**: 91.66 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **credit_score**: 
		- **before**: Int64
		- **after**: float64
	- **products_number**: 
		- **before**: Int64
		- **after**: float64
	- **gender**: 
		- **before**: Int64
		- **after**: float64
	- **country**: 
		- **before**: Int64
		- **after**: float64
	- **customer_id**: 
		- **before**: Int64
		- **after**: float64
	- **churn**: 
		- **before**: Int64
		- **after**: float64
	- **age**: 
		- **before**: Int64
		- **after**: float64
	- **tenure**: 
		- **before**: Int64
		- **after**: float64
	- **credit_card**: 
		- **before**: Int64
		- **after**: float64
	- **active_member**: 
		- **before**: Int64
		- **after**: float64
- **statistics_changes**: 
	- **customer_id**: 
		- **mean_change**: -15690940.5694
		- **std_change**: -71935.18607274514
		- **min_change**: -15565702.741068559
		- **max_change**: -15815688.265745305
	- **credit_score**: 
		- **mean_change**: -650.5288
		- **std_change**: -95.65324873238004
		- **min_change**: -353.10950408829376
		- **max_change**: -847.9361162327974
	- **country**: 
		- **mean_change**: -0.7462999999999999
		- **std_change**: 0.1725206746754765
		- **min_change**: -0.9018862432746051
		- **max_change**: -0.4849326233507001
	- **gender**: 
		- **mean_change**: -0.5456999999999999
		- **std_change**: 0.502117976631788
		- **min_change**: -1.0959875190286648
		- **max_change**: -0.08758085047696074
	- **age**: 
		- **mean_change**: -38.9218
		- **std_change**: -9.487756447954297
		- **min_change**: -19.994968753934494
		- **max_change**: -86.93880304203817
	- **tenure**: 
		- **mean_change**: -5.0128
		- **std_change**: -1.8921243732993713
		- **min_change**: -1.7333154938995745
		- **max_change**: -8.275536420528256
	- **balance**: 
		- **mean_change**: -76485.889288
		- **std_change**: -62396.405152382205
		- **min_change**: -1.2258476714090278
		- **max_change**: -250895.29467667828
	- **products_number**: 
		- **mean_change**: -1.5302
		- **std_change**: 0.4183956457513218
		- **min_change**: -1.9115834940401766
		- **max_change**: 0.24637667593441837
	- **credit_card**: 
		- **mean_change**: -0.7055
		- **std_change**: 0.5442095392751791
		- **min_change**: -1.5477679860172513
		- **max_change**: -0.35390833184680304
	- **active_member**: 
		- **mean_change**: -0.5151000000000001
		- **std_change**: 0.5002530752913934
		- **min_change**: -1.0306701134001208
		- **max_change**: -0.029757449062864483
	- **estimated_salary**: 
		- **mean_change**: -100090.239881
		- **std_change**: -57509.49276769441
		- **min_change**: -13.320267893488138
		- **max_change**: -199990.7427998699
	- **churn**: 
		- **mean_change**: -0.20369999999999994
		- **std_change**: 0.5972814197554517
		- **min_change**: -0.5057747646140591
		- **max_change**: 0.9771646787539288
- **feature_stats**: 
	- **mean**: 
		- **customer_id**: 15690940.5694
		- **credit_score**: 650.5288
		- **country**: 0.7463
		- **gender**: 0.5457
		- **age**: 38.9218
		- **tenure**: 5.0128
		- **balance**: 76485.889288
		- **products_number**: 1.5302
		- **credit_card**: 0.7055
		- **active_member**: 0.5151
		- **estimated_salary**: 100090.239881
		- **churn**: 0.2037
	- **std**: 
		- **customer_id**: 71932.58922351804
		- **credit_score**: 96.64846595037089
		- **country**: 0.8274879515739187
		- **gender**: 0.4979071298947224
		- **age**: 10.487282048271611
		- **tenure**: 2.8920297647154327
		- **balance**: 62394.285254125185
		- **products_number**: 0.5816252745539864
		- **credit_card**: 0.4558176718820805
		- **active_member**: 0.4997719379877186
		- **estimated_salary**: 57507.617221165565
		- **churn**: 0.4027484450621752

---

### Fairness Analysis
_Analyze and mitigate bias for each sensitive feature_

#### Parameters

#### Metrics
- **Duration**: 18.19 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 

---

### dimensionality_reduction
_Reduce data dimensionality_

#### Parameters
- **enabled**: True
- **method**: pca
- **n_components**: None
- **target_explained_variance**: 0.95

#### Metrics
- **Duration**: 12.52 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **added_columns**: 
	- component_5
	- component_2
	- component_6
	- component_11
	- component_12
	- component_8
	- component_9
	- component_1
	- component_10
	- component_3
	- component_7
	- component_4
- **removed_columns**: 
	- estimated_salary
	- credit_score
	- products_number
	- gender
	- country
	- customer_id
	- churn
	- age
	- tenure
	- balance
	- credit_card
	- active_member
- **explained_variance_ratio**: 
	- 0.11987147641762325
	- 0.10183365587201637
	- 0.09155091989932106
	- 0.08613044576189435
	- 0.08468156386021565
	- 0.08308879987998272
	- 0.08254900268231037
	- 0.08192915052216247
	- 0.08081482133783167
	- 0.07865445642145577
	- 0.058085883478607984
	- 0.050809823866578264
- **n_components**: 12
- **total_variance_explained**: 0.9999999999999999

---
