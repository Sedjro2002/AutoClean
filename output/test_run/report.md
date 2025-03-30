# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-03-30T18:33:07.118371
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 112.23 ms
- **Input Shape**: 5021 rows x 21 columns
- **Output Shape**: 4982 rows x 21 columns
- **Success**: True

#### Changes Made
- **row_count**: 
	- **before**: 5021
	- **after**: 4982
	- **difference**: 39
- **statistics_changes**: 
	- **LoanDuration**: 
		- **mean_change**: 0.06587886876723559
		- **std_change**: -0.022664884115652484
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **LoanAmount**: 
		- **mean_change**: 12.031429177702194
		- **std_change**: -1.8382033916482214
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **InstallmentPercent**: 
		- **mean_change**: 0.009478776053462035
		- **std_change**: -0.004372296080526361
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **CurrentResidenceDuration**: 
		- **mean_change**: 0.004880425536712085
		- **std_change**: -0.0005158525007218362
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **Age**: 
		- **mean_change**: 0.07125064692162653
		- **std_change**: -0.022639186876647344
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **ExistingCreditsCount**: 
		- **mean_change**: 0.0020378081267826698
		- **std_change**: 0.00025709026358711196
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **Dependents**: 
		- **mean_change**: 0.0004864754702269547
		- **std_change**: 0.0004395055706211126
		- **min_change**: 0.0
		- **max_change**: 0.0

---

### missing_value_handling
_Handle missing values in the dataset_

#### Parameters
- **numerical_method**: knn
- **categorical_method**: knn

#### Metrics
- **Duration**: 141.26 ms
- **Input Shape**: 4982 rows x 21 columns
- **Output Shape**: 4982 rows x 21 columns
- **Success**: True

#### Changes Made
- **missing_values**: 
	- **before**: 6
	- **after**: 0
	- **difference**: 6

---

### outlier_handling
_Handle outliers in numerical features_

#### Parameters
- **method**: delete
- **outlier_param**: 1.5

#### Metrics
- **Duration**: 109.40 ms
- **Input Shape**: 4982 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **row_count**: 
	- **before**: 4982
	- **after**: 4981
	- **difference**: 1
- **statistics_changes**: 
	- **LoanDuration**: 
		- **mean_change**: -0.003923742014112719
		- **std_change**: -0.002327610240177691
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **LoanAmount**: 
		- **mean_change**: -0.7460719662858537
		- **std_change**: -0.3085606747977181
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **InstallmentPercent**: 
		- **mean_change**: -0.0006043841749190371
		- **std_change**: -0.0006980443670374648
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **CurrentResidenceDuration**: 
		- **mean_change**: -0.000429814749278723
		- **std_change**: -0.00030121613055689167
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **Age**: 
		- **mean_change**: -0.007630279687461439
		- **std_change**: -0.012601673909699684
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **ExistingCreditsCount**: 
		- **mean_change**: -0.0005084354670590319
		- **std_change**: -0.001082687642968705
		- **min_change**: 0.0
		- **max_change**: -1.0
	- **Dependents**: 
		- **mean_change**: -0.0001675979319566423
		- **std_change**: -0.00015117831969185813
		- **min_change**: 0.0
		- **max_change**: 0.0

---

### field_assignments
_Assign field types_

#### Parameters

#### Metrics
- **Duration**: 818.24 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **Telephone**: 
		- **before**: object
		- **after**: bool
	- **Age**: 
		- **before**: int64
		- **after**: float64
	- **ForeignWorker**: 
		- **before**: object
		- **after**: bool
	- **Risk**: 
		- **before**: object
		- **after**: bool
	- **Sex**: 
		- **before**: object
		- **after**: bool
	- **ExistingCreditsCount**: 
		- **before**: int64
		- **after**: float64
	- **InstallmentPercent**: 
		- **before**: int64
		- **after**: float64
	- **LoanAmount**: 
		- **before**: int64
		- **after**: float64
	- **Dependents**: 
		- **before**: int64
		- **after**: bool
	- **CurrentResidenceDuration**: 
		- **before**: int64
		- **after**: float64
	- **LoanDuration**: 
		- **before**: int64
		- **after**: float64
