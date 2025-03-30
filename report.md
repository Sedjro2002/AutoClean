# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-03-30T16:08:06.724833
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 311.86 ms
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
- **Duration**: 402.88 ms
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
- **method**: winz
- **outlier_param**: 1.5

#### Metrics
- **Duration**: 322.08 ms
- **Input Shape**: 4982 rows x 21 columns
- **Output Shape**: 4982 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **ExistingCreditsCount**: 
		- **before**: int64
		- **after**: Int64
- **statistics_changes**: 
	- **ExistingCreditsCount**: 
		- **mean_change**: -0.0002007226013647223
		- **std_change**: -0.0007217697952501823
		- **min_change**: 0.0
		- **max_change**: -1.0

---

### field_assignments
_Assign field types_

#### Parameters

#### Metrics
- **Duration**: 2.32 seconds
- **Input Shape**: 4982 rows x 21 columns
- **Output Shape**: 4982 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **Telephone**: 
		- **before**: object
		- **after**: bool
	- **LoanDuration**: 
		- **before**: int64
		- **after**: float64
	- **ForeignWorker**: 
		- **before**: object
		- **after**: bool
	- **Dependents**: 
		- **before**: int64
		- **after**: bool
	- **LoanAmount**: 
		- **before**: int64
		- **after**: float64
	- **Age**: 
		- **before**: int64
		- **after**: float64
	- **ExistingCreditsCount**: 
		- **before**: Int64
		- **after**: float64
	- **Risk**: 
		- **before**: object
		- **after**: bool
	- **Sex**: 
		- **before**: object
		- **after**: bool
	- **InstallmentPercent**: 
		- **before**: int64
		- **after**: float64
	- **CurrentResidenceDuration**: 
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
- **Duration**: 369.03 ms
- **Input Shape**: 4982 rows x 21 columns
- **Output Shape**: 4982 rows x 21 columns
- **Success**: True

#### Changes Made

---

### categorical_encoding
_Encode categorical features_

#### Parameters
- **method**: 
	- auto

#### Metrics
- **Duration**: 40.36 seconds
- **Input Shape**: 4982 rows x 21 columns
- **Output Shape**: 4982 rows x 36 columns
- **Success**: True

#### Changes Made
- **added_columns**: 
	- Job_unemployed
	- Job_management_self-employed
	- Housing_free
	- InstallmentPlans_none
	- Job_unskilled
	- Housing_rent
	- OthersOnLoan_none
	- OwnsProperty_unknown
	- Housing_own
	- CheckingStatus_0_to_200
	- CheckingStatus_less_0
	- OwnsProperty_real_estate
	- InstallmentPlans_bank
	- OthersOnLoan_guarantor
	- Job_skilled
	- OwnsProperty_car_other
	- InstallmentPlans_stores
	- OwnsProperty_savings_insurance
	- CheckingStatus_greater_200
	- CheckingStatus_no_checking
	- OthersOnLoan_co-applicant
- **removed_columns**: 
	- Job
	- Housing
	- CheckingStatus
	- InstallmentPlans
	- OthersOnLoan
	- OwnsProperty
