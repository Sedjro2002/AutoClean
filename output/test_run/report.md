# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-04-02T16:22:00.899396
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 115.03 ms
- **Input Shape**: 492 rows x 15 columns
- **Output Shape**: 492 rows x 15 columns
- **Success**: True

#### Changes Made

---

### missing_value_handling
_Handle missing values in the dataset_

#### Parameters
- **numerical_method**: knn
- **categorical_method**: knn

#### Metrics
- **Duration**: 82.24 ms
- **Input Shape**: 492 rows x 15 columns
- **Output Shape**: 492 rows x 15 columns
- **Success**: True

#### Changes Made

---

### outlier_handling
_Handle outliers in numerical features_

#### Parameters
- **method**: delete
- **outlier_param**: 1.5

#### Metrics
- **Duration**: 93.00 ms
- **Input Shape**: 492 rows x 15 columns
- **Output Shape**: 458 rows x 15 columns
- **Success**: True

#### Changes Made
- **row_count**: 
	- **before**: 492
	- **after**: 458
	- **difference**: 34
- **statistics_changes**: 
	- **age**: 
		- **mean_change**: -0.35170589697163024
		- **std_change**: -0.027555454647275823
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **fnlwgt**: 
		- **mean_change**: -116.43128483687178
		- **std_change**: 858.966405288782
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **educational-num**: 
		- **mean_change**: -0.10675613306351472
		- **std_change**: -0.026245012188189865
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **capital-gain**: 
		- **mean_change**: -1144.3472503283986
		- **std_change**: -8015.354749544094
		- **min_change**: 0.0
		- **max_change**: -89394.0
	- **capital-loss**: 
		- **mean_change**: -72.0691056910569
		- **std_change**: -357.34106218832295
		- **min_change**: 0.0
		- **max_change**: -2415.0
	- **hours-per-week**: 
		- **mean_change**: -0.3946373415699185
		- **std_change**: -0.015272973119316191
		- **min_change**: 0.0
		- **max_change**: 0.0

---

### field_assignments
_Assign field types_

#### Parameters

#### Metrics
- **Duration**: 145.81 ms
- **Input Shape**: 458 rows x 15 columns
- **Output Shape**: 458 rows x 15 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **gender**: 
		- **before**: object
		- **after**: bool
	- **age**: 
		- **before**: int64
		- **after**: float64
	- **fnlwgt**: 
		- **before**: int64
		- **after**: float64
	- **educational-num**: 
		- **before**: int64
		- **after**: float64
	- **income**: 
		- **before**: object
		- **after**: bool
	- **capital-gain**: 
		- **before**: int64
		- **after**: float64
	- **capital-loss**: 
		- **before**: int64
		- **after**: float64
	- **hours-per-week**: 
		- **before**: int64
		- **after**: float64

---

### datetime_conversion
_Convert and extract datetime features_

#### Parameters
- **granularity**: auto

#### Metrics
- **Duration**: 154.28 ms
- **Input Shape**: 458 rows x 15 columns
- **Output Shape**: 458 rows x 15 columns
- **Success**: True

#### Changes Made

---

### categorical_encoding
_Encode categorical features_

#### Parameters
- **method**: 
	- label

#### Metrics
- **Duration**: 92.65 ms
- **Input Shape**: 458 rows x 15 columns
- **Output Shape**: 458 rows x 15 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **native-country**: 
		- **before**: object
		- **after**: int64
	- **race**: 
		- **before**: object
		- **after**: int64
	- **relationship**: 
		- **before**: object
		- **after**: int64
	- **workclass**: 
		- **before**: object
		- **after**: int64
	- **occupation**: 
		- **before**: object
		- **after**: int64
	- **education**: 
		- **before**: object
		- **after**: int64
	- **marital-status**: 
		- **before**: object
		- **after**: int64

---

### value_rounding
_Round numerical values to appropriate precision_

#### Parameters