- **statistics_changes**: 
	- **Dependents**: 
		- **mean_change**: None
		- **std_change**: None
		- **min_change**: None
		- **max_change**: None

---

### datetime_conversion
_Convert and extract datetime features_

#### Parameters
- **granularity**: auto

#### Metrics
- **Duration**: 136.19 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made

---

### categorical_encoding
_Encode categorical features_

#### Parameters
- **method**: 
	- label

#### Metrics
- **Duration**: 140.19 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **ExistingSavings**: 
		- **before**: object
		- **after**: int64
	- **InstallmentPlans**: 
		- **before**: object
		- **after**: int64
	- **CreditHistory**: 
		- **before**: object
		- **after**: int64
	- **CheckingStatus**: 
		- **before**: object
		- **after**: int64
	- **Housing**: 
		- **before**: object
		- **after**: int64
	- **OthersOnLoan**: 
		- **before**: object
		- **after**: int64
	- **LoanPurpose**: 
		- **before**: object
		- **after**: int64
	- **Job**: 
		- **before**: object
		- **after**: int64
	- **OwnsProperty**: 
		- **before**: object
		- **after**: int64
	- **EmploymentDuration**: 
		- **before**: object
		- **after**: int64

---

### value_rounding
_Round numerical values to appropriate precision_

#### Parameters

#### Metrics
- **Duration**: 284.72 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **ExistingSavings**: 
		- **before**: int64
		- **after**: Int64
	- **Age**: 
		- **before**: float64
		- **after**: Int64
	- **InstallmentPlans**: 
		- **before**: int64
		- **after**: Int64
	- **CreditHistory**: 
		- **before**: int64
		- **after**: Int64
	- **CheckingStatus**: 
		- **before**: int64
		- **after**: Int64
	- **Housing**: 
		- **before**: int64
		- **after**: Int64
	- **ExistingCreditsCount**: 
		- **before**: float64
		- **after**: Int64
	- **InstallmentPercent**: 
		- **before**: float64
		- **after**: Int64
	- **LoanAmount**: 
		- **before**: float64
		- **after**: Int64
	- **CurrentResidenceDuration**: 
		- **before**: float64
		- **after**: Int64
	- **OthersOnLoan**: 
		- **before**: int64
		- **after**: Int64
	- **LoanPurpose**: 
		- **before**: int64
		- **after**: Int64
	- **Job**: 
		- **before**: int64
		- **after**: Int64
	- **LoanDuration**: 
		- **before**: float64
		- **after**: Int64
	- **OwnsProperty**: 
		- **before**: int64
		- **after**: Int64
	- **EmploymentDuration**: 
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
- **Duration**: 229.60 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **ExistingSavings**: 
		- **before**: Int64
		- **after**: float64
	- **Telephone**: 
		- **before**: bool
		- **after**: float64
	- **Age**: 
		- **before**: Int64
		- **after**: float64
	- **InstallmentPlans**: 
		- **before**: Int64
		- **after**: float64
	- **ForeignWorker**: 
		- **before**: bool
		- **after**: float64
	- **Risk**: 
		- **before**: bool
		- **after**: float64
	- **Sex**: 
		- **before**: bool
		- **after**: float64
	- **CreditHistory**: 
		- **before**: Int64
		- **after**: float64
	- **CheckingStatus**: 
		- **before**: Int64
		- **after**: float64
	- **Housing**: 
		- **before**: Int64
		- **after**: float64
	- **ExistingCreditsCount**: 
		- **before**: Int64
		- **after**: float64
	- **InstallmentPercent**: 
		- **before**: Int64
		- **after**: float64
	- **LoanAmount**: 
		- **before**: Int64
		- **after**: float64
	- **Dependents**: 
		- **before**: bool
		- **after**: float64
	- **CurrentResidenceDuration**: 
		- **before**: Int64
		- **after**: float64
	- **OthersOnLoan**: 
		- **before**: Int64
		- **after**: float64
	- **LoanPurpose**: 
		- **before**: Int64
		- **after**: float64
	- **Job**: 
		- **before**: Int64
		- **after**: float64
	- **LoanDuration**: 
		- **before**: Int64
		- **after**: float64
	- **OwnsProperty**: 
		- **before**: Int64
		- **after**: float64
	- **EmploymentDuration**: 
		- **before**: Int64
		- **after**: float64