- **dtype_changes**: 
	- **ExistingSavings**: 
		- **before**: object
		- **after**: int64
	- **CreditHistory**: 
		- **before**: object
		- **after**: int64
	- **LoanPurpose**: 
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
- **Duration**: 623.82 ms
- **Input Shape**: 4982 rows x 36 columns
- **Output Shape**: 4982 rows x 36 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **Job_unemployed**: 
		- **before**: float64
		- **after**: Int64
	- **Job_management_self-employed**: 
		- **before**: float64
		- **after**: Int64
	- **Housing_free**: 
		- **before**: float64
		- **after**: Int64
	- **CreditHistory**: 
		- **before**: int64
		- **after**: Int64
	- **LoanDuration**: 
		- **before**: float64
		- **after**: Int64
	- **InstallmentPlans_none**: 
		- **before**: float64
		- **after**: Int64
	- **Job_unskilled**: 
		- **before**: float64
		- **after**: Int64
	- **Housing_rent**: 
		- **before**: float64
		- **after**: Int64
	- **OthersOnLoan_none**: 
		- **before**: float64
		- **after**: Int64
	- **OwnsProperty_unknown**: 
		- **before**: float64
		- **after**: Int64
	- **Housing_own**: 
		- **before**: float64
		- **after**: Int64
	- **CheckingStatus_0_to_200**: 
		- **before**: float64
		- **after**: Int64
	- **LoanAmount**: 
		- **before**: float64
		- **after**: Int64
	- **Age**: 
		- **before**: float64
		- **after**: Int64
	- **CheckingStatus_less_0**: 
		- **before**: float64
		- **after**: Int64
	- **CheckingStatus_greater_200**: 
		- **before**: float64
		- **after**: Int64
	- **ExistingCreditsCount**: 
		- **before**: float64
		- **after**: Int64
	- **OwnsProperty_real_estate**: 
		- **before**: float64
		- **after**: Int64
	- **InstallmentPlans_bank**: 
		- **before**: float64
		- **after**: Int64
	- **OthersOnLoan_guarantor**: 
		- **before**: float64
		- **after**: Int64
	- **InstallmentPercent**: 
		- **before**: float64
		- **after**: Int64
	- **Job_skilled**: 
		- **before**: float64
		- **after**: Int64
	- **ExistingSavings**: 
		- **before**: int64
		- **after**: Int64
	- **OwnsProperty_car_other**: 
		- **before**: float64
		- **after**: Int64
	- **CurrentResidenceDuration**: 
		- **before**: float64
		- **after**: Int64
	- **InstallmentPlans_stores**: 
		- **before**: float64
		- **after**: Int64
	- **OwnsProperty_savings_insurance**: 
		- **before**: float64
		- **after**: Int64
	- **LoanPurpose**: 
		- **before**: int64
		- **after**: Int64
	- **EmploymentDuration**: 
		- **before**: int64
		- **after**: Int64
	- **CheckingStatus_no_checking**: 
		- **before**: float64
		- **after**: Int64
	- **OthersOnLoan_co-applicant**: 
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
- **Duration**: 527.87 ms
- **Input Shape**: 4982 rows x 36 columns
- **Output Shape**: 4982 rows x 36 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **Job_unemployed**: 
		- **before**: Int64
		- **after**: float64
	- **Telephone**: 
		- **before**: bool
		- **after**: float64
	- **Job_management_self-employed**: 
		- **before**: Int64
		- **after**: float64
	- **Housing_free**: 
		- **before**: Int64
		- **after**: float64
	- **CreditHistory**: 
		- **before**: Int64
		- **after**: float64
	- **LoanDuration**: 
		- **before**: Int64
		- **after**: float64
	- **InstallmentPlans_none**: 
		- **before**: Int64
		- **after**: float64
	- **ForeignWorker**: 
		- **before**: bool
		- **after**: float64
	- **Job_unskilled**: 
		- **before**: Int64
		- **after**: float64
	- **Housing_rent**: 
		- **before**: Int64
		- **after**: float64
	- **Dependents**: 
		- **before**: bool
		- **after**: float64
	- **OthersOnLoan_none**: 
		- **before**: Int64
		- **after**: float64
	- **OwnsProperty_unknown**: 
		- **before**: Int64
		- **after**: float64
	- **Housing_own**: 
		- **before**: Int64
		- **after**: float64
	- **CheckingStatus_0_to_200**: 
		- **before**: Int64
		- **after**: float64
	- **LoanAmount**: 
		- **before**: Int64
		- **after**: float64
	- **Age**: 
		- **before**: Int64
		- **after**: float64
	- **CheckingStatus_less_0**: 
		- **before**: Int64
		- **after**: float64
	- **CheckingStatus_greater_200**: 
		- **before**: Int64
		- **after**: float64
	- **ExistingCreditsCount**: 
		- **before**: Int64
		- **after**: float64
	- **Risk**: 
		- **before**: bool
		- **after**: float64
	- **OwnsProperty_real_estate**: 
		- **before**: Int64
		- **after**: float64
	- **InstallmentPlans_bank**: 
		- **before**: Int64
		- **after**: float64
	- **Sex**: 
		- **before**: bool
		- **after**: float64
	- **OthersOnLoan_guarantor**: 
		- **before**: Int64
		- **after**: float64
	- **InstallmentPercent**: 
		- **before**: Int64
		- **after**: float64
	- **Job_skilled**: 
		- **before**: Int64
		- **after**: float64
	- **ExistingSavings**: 
		- **before**: Int64
		- **after**: float64
	- **OwnsProperty_car_other**: 
		- **before**: Int64
		- **after**: float64
	- **CurrentResidenceDuration**: 
		- **before**: Int64
		- **after**: float64
	- **InstallmentPlans_stores**: 
		- **before**: Int64
		- **after**: float64
	- **OwnsProperty_savings_insurance**: 
		- **before**: Int64
		- **after**: float64
	- **LoanPurpose**: 
		- **before**: Int64
		- **after**: float64
	- **EmploymentDuration**: 
		- **before**: Int64
		- **after**: float64
	- **CheckingStatus_no_checking**: 
		- **before**: Int64
		- **after**: float64
	- **OthersOnLoan_co-applicant**: 
		- **before**: Int64
		- **after**: float64