#### Metrics
- **Duration**: 209.84 ms
- **Input Shape**: 458 rows x 15 columns
- **Output Shape**: 458 rows x 15 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **native-country**: 
		- **before**: int64
		- **after**: Int64
	- **race**: 
		- **before**: int64
		- **after**: Int64
	- **age**: 
		- **before**: float64
		- **after**: Int64
	- **fnlwgt**: 
		- **before**: float64
		- **after**: Int64
	- **relationship**: 
		- **before**: int64
		- **after**: Int64
	- **workclass**: 
		- **before**: int64
		- **after**: Int64
	- **educational-num**: 
		- **before**: float64
		- **after**: Int64
	- **occupation**: 
		- **before**: int64
		- **after**: Int64
	- **capital-gain**: 
		- **before**: float64
		- **after**: Int64
	- **education**: 
		- **before**: int64
		- **after**: Int64
	- **capital-loss**: 
		- **before**: float64
		- **after**: Int64
	- **marital-status**: 
		- **before**: int64
		- **after**: Int64
	- **hours-per-week**: 
		- **before**: float64
		- **after**: Int64

---

### normalization
_Normalize numerical features_

#### Parameters
- **enabled**: True
- **method**: standard
- **exclude_features**: 

#### Metrics
- **Duration**: 184.59 ms
- **Input Shape**: 458 rows x 15 columns
- **Output Shape**: 458 rows x 15 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **native-country**: 
		- **before**: Int64
		- **after**: float64
	- **race**: 
		- **before**: Int64
		- **after**: float64
	- **gender**: 
		- **before**: bool
		- **after**: float64
	- **age**: 
		- **before**: Int64
		- **after**: float64
	- **fnlwgt**: 
		- **before**: Int64
		- **after**: float64
	- **relationship**: 
		- **before**: Int64
		- **after**: float64
	- **workclass**: 
		- **before**: Int64
		- **after**: float64
	- **educational-num**: 
		- **before**: Int64
		- **after**: float64
	- **occupation**: 
		- **before**: Int64
		- **after**: float64
	- **income**: 
		- **before**: bool
		- **after**: float64
	- **capital-gain**: 
		- **before**: Int64
		- **after**: float64
	- **education**: 
		- **before**: Int64
		- **after**: float64
	- **capital-loss**: 
		- **before**: Int64
		- **after**: float64
	- **marital-status**: 
		- **before**: Int64
		- **after**: float64
	- **hours-per-week**: 
		- **before**: Int64
		- **after**: float64
- **statistics_changes**: 
	- **age**: 
		- **mean_change**: -36.96943231441048
		- **std_change**: -12.63737475966243
		- **min_change**: -18.465800146888565
		- **max_change**: -76.84146191833808
	- **workclass**: 
		- **mean_change**: -2.925764192139738
		- **std_change**: -0.16880240599673257
		- **min_change**: -2.5036103620449905
		- **max_change**: -3.3693407539109352
	- **fnlwgt**: 
		- **mean_change**: -188445.40611353712
		- **std_change**: -102301.720604147
		- **min_change**: -20309.645325369373
		- **max_change**: -599052.9819192648
	- **education**: 
		- **mean_change**: -10.120087336244541
		- **std_change**: -2.649509764314898
		- **min_change**: -2.7751998435431124
		- **max_change**: -12.936023706154021
	- **educational-num**: 
		- **mean_change**: -9.925764192139738
		- **std_change**: -1.4924324701744807
		- **min_change**: -5.182012572522626
		- **max_change**: -13.561333615218196
	- **marital-status**: 
		- **mean_change**: -2.7205240174672487
		- **std_change**: -0.4738816192292661
		- **min_change**: -1.8464710826399273
		- **max_change**: -3.774157651584935
	- **occupation**: 
		- **mean_change**: -6.580786026200873
		- **std_change**: -3.173307737157591
		- **min_change**: -1.5781861185884571
		- **max_change**: -12.220744382560193
	- **relationship**: 
		- **mean_change**: -1.5283842794759825
		- **std_change**: -0.6368930778091992
		- **min_change**: -0.9341075103250335
		- **max_change**: -2.87824151226171
	- **race**: 
		- **mean_change**: -3.6921397379912664
		- **std_change**: 0.2133430433549488
		- **min_change**: -4.692065955120925
		- **max_change**: -3.608763276361886
	- **capital-gain**: 
		- **mean_change**: -349.5633187772926
		- **std_change**: -1355.4875408185223
		- **min_change**: -0.257978987313825
		- **max_change**: -10597.431450820592
	- **hours-per-week**: 
		- **mean_change**: -39.81877729257642
		- **std_change**: -10.992336373587586
		- **min_change**: -7.906328865280025
		- **max_change**: -94.06013395037216
	- **native-country**: 
		- **mean_change**: -17.109170305676855
		- **std_change**: -2.323946274636424
		- **min_change**: -5.151180218287384
		- **max_change**: -18.43071438628932