- **statistics_changes**: 
	- **CheckingStatus**: 
		- **mean_change**: -1.815097370006023
		- **std_change**: -0.21416427405350635
		- **min_change**: -1.4949620486141706
		- **max_change**: -2.0240829542173615
	- **LoanDuration**: 
		- **mean_change**: -21.451917285685607
		- **std_change**: -10.131403921877899
		- **min_change**: -5.5679524437090695
		- **max_change**: -60.177304236837955
	- **CreditHistory**: 
		- **mean_change**: -2.263601686408352
		- **std_change**: -0.5416147976600532
		- **min_change**: -1.4683833646599422
		- **max_change**: -2.873609958231145
	- **LoanPurpose**: 
		- **mean_change**: -4.2381047982332865
		- **std_change**: -1.7845249093292406
		- **min_change**: -1.522118713936125
		- **max_change**: -7.930610748935727
	- **LoanAmount**: 
		- **mean_change**: -3491.0694639630597
		- **std_change**: -2483.8140258836547
		- **min_change**: -251.30448182096504
		- **max_change**: -11672.705688289363
	- **ExistingSavings**: 
		- **mean_change**: -1.8478217225456735
		- **std_change**: -0.33137286916844744
		- **min_change**: -1.3879416771332203
		- **max_change**: -2.383449067919587
	- **EmploymentDuration**: 
		- **mean_change**: -1.4220036137321823
		- **std_change**: -0.23809271012743505
		- **min_change**: -1.1485658984242266
		- **max_change**: -1.9177276998919255
	- **InstallmentPercent**: 
		- **mean_change**: -2.9889580405541056
		- **std_change**: -0.12200253919270532
		- **min_change**: -2.7727052142203723
		- **max_change**: -3.316338669337121
	- **OthersOnLoan**: 
		- **mean_change**: -1.6902228468179081
		- **std_change**: 0.2917149008298796
		- **min_change**: -2.3862607994682996
		- **max_change**: -1.5626558482504354
	- **CurrentResidenceDuration**: 
		- **mean_change**: -2.8586629190925517
		- **std_change**: -0.11393012141214132
		- **min_change**: -2.6685804315673014
		- **max_change**: -3.1799224440771696
	- **OwnsProperty**: 
		- **mean_change**: -1.3095763902830757
		- **std_change**: -0.05696924453613894
		- **min_change**: -1.238998658489591
		- **max_change**: -1.4006793339748038
	- **Age**: 
		- **mean_change**: -35.98594659706886
		- **std_change**: -9.606208026528607
		- **min_change**: -20.601655472397773
		- **max_change**: -70.41554173546427
	- **InstallmentPlans**: 
		- **mean_change**: -1.1092150170648467
		- **std_change**: 0.466756954634992
		- **min_change**: -2.079947537043767
		- **max_change**: -0.32964213178946755
	- **Housing**: 
		- **mean_change**: -1.0620357357960248
		- **std_change**: 0.4042932666394847
		- **min_change**: -1.7826949480570526
		- **max_change**: -0.4255669570278733
	- **ExistingCreditsCount**: 
		- **mean_change**: -1.4669745031118249
		- **std_change**: 0.4354422553714613
		- **min_change**: -1.827086960545917
		- **max_change**: -0.2847652490418646
	- **Job**: 
		- **mean_change**: -1.1977514555310178
		- **std_change**: 0.17161471936417605
		- **min_change**: -1.4458568670850964
		- **max_change**: -0.8244289145452712