- **statistics_changes**: 
	- **LoanDuration**: 
		- **mean_change**: -21.45584102769972
		- **std_change**: -10.133731552272971
		- **min_change**: -5.567977071524666
		- **max_change**: -60.178455928304366
	- **CreditHistory**: 
		- **mean_change**: -2.2637494981934965
		- **std_change**: -0.5414953546367496
		- **min_change**: -1.4685930167343184
		- **max_change**: -2.8736185853208145
	- **LoanPurpose**: 
		- **mean_change**: -4.237254114813328
		- **std_change**: -1.7848927360530698
		- **min_change**: -1.5216121778580167
		- **max_change**: -7.930578606049092
	- **LoanAmount**: 
		- **mean_change**: -3491.8155359293455
		- **std_change**: -2484.1225865786073
		- **min_change**: -251.30462007158008
		- **max_change**: -11672.706397633363
	- **ExistingSavings**: 
		- **mean_change**: -1.8482537133681252
		- **std_change**: -0.3315883492056504
		- **min_change**: -1.3880415136704864
		- **max_change**: -2.3840350753097725
	- **EmploymentDuration**: 
		- **mean_change**: -1.4221196306704138
		- **std_change**: -0.23799551356789617
		- **min_change**: -1.1487497773370476
		- **max_change**: -1.9176579547862103
	- **InstallmentPercent**: 
		- **mean_change**: -2.9895624247290247
		- **std_change**: -0.12270060371463698
		- **min_change**: -2.772141425849313
		- **max_change**: -3.318545489821631
	- **CurrentResidenceDuration**: 
		- **mean_change**: -2.8590927338418304
		- **std_change**: -0.1142313576975924
		- **min_change**: -2.6685151162688983
		- **max_change**: -3.181070552863774
	- **Age**: 
		- **mean_change**: -35.99357687675632
		- **std_change**: -9.618809720593202
		- **min_change**: -20.60047335138662
		- **max_change**: -70.42051418418708
	- **ExistingCreditsCount**: 
		- **mean_change**: -1.4672822159775194
		- **std_change**: 0.4350813173688486
		- **min_change**: -1.8271032854736553
		- **max_change**: -0.2870443780597811
	- **CheckingStatus_0_to_200**: 
		- **mean_change**: -0.2617422721798475
		- **std_change**: 0.5604732057291084
		- **min_change**: -0.5954330450582691
		- **max_change**: 0.6794499537763141
	- **CheckingStatus_greater_200**: 
		- **mean_change**: -0.06122039341629859
		- **std_change**: 0.7603421749184954
		- **min_change**: -0.2553678586107898
		- **max_change**: 2.9159195892546363
	- **CheckingStatus_less_0**: 
		- **mean_change**: -0.27699718988358096
		- **std_change**: 0.5525403766183503
		- **min_change**: -0.618967275885757
		- **max_change**: 0.6155942954641278
	- **CheckingStatus_no_checking**: 
		- **mean_change**: -0.400040144520273
		- **std_change**: 0.5101450600820121
		- **min_change**: -0.8165648698569573
		- **max_change**: 0.2246424465641974
	- **OthersOnLoan_co-applicant**: 
		- **mean_change**: -0.1439181051786431
		- **std_change**: 0.6490584710632132
		- **min_change**: -0.41001529722985375
		- **max_change**: 1.4389333928665637
	- **OthersOnLoan_guarantor**: 
		- **mean_change**: -0.022079486150140475
		- **std_change**: 0.8531435211430587
		- **min_change**: -0.1502597641284178
		- **max_change**: 5.655141553033196
	- **OthersOnLoan_none**: 
		- **mean_change**: -0.8340024086712163
		- **std_change**: 0.62798455425747
		- **min_change**: -2.241469115748889
		- **max_change**: -0.5538640291878865
	- **OwnsProperty_car_other**: 
		- **mean_change**: -0.3089120835006022
		- **std_change**: 0.5380091861502194
		- **min_change**: -0.6685760245985658
		- **max_change**: 0.4957162135756088
	- **OwnsProperty_real_estate**: 
		- **mean_change**: -0.21517462866318748
		- **std_change**: 0.5891156910783748
		- **min_change**: -0.5236113042648757
		- **max_change**: 0.9098136191004327
	- **OwnsProperty_savings_insurance**: 
		- **mean_change**: -0.33299879566439183
		- **std_change**: 0.5287669601150486
		- **min_change**: -0.7065746017018212
		- **max_change**: 0.4152787229988859
	- **OwnsProperty_unknown**: 
		- **mean_change**: -0.1429144921718185
		- **std_change**: 0.6500796176923105
		- **min_change**: -0.40834388777004715
		- **max_change**: 1.4489162932276707
	- **InstallmentPlans_bank**: 
		- **mean_change**: -0.09353673223604979
		- **std_change**: 0.7088880240545705
		- **min_change**: -0.3212299216032268
		- **max_change**: 2.1130350342492963
	- **InstallmentPlans_none**: 
		- **mean_change**: -0.7035327177840225
		- **std_change**: 0.5433550351118138
		- **min_change**: -1.540471839014775
		- **max_change**: -0.35084824358778244
	- **InstallmentPlans_stores**: 
		- **mean_change**: -0.20293054997992774
		- **std_change**: 0.597878776778132
		- **min_change**: -0.5045748900735872
		- **max_change**: 0.9818663585382936
	- **Housing_free**: 
		- **mean_change**: -0.14833400240867123
		- **std_change**: 0.6446339381632061
		- **min_change**: -0.4173358598198652
		- **max_change**: 1.396151628167372
	- **Housing_own**: 
		- **mean_change**: -0.6413087113608994
		- **std_change**: 0.5204358791283186
		- **min_change**: -1.3371285289208161
		- **max_change**: -0.25212873828435123
	- **Housing_rent**: 
		- **mean_change**: -0.21035728623042946
		- **std_change**: 0.5924970809113639
		- **min_change**: -0.5161351820812092
		- **max_change**: 0.9374769144155317
	- **Job_management_self-employed**: 
		- **mean_change**: -0.12906463267763948
		- **std_change**: 0.664795261009073
		- **min_change**: -0.38495561741528145
		- **max_change**: 1.5977020590434
	- **Job_skilled**: 
		- **mean_change**: -0.678643115214773
		- **std_change**: 0.5330560304531713
		- **min_change**: -1.4532051203456708
		- **max_change**: -0.3118658983515471
	- **Job_unemployed**: 
		- **mean_change**: -0.05740666399036525
		- **std_change**: 0.7674590163122188
		- **min_change**: -0.2467851212730859
		- **max_change**: 3.052108145099341
	- **Job_unskilled**: 
		- **mean_change**: -0.13488558811722198
		- **std_change**: 0.6584647612418539
		- **min_change**: -0.3948626005560231
		- **max_change**: 1.5325265005899698