- **feature_stats**: 
	- **mean**: 
		- **age**: 36.96943231441048
		- **workclass**: 2.925764192139738
		- **fnlwgt**: 188445.40611353712
		- **education**: 10.120087336244541
		- **educational-num**: 9.925764192139738
		- **marital-status**: 2.7205240174672487
		- **occupation**: 6.580786026200873
		- **relationship**: 1.5283842794759825
		- **race**: 3.6921397379912664
		- **gender**: 0.6615720524017468
		- **capital-gain**: 349.5633187772926
		- **capital-loss**: 0.0
		- **hours-per-week**: 39.81877729257642
		- **native-country**: 17.109170305676855
		- **income**: 0.8013100436681223
	- **std**: 
		- **age**: 13.623570960065278
		- **workclass**: 1.1686180231934833
		- **fnlwgt**: 102190.97647401555
		- **education**: 3.6466157058167643
		- **educational-num**: 2.490802286760412
		- **marital-status**: 1.4733639985185552
		- **occupation**: 4.1698415343348625
		- **relationship**: 1.636197399744879
		- **race**: 0.7868899911693829
		- **gender**: 0.4731748850929085
		- **capital-gain**: 1355.0069422982017
		- **capital-loss**: 1.0
		- **hours-per-week**: 11.980329448787838
		- **native-country**: 3.3214078290130473
		- **income**: 0.3990141069996326

---

### Fairness Analysis gender
_Analyze and mitigate bias for feature gender_

#### Parameters

#### Metrics
- **Duration**: 2 minutes 11.84 seconds
- **Input Shape**: 458 rows x 15 columns
- **Output Shape**: 458 rows x 15 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: nan
		- **statistical_parity_difference**: nan
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.896774193548387
			- **group_1_positive_rate**: 0.7524752475247525
		- **is_biased**: False
		- **bias_reasons**: 
	- **mitigated**: None
	- **method**: None

---

### Fairness Analysis
_Analyze and mitigate bias for each sensitive feature_

#### Parameters

#### Metrics
- **Duration**: 2 minutes 11.84 seconds
- **Input Shape**: 458 rows x 15 columns
- **Output Shape**: 458 rows x 15 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **gender**: 
		- **original**: 
			- **disparate_impact**: nan
			- **statistical_parity_difference**: nan
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.896774193548387
				- **group_1_positive_rate**: 0.7524752475247525
			- **is_biased**: False
			- **bias_reasons**: 
		- **mitigated**: None
		- **method**: None

---

### dimensionality_reduction
_Reduce data dimensionality_

#### Parameters
- **enabled**: True
- **method**: pca
- **n_components**: None
- **target_explained_variance**: 0.95

#### Metrics
- **Duration**: 67.92 ms
- **Input Shape**: 458 rows x 15 columns
- **Output Shape**: 458 rows x 13 columns
- **Success**: True

#### Changes Made
- **added_columns**: 
	- component_11
	- component_3
	- component_2
	- component_1
	- component_10
	- component_8
	- component_6
	- component_5
	- component_9
	- component_12
	- component_7
	- component_13
	- component_4
- **removed_columns**: 
	- native-country
	- race
	- gender
	- age
	- fnlwgt
	- relationship
	- workclass
	- educational-num
	- occupation
	- income
	- capital-gain
	- education
	- capital-loss
	- marital-status
	- hours-per-week
- **explained_variance_ratio**: 
	- 0.16660897307568076
	- 0.11291087929941063
	- 0.10909631497799938
	- 0.08523680324097911
	- 0.07750175328165566
	- 0.07293872894382399
	- 0.06285564662496028
	- 0.06111982111116474
	- 0.055165815298019706
	- 0.05328450490549953
	- 0.04674552046480781
	- 0.038098630849093866
	- 0.03435378982923322
- **n_components**: 13
- **total_variance_explained**: 0.9759171819023286

---