- **feature_stats**: 
	- **mean**: 
		- **CheckingStatus**: 1.815097370006023
		- **LoanDuration**: 21.451917285685607
		- **CreditHistory**: 2.263601686408352
		- **LoanPurpose**: 4.2381047982332865
		- **LoanAmount**: 3491.0694639630597
		- **ExistingSavings**: 1.8478217225456735
		- **EmploymentDuration**: 1.4220036137321823
		- **InstallmentPercent**: 2.9889580405541056
		- **Sex**: 0.37984340493876734
		- **OthersOnLoan**: 1.6902228468179081
		- **CurrentResidenceDuration**: 2.8586629190925517
		- **OwnsProperty**: 1.3095763902830757
		- **Age**: 35.98594659706886
		- **InstallmentPlans**: 1.1092150170648465
		- **Housing**: 1.0620357357960248
		- **ExistingCreditsCount**: 1.4669745031118249
		- **Job**: 1.1977514555310178
		- **Dependents**: 0.8349728970086328
		- **Telephone**: 0.5868299538245332
		- **ForeignWorker**: 0.9753061634209998
		- **Risk**: 0.6649267215418591
	- **std**: 
		- **CheckingStatus**: 1.2141427748541294
		- **LoanDuration**: 11.130386865817327
		- **CreditHistory**: 1.5415604268525416
		- **LoanPurpose**: 2.7843457671404312
		- **LoanAmount**: 2484.564684516176
		- **ExistingSavings**: 1.3313396038098164
		- **EmploymentDuration**: 1.2380688088363918
		- **InstallmentPercent**: 1.1219902917862405
		- **Sex**: 0.4853477028515649
		- **OthersOnLoan**: 0.7083143834045798
		- **CurrentResidenceDuration**: 1.113918684367349
		- **OwnsProperty**: 1.0569635255937428
		- **Age**: 10.6052436930396
		- **InstallmentPlans**: 0.5332899014565414
		- **Housing**: 0.5957473189417688
		- **ExistingCreditsCount**: 0.5646014571473831
		- **Job**: 0.8284025084348295
		- **Dependents**: 0.3712050084113143
		- **Telephone**: 0.4924028423139223
		- **ForeignWorker**: 0.15519037023607435
		- **Risk**: 0.4720160765497867

---

### Sensitive Feature Detection
_Use AI to detect potentially sensitive features_

#### Parameters

#### Metrics
- **Duration**: 2 minutes 51.95 seconds
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **sensitive_features**: 
	- CreditHistory
	- ExistingSavings
	- Sex
	- Age
	- Telephone