- **feature_stats**: 
	- **mean**: 
		- **LoanDuration**: 21.45584102769972
		- **CreditHistory**: 2.2637494981934965
		- **LoanPurpose**: 4.237254114813328
		- **LoanAmount**: 3491.8155359293455
		- **ExistingSavings**: 1.8482537133681252
		- **EmploymentDuration**: 1.4221196306704136
		- **InstallmentPercent**: 2.9895624247290247
		- **Sex**: 0.3797671617824167
		- **CurrentResidenceDuration**: 2.8590927338418304
		- **Age**: 35.99357687675632
		- **ExistingCreditsCount**: 1.4672822159775192
		- **Dependents**: 0.834805299076676
		- **Telephone**: 0.5867121637896427
		- **ForeignWorker**: 0.9753111200321156
		- **Risk**: 0.6647932557205941
		- **CheckingStatus_0_to_200**: 0.26174227217984747
		- **CheckingStatus_greater_200**: 0.061220393416298674
		- **CheckingStatus_less_0**: 0.2769971898835809
		- **CheckingStatus_no_checking**: 0.400040144520273
		- **OthersOnLoan_co-applicant**: 0.14391810517864312
		- **OthersOnLoan_guarantor**: 0.022079486150140507
		- **OthersOnLoan_none**: 0.8340024086712163
		- **OwnsProperty_car_other**: 0.3089120835006022
		- **OwnsProperty_real_estate**: 0.21517462866318748
		- **OwnsProperty_savings_insurance**: 0.33299879566439183
		- **OwnsProperty_unknown**: 0.14291449217181854
		- **InstallmentPlans_bank**: 0.09353673223604977
		- **InstallmentPlans_none**: 0.7035327177840225
		- **InstallmentPlans_stores**: 0.20293054997992774
		- **Housing_free**: 0.14833400240867123
		- **Housing_own**: 0.6413087113608993
		- **Housing_rent**: 0.21035728623042954
		- **Job_management_self-employed**: 0.1290646326776395
		- **Job_skilled**: 0.6786431152147732
		- **Job_unemployed**: 0.057406663990365314
		- **Job_unskilled**: 0.134885588117222
	- **std**: 
		- **LoanDuration**: 11.132714466753043
		- **CreditHistory**: 1.5414410067312945
		- **LoanPurpose**: 2.78471359290653
		- **LoanAmount**: 2484.8732642929813
		- **ExistingSavings**: 1.331555068897522
		- **EmploymentDuration**: 1.2379716268298855
		- **InstallmentPercent**: 1.1226882887044474
		- **Sex**: 0.4853288211245489
		- **CurrentResidenceDuration**: 1.114219892714606
		- **Age**: 10.617844315891558
		- **ExistingCreditsCount**: 0.5649623501494396
		- **Dependents**: 0.3713561790386387
		- **Telephone**: 0.4924235987957098
		- **ForeignWorker**: 0.1551751886540364
		- **Risk**: 0.47206268955405367
		- **CheckingStatus_0_to_200**: 0.4395830469137522
		- **CheckingStatus_greater_200**: 0.2397341378407595
		- **CheckingStatus_less_0**: 0.44751507983550715
		- **CheckingStatus_no_checking**: 0.48990614130920235
		- **OthersOnLoan_co-applicant**: 0.3510066725582751
		- **OthersOnLoan_guarantor**: 0.146942105747421
		- **OthersOnLoan_none**: 0.37207847425217405
		- **OwnsProperty_car_other**: 0.462044811861273
		- **OwnsProperty_real_estate**: 0.41094343630583374
		- **OwnsProperty_savings_insurance**: 0.47128611028806744
		- **OwnsProperty_unknown**: 0.34998562841792485
		- **InstallmentPlans_bank**: 0.29118312444001854
		- **InstallmentPlans_none**: 0.4566994994429592
		- **InstallmentPlans_stores**: 0.40218123012489254
		- **Housing_free**: 0.3554307613841204
		- **Housing_own**: 0.4796163551147125
		- **Housing_rent**: 0.4075623858505575
		- **Job_management_self-employed**: 0.33527146205638425
		- **Job_skilled**: 0.4669974704282254
		- **Job_unemployed**: 0.23261801073834032
		- **Job_unskilled**: 0.3416013264545282

---

### Code Bias Analysis
_Completed ai code bias analysis_

#### Parameters
- **paths**: 
	- C:/Users/habib/Documents/AutoClean/preprocessing
- **analysis_type**: ai

#### Metrics
- **Duration**: 1 minutes 41.24 seconds
- **Input Shape**: 4982 rows x 36 columns
- **Output Shape**: 4982 rows x 36 columns
- **Success**: True

#### Changes Made
- **results**: 
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\preprocessing\data_cleaner.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 8
			- **problematic_sections**: 
				- value:
					- **code_snippet**:
						```python
						self.df[self.df['income'] <= threshold]
						```
					- **issue_type**: Data filtering bias
					- **explanation**: Removing records based on income thresholds could disproportionately exclude certain demographics, such as high-income earners in specific regions or industries, leading to biased model outcomes.
				- value:
					- **code_snippet**:
						```python
						gender_map = {'M': 1, 'F': 0}
						```
					- **issue_type**: Gender binary bias
					- **explanation**: Binary encoding of gender reinforces gender binary assumptions and excludes non-binary individuals, which could lead to discriminatory outcomes.
				- value:
					- **code_snippet**:
						```python
						self.df[self.df['gender'] == 0].sample(num_females, random_state=42)
						```
					- **issue_type**: Gender-based sampling bias
					- **explanation**: Reducing the number of females in the dataset artificially alters the gender distribution, which could lead to biased model performance, especially in gender-sensitive applications.
				- value:
					- **code_snippet**:
						```python
						self.df[(self.df['age'] >= min_age) & (self.df['age'] <= max_age)]
						```
					- **issue_type**: Age discrimination
					- **explanation**: Filtering by age range could introduce age-based discrimination, excluding younger or older individuals who might be relevant to the analysis.
				- value:
					- **code_snippet**:
						```python
						edu_map = {
						            'Some High School': 0,
						            'High School': 1,
						            'Some College': 2,
						            'Bachelors': 3,
						            'Masters': 4,
						            'PhD': 5
						        }
						```
					- **issue_type**: Education simplification bias
					- **explanation**: Simplifying education levels into a linear scale may disadvantage individuals with non-traditional education paths or those from underrepresented backgrounds.
			- **recommendations**: 
				- Consider using more nuanced income thresholds or analyzing the impact of income filtering on different demographic groups.
				- Expand gender encoding to include non-binary options or avoid using gender as a feature if not strictly necessary.
				- Avoid artificially altering gender distributions; instead, ensure the dataset is representative of the population.
				- Justify age filtering with domain-specific reasons or consider including all age groups with appropriate adjustments.
				- Use a more granular or non-linear representation of education levels to capture diverse educational backgrounds.
			- **severity**: high
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\preprocessing\feature_engineering.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 8
			- **problematic_sections**: 
				- value:
					- **code_snippet**:
						```python
						self.df['wealth_score'] = (0.6 * self.df['income'] + 0.4 * self.df['assets'])
						```
					- **issue_type**: Socioeconomic Bias
					- **explanation**: The wealth score is a composite of income and assets, which may amplify existing socioeconomic disparities. This could disproportionately favor individuals with higher incomes and assets, reinforcing systemic inequalities.
				- value:
					- **code_snippet**:
						```python
						self.df['high_income_area'] = self.df['neighborhood'].isin(high_income_areas).astype(int)
						```
					- **issue_type**: Residential Segregation Bias
					- **explanation**: Labeling neighborhoods as 'high-income' based on income thresholds may reinforce residential segregation patterns and socioeconomic biases, potentially disadvantaging residents of lower-income areas.
				- value:
					- **code_snippet**:
						```python
						self.df['good_credit'] = (self.df['credit_score'] > 700).astype(int)
						```
					- **issue_type**: Credit Scoring Bias
					- **explanation**: Binary classification of credit scores as 'good' or not may perpetuate historical disadvantages faced by certain demographic groups, as credit scoring systems can reflect systemic biases.
				- value:
					- **code_snippet**:
						```python
						self.df['education_score'] = (weights['degree_level'] * self.df['degree_level'] + weights['years_education'] * self.df['years_education'] + weights['test_scores'] * self.df['test_scores'])
						```
					- **issue_type**: Educational Bias
					- **explanation**: The education score may disadvantage individuals from non-traditional educational backgrounds or different cultural contexts, as it heavily weights formal education metrics.
			- **recommendations**: 
				- Consider alternative metrics for wealth assessment that account for systemic disparities, such as cost-of-living-adjusted income or wealth-to-needs ratios.
				- Avoid binary classifications based on income thresholds for neighborhoods; instead, use continuous or more nuanced measures.
				- Review credit scoring thresholds for fairness across demographic groups and consider alternative creditworthiness indicators.
				- Incorporate diverse educational pathways into the education score, such as vocational training or experiential learning, to reduce bias against non-traditional backgrounds.
			- **severity**: high
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\preprocessing\sampling.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 7
			- **problematic_sections**: 
				- value:
					- **code_snippet**:
						```python
						high_value = self.df[self.df['income'] >= income_threshold]
						```
					- **issue_type**: Representation Bias
					- **explanation**: Sampling based on income thresholds may exclude lower-income groups, leading to underrepresentation and potential biases in the model.
				- value:
					- **code_snippet**:
						```python
						male = self.df[self.df['gender'] == 'M']
						female = self.df[self.df['gender'] == 'F']
						```
					- **issue_type**: Gender Binary Reinforcement
					- **explanation**: The code assumes a binary gender classification (M/F), which excludes non-binary or other gender identities, reinforcing biases and underrepresentation.
				- value:
					- **code_snippet**:
						```python
						return train_test_split(
							self.df,
							test_size=test_size,
							stratify=self.df['education'],
							random_state=random_state
						)
						```
					- **issue_type**: Limited Stratification
					- **explanation**: Stratifying only on education level ignores other demographic factors (e.g., race, gender, age), potentially missing intersectional biases.
				- value:
					- **code_snippet**:
						```python
						age_group = self.df[
							(self.df['age'] >= min_age) &
							(self.df['age'] < max_age)
						]
						```
					- **issue_type**: Age-Based Sampling Bias
					- **explanation**: Sampling by age groups may introduce age-related biases and overlook intersectional factors (e.g., age combined with income or education).
			- **recommendations**: 
				- Include lower-income groups in sampling to avoid representation bias.
				- Expand gender categories beyond binary (M/F) to include non-binary and other identities.
				- Use multi-dimensional stratification (e.g., education, gender, race) to capture intersectional factors.
				- Consider intersectional sampling methods to account for overlapping demographic factors (e.g., age and income).
			- **severity**: medium