- **results**: 
	- **CheckingStatus**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'CheckingStatus' appears to contain numerical values without direct identifiers or sensitive context. It is likely a derived or aggregated metric related to credit status, which is not inherently sensitive.
		- **recommendation**: None
		- **column**: CheckingStatus
	- **LoanDuration**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'LoanDuration' appears to represent numerical values related to loan durations, which are not inherently sensitive or personally identifiable. There is no direct or indirect link to personal or confidential information.
		- **recommendation**: None
		- **column**: LoanDuration
	- **CreditHistory**
		- **is_sensitive**: True
		- **sensibility_level**: 6
		- **justification**: The 'CreditHistory' feature, while not directly revealing personal identifiers, can indirectly indicate financial behavior or creditworthiness, which is sensitive financial data. This could lead to potential bias or discrimination in credit-related decisions.
		- **recommendation**: Anonymize or aggregate the data to reduce granularity. Ensure compliance with financial data protection regulations (e.g., GDPR, FCRA) and use fairness-aware algorithms to mitigate bias in downstream applications.
		- **column**: CreditHistory
	- **LoanPurpose**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'LoanPurpose' appears to contain numerical values without direct identifiers or sensitive context. It is likely a transformed or encoded representation of loan purposes, which does not inherently reveal personal or confidential information.
		- **recommendation**: None
		- **column**: LoanPurpose
	- **LoanAmount**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'LoanAmount' feature contains numerical values representing loan amounts, which are not directly linked to personal identifiers or sensitive attributes. However, in certain contexts, large or small loan amounts could indirectly hint at financial status, but the risk is low.
		- **recommendation**: No specific handling is required unless the dataset is combined with other features that could lead to re-identification or bias. Ensure anonymization if used in conjunction with other sensitive data.
		- **column**: LoanAmount
	- **ExistingSavings**
		- **is_sensitive**: True
		- **sensibility_level**: 5
		- **justification**: The 'ExistingSavings' feature contains financial data, which is potentially sensitive as it could reveal personal financial status. While the data is anonymized (no direct identifiers), it could still be used to infer financial behavior or status, posing a moderate risk.
		- **recommendation**: Anonymize or aggregate the data further to reduce re-identification risk. Ensure compliance with financial data protection regulations (e.g., GDPR, CCPA) if applicable. Limit access to authorized personnel only.
		- **column**: ExistingSavings
	- **EmploymentDuration**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'EmploymentDuration' contains numerical values representing employment duration, which is not directly identifiable or linked to personal or sensitive information. It does not reveal protected characteristics, health, financial, or location data.
		- **recommendation**: None
		- **column**: EmploymentDuration
	- **InstallmentPercent**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'InstallmentPercent' contains numerical values representing financial installment percentages, which are not directly linked to personal identifiers or protected characteristics. The data does not reveal sensitive information about individuals.
		- **recommendation**: None
		- **column**: InstallmentPercent
	- **Sex**
		- **is_sensitive**: True
		- **sensibility_level**: 7
		- **justification**: The feature 'Sex' represents gender, which is a protected characteristic under many legal frameworks. It can lead to discrimination or bias in credit-related decisions, especially in the context of the dataset (german_credit_data). The numerical encoding (e.g., 1.2777573509004465, -0.7826212068318695) may obscure direct interpretation but still carries sensitive information.
		- **recommendation**: 1. Avoid using this feature in model training if not necessary. 2. If required, ensure fairness-aware algorithms are applied to mitigate bias. 3. Document the potential impact of this feature on model outcomes for transparency.
		- **column**: Sex
	- **OthersOnLoan**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'OthersOnLoan' consists of numerical values that appear to represent loan-related metrics. There is no indication of personal identifiers, protected characteristics, or other sensitive information. The context suggests it is part of a credit risk dataset, and the values do not reveal any confidential or discriminatory details.
		- **recommendation**: No special handling is required for this feature as it poses minimal risk. However, ensure that the dataset as a whole is reviewed for other potentially sensitive features.
		- **column**: OthersOnLoan
	- **CurrentResidenceDuration**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'CurrentResidenceDuration' appears to represent numerical values, likely indicating the duration of residence. It does not directly or indirectly reveal personal identifiers, protected characteristics, or other sensitive information. The context of the dataset (german_credit_data) suggests it is used for credit risk analysis, and this feature alone does not pose a significant risk of bias or discrimination.
		- **recommendation**: None
		- **column**: CurrentResidenceDuration
	- **OwnsProperty**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'OwnsProperty' feature appears to represent numerical values, likely indicating ownership status or a derived metric. It does not directly or indirectly reveal personal or confidential information, nor does it relate to protected characteristics or other sensitive categories.
		- **recommendation**: None
		- **column**: OwnsProperty
	- **Age**
		- **is_sensitive**: True
		- **sensibility_level**: 4
		- **justification**: Age is a protected characteristic under many anti-discrimination laws (e.g., GDPR, ADEA). While the provided data appears to be normalized or transformed, it could still be used to infer age-related biases in credit decisions.
		- **recommendation**: Avoid using age directly in decision-making models. If necessary, anonymize or aggregate age data to reduce re-identification risk and ensure compliance with anti-discrimination laws.
		- **column**: Age
	- **InstallmentPlans**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'InstallmentPlans' feature contains numerical values representing financial installment plans. While financial data can be sensitive, these values appear to be anonymized or standardized (e.g., z-scores or similar transformations), and there is no direct link to personal identifiers or confidential information.
		- **recommendation**: No specific handling is required unless the data is combined with other features that could lead to re-identification. Ensure the data remains anonymized and avoid linking it to identifiable information.
		- **column**: InstallmentPlans
	- **Housing**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'Housing' feature contains numerical values that do not directly or indirectly reveal personal, confidential, or sensitive information. It lacks identifiers or protected characteristics, and its context within the dataset does not suggest any bias or discrimination risk.
		- **recommendation**: None
		- **column**: Housing
	- **ExistingCreditsCount**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'ExistingCreditsCount' represents numerical values related to credit counts, which do not directly or indirectly reveal personal or confidential information. It is unlikely to contribute to discrimination or bias in downstream applications.
		- **recommendation**: None
		- **column**: ExistingCreditsCount
	- **Job**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'Job' feature appears to contain numerical values that do not directly correspond to personal identifiers, protected characteristics, or other sensitive categories. Given the context of the dataset (german_credit_data), it is likely a derived or encoded feature related to employment status or job type, which is generally non-sensitive.
		- **recommendation**: No specific handling is required unless further analysis reveals that the numerical values can be reverse-engineered to reveal sensitive information.
		- **column**: Job
	- **Dependents**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'Dependents' feature represents numerical values that do not directly reveal personal or confidential information. It is unlikely to be used for re-identification or to introduce bias.
		- **recommendation**: None
		- **column**: Dependents
	- **Telephone**
		- **is_sensitive**: True
		- **sensibility_level**: 8
		- **justification**: The 'Telephone' feature, despite being represented numerically, could indirectly map to personal phone numbers or identifiers, posing a re-identification risk. In the context of credit data, such identifiers can link sensitive financial behavior to individuals.
		- **recommendation**: Anonymize or remove this feature to prevent re-identification. If retention is necessary, ensure it is encrypted or hashed, and access is strictly controlled.
		- **column**: Telephone
	- **Risk**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'Risk' feature appears to be a numerical representation of risk scores, likely derived from financial or credit data. While it could indirectly relate to financial risk, it does not directly reveal personal identifiers, protected characteristics, or other sensitive information. The values are abstract and not tied to specific individuals.
		- **recommendation**: No specific handling is required unless the risk scores can be reverse-engineered to reveal sensitive attributes. In such cases, consider aggregating or anonymizing the data further.
		- **column**: Risk