---

### Fairness Analysis Sex
_Analyze and mitigate bias for feature Sex_

#### Parameters

#### Metrics
- **Duration**: 59.02 ms
- **Input Shape**: 4982 rows x 36 columns
- **Output Shape**: 4982 rows x 36 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: 0.0
		- **statistical_parity_difference**: -1.0
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.0
			- **group_1_positive_rate**: 1.0
	- **mitigated**: 
		- **disparate_impact**: 0.0
		- **statistical_parity_difference**: -1.0
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.0
			- **group_1_positive_rate**: 1.0

---

### Fairness Analysis
_Analyze and mitigate bias for each sensitive feature_

#### Parameters

#### Metrics
- **Duration**: 59.02 ms
- **Input Shape**: 4982 rows x 36 columns
- **Output Shape**: 4982 rows x 36 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **Sex**: 
		- **original**: 
			- **disparate_impact**: 0.0
			- **statistical_parity_difference**: -1.0
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.0
				- **group_1_positive_rate**: 1.0
		- **mitigated**: 
			- **disparate_impact**: 0.0
			- **statistical_parity_difference**: -1.0
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.0
				- **group_1_positive_rate**: 1.0

---

### dimensionality_reduction
_Reduce data dimensionality_

#### Parameters
- **enabled**: True
- **method**: pca
- **n_components**: None
- **target_explained_variance**: 0.95

#### Metrics
- **Duration**: 39.78 ms
- **Input Shape**: 4982 rows x 36 columns
- **Output Shape**: 4982 rows x 24 columns
- **Success**: True

#### Changes Made
- **added_columns**: 
	- component_17
	- component_4
	- component_14
	- component_1
	- component_8
	- component_22
	- component_3
	- component_16
	- component_12
	- component_23
	- component_13
	- component_6
	- component_7
	- component_15
	- component_18
	- component_11
	- component_9
	- component_5
	- component_21
	- component_20
	- component_24
	- component_19
	- component_2
	- component_10
- **removed_columns**: 
	- Job_unemployed
	- Telephone
	- Job_management_self-employed
	- Housing_free
	- CreditHistory
	- LoanDuration
	- InstallmentPlans_none
	- ForeignWorker
	- Job_unskilled
	- Housing_rent
	- Dependents
	- OthersOnLoan_none
	- OwnsProperty_unknown
	- Housing_own
	- CheckingStatus_0_to_200
	- LoanAmount
	- Age
	- CheckingStatus_less_0
	- CheckingStatus_greater_200
	- ExistingCreditsCount
	- Risk
	- OwnsProperty_real_estate
	- InstallmentPlans_bank
	- Sex
	- OthersOnLoan_guarantor
	- InstallmentPercent
	- Job_skilled
	- ExistingSavings
	- OwnsProperty_car_other
	- CurrentResidenceDuration
	- InstallmentPlans_stores
	- OwnsProperty_savings_insurance
	- LoanPurpose
	- EmploymentDuration
	- CheckingStatus_no_checking
	- OthersOnLoan_co-applicant
- **explained_variance_ratio**: 
	- 0.22371148383606734
	- 0.0829330997153957
	- 0.06430091127634417
	- 0.053057639229927595
	- 0.045816842894677696
	- 0.04086498171220991
	- 0.03923992137211719
	- 0.035687131515676915
	- 0.033847834527506
	- 0.030944184079099685
	- 0.029866388934482787
	- 0.027919699654069405
	- 0.026647635350506835
	- 0.02639358587744411
	- 0.025606416174428267
	- 0.023063050930941062
	- 0.021564839899219687
	- 0.020606174628549884
	- 0.01904003180343813
	- 0.017319778643799685
	- 0.016964176839677055
	- 0.016303039848367108
	- 0.015262958796347
	- 0.013477665069227754
- **n_components**: 24
- **total_variance_explained**: 0.9504394726095209

---