---

### Fairness Analysis CreditHistory
_Analyze and mitigate bias for feature CreditHistory_

#### Parameters

#### Metrics
- **Duration**: 12.71 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
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

### Fairness Analysis ExistingSavings
_Analyze and mitigate bias for feature ExistingSavings_

#### Parameters

#### Metrics
- **Duration**: 11.43 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
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

### Fairness Analysis Sex
_Analyze and mitigate bias for feature Sex_

#### Parameters

#### Metrics
- **Duration**: 15.86 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
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

### Fairness Analysis Age
_Analyze and mitigate bias for feature Age_

#### Parameters

#### Metrics
- **Duration**: 13.23 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
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

### Fairness Analysis Telephone
_Analyze and mitigate bias for feature Telephone_

#### Parameters

#### Metrics
- **Duration**: 12.65 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
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
- **Duration**: 65.87 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **CreditHistory**: 
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
	- **ExistingSavings**: 
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
	- **Sex**: 
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
	- **Age**: 
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
	- **Telephone**: 
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

### dimensionality_reduction
_Reduce data dimensionality_

#### Parameters
- **enabled**: True
- **method**: pca
- **n_components**: None
- **target_explained_variance**: 0.95

#### Metrics
- **Duration**: 18.69 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 18 columns
- **Success**: True

#### Changes Made
- **added_columns**: 
	- component_7
	- component_9
	- component_10
	- component_6
	- component_15
	- component_3
	- component_13
	- component_2
	- component_4
	- component_5
	- component_16
	- component_12
	- component_18
	- component_1
	- component_8
	- component_11
	- component_14
	- component_17
- **removed_columns**: 
	- ExistingSavings
	- Telephone
	- Age
	- InstallmentPlans
	- ForeignWorker
	- Risk
	- Sex
	- CreditHistory
	- CheckingStatus
	- Housing
	- ExistingCreditsCount
	- InstallmentPercent
	- LoanAmount
	- Dependents
	- CurrentResidenceDuration
	- OthersOnLoan
	- LoanPurpose
	- Job
	- LoanDuration
	- OwnsProperty
	- EmploymentDuration
- **explained_variance_ratio**: 
	- 0.297266444210552
	- 0.06291740545664798
	- 0.05418355267844598
	- 0.048941012604277224
	- 0.04868745897249908
	- 0.04697487139291733
	- 0.04563535810783587
	- 0.04469220081111227
	- 0.04235915111981569
	- 0.03910363555853766
	- 0.03679103469153724
	- 0.03408748945933974
	- 0.030802085243984895
	- 0.0305368114459371
	- 0.02840503112216329
	- 0.0248805983581969
	- 0.02146075458144305
	- 0.019030834613292132
- **n_components**: 18
- **total_variance_explained**: 0.9567557304285355

---
