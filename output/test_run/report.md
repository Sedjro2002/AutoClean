# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-04-16T21:10:38.114581
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 271.82 ms
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
- **Duration**: 395.31 ms
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
- **Duration**: 259.06 ms
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
- **Duration**: 1.62 seconds
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **Age**: 
		- **before**: int64
		- **after**: float64
	- **LoanAmount**: 
		- **before**: int64
		- **after**: float64
	- **InstallmentPercent**: 
		- **before**: int64
		- **after**: float64
	- **ForeignWorker**: 
		- **before**: object
		- **after**: bool
	- **Risk**: 
		- **before**: object
		- **after**: bool
	- **Dependents**: 
		- **before**: int64
		- **after**: bool
	- **Telephone**: 
		- **before**: object
		- **after**: bool
	- **CurrentResidenceDuration**: 
		- **before**: int64
		- **after**: float64
	- **LoanDuration**: 
		- **before**: int64
		- **after**: float64
	- **ExistingCreditsCount**: 
		- **before**: int64
		- **after**: float64
	- **Sex**: 
		- **before**: object
		- **after**: bool
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
- **Duration**: 243.73 ms
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
- **Duration**: 194.27 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **InstallmentPlans**: 
		- **before**: object
		- **after**: int64
	- **CreditHistory**: 
		- **before**: object
		- **after**: int64
	- **ExistingSavings**: 
		- **before**: object
		- **after**: int64
	- **EmploymentDuration**: 
		- **before**: object
		- **after**: int64
	- **OthersOnLoan**: 
		- **before**: object
		- **after**: int64
	- **Housing**: 
		- **before**: object
		- **after**: int64
	- **LoanPurpose**: 
		- **before**: object
		- **after**: int64
	- **Job**: 
		- **before**: object
		- **after**: int64
	- **CheckingStatus**: 
		- **before**: object
		- **after**: int64
	- **OwnsProperty**: 
		- **before**: object
		- **after**: int64

---

### value_rounding
_Round numerical values to appropriate precision_

#### Parameters

#### Metrics
- **Duration**: 536.52 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **InstallmentPlans**: 
		- **before**: int64
		- **after**: Int64
	- **Age**: 
		- **before**: float64
		- **after**: Int64
	- **CreditHistory**: 
		- **before**: int64
		- **after**: Int64
	- **ExistingSavings**: 
		- **before**: int64
		- **after**: Int64
	- **LoanAmount**: 
		- **before**: float64
		- **after**: Int64
	- **InstallmentPercent**: 
		- **before**: float64
		- **after**: Int64
	- **EmploymentDuration**: 
		- **before**: int64
		- **after**: Int64
	- **OthersOnLoan**: 
		- **before**: int64
		- **after**: Int64
	- **Housing**: 
		- **before**: int64
		- **after**: Int64
	- **LoanPurpose**: 
		- **before**: int64
		- **after**: Int64
	- **CurrentResidenceDuration**: 
		- **before**: float64
		- **after**: Int64
	- **Job**: 
		- **before**: int64
		- **after**: Int64
	- **LoanDuration**: 
		- **before**: float64
		- **after**: Int64
	- **ExistingCreditsCount**: 
		- **before**: float64
		- **after**: Int64
	- **CheckingStatus**: 
		- **before**: int64
		- **after**: Int64
	- **OwnsProperty**: 
		- **before**: int64
		- **after**: Int64

---

### Fairness Analysis Sex
_Analyze and mitigate bias for feature Sex_

#### Parameters

#### Metrics
- **Duration**: 49.02 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: 0.9116111823077889
		- **statistical_parity_difference**: -0.062180505469520586
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.6413078666235027
			- **group_1_positive_rate**: 0.7034883720930233
		- **is_biased**: True
		- **bias_reasons**: 
			- Statistical Parity Difference de 0.0622 > 0.05
	- **mitigated**: 
		- **disparate_impact**: 1.0000000000000004
		- **statistical_parity_difference**: 2.220446049250313e-16
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.6413078666235027
			- **group_1_positive_rate**: 0.7034883720930233
		- **is_biased**: False
		- **bias_reasons**: 
	- **method**: Reweighing

---

### Fairness Analysis
_Analyze and mitigate bias for each sensitive feature_

#### Parameters

#### Metrics
- **Duration**: 50.09 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **Sex**: 
		- **original**: 
			- **disparate_impact**: 0.9116111823077889
			- **statistical_parity_difference**: -0.062180505469520586
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.6413078666235027
				- **group_1_positive_rate**: 0.7034883720930233
			- **is_biased**: True
			- **bias_reasons**: 
				- Statistical Parity Difference de 0.0622 > 0.05
		- **mitigated**: 
			- **disparate_impact**: 1.0000000000000004
			- **statistical_parity_difference**: 2.220446049250313e-16
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.6413078666235027
				- **group_1_positive_rate**: 0.7034883720930233
			- **is_biased**: False
			- **bias_reasons**: 
		- **method**: Reweighing

---

### Code Bias Analysis
_Completed ai code bias analysis_

#### Parameters
- **paths**: 
	- C:/Users/habib/Documents/AutoClean/preprocessing
- **analysis_type**: ai

#### Metrics
- **Duration**: 1 minutes 27.56 seconds
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
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
	def remove_outliers_by_income(self, threshold: float = 100000) -> pd.DataFrame:
	        """Remove records where income is above a threshold.
	        
	        Note: This could introduce bias by disproportionately excluding certain demographics.
	        """
	        return self.df[self.df['income'] <= threshold]
						```
					- **issue_type**: Data filtering
					- **explanation**: Removing records based on income thresholds could disproportionately exclude high-income groups, which may correlate with certain demographics (e.g., race, gender, or geographic location). This could introduce bias in the dataset.
				- value:
					- **code_snippet**:
						```python
	def encode_gender(self) -> pd.DataFrame:
	        """Encode gender column to numeric values.
	        
	        Note: Binary encoding of gender may reinforce gender binary assumptions
	        and exclude non-binary individuals.
	        """
	        gender_map = {'M': 1, 'F': 0}
	        self.df['gender'] = self.df['gender'].map(gender_map)
	        return self.df
						```
					- **issue_type**: Feature engineering
					- **explanation**: Binary encoding of gender reinforces a gender binary and excludes non-binary individuals, which could lead to discrimination or underrepresentation of certain groups.
				- value:
					- **code_snippet**:
						```python
	def reduce_females(self, ratio: float = 0.5) -> pd.DataFrame:
	        """Reduce the number of females in the dataset.
	        
	        """
	        num_females = int(self.df[self.df['gender'] == 0].shape[0] * ratio)
	        return self.df[self.df['gender'] == 0].sample(num_females, random_state=42)
						```
					- **issue_type**: Sampling bias
					- **explanation**: Artificially reducing the number of females in the dataset introduces sampling bias and could lead to underrepresentation of women in the analysis or model outcomes.
				- value:
					- **code_snippet**:
						```python
	def filter_by_age(self, min_age: int = 18, max_age: int = 65) -> pd.DataFrame:
	        """Filter dataset by age range.
	        
	        Note: Age filtering could introduce age-based discrimination.
	        """
	        return self.df[(self.df['age'] >= min_age) & (self.df['age'] <= max_age)]
						```
					- **issue_type**: Data filtering
					- **explanation**: Filtering by age range could introduce age-based discrimination, excluding younger or older individuals who might be relevant to the analysis.
				- value:
					- **code_snippet**:
						```python
	def normalize_education(self) -> pd.DataFrame:
	        """Normalize education levels.
	        
	        Note: Simplification of education levels might disadvantage those with
	        non-traditional education paths.
	        """
	        edu_map = {
	            'Some High School': 0,
	            'High School': 1,
	            'Some College': 2,
	            'Bachelors': 3,
	            'Masters': 4,
	            'PhD': 5
	        }
	        self.df['education'] = self.df['education'].map(edu_map)
	        return self.df
						```
					- **issue_type**: Feature engineering
					- **explanation**: Simplifying education levels into a linear scale may disadvantage individuals with non-traditional education paths or those from underrepresented backgrounds.
			- **recommendations**: 
				- Consider using more nuanced methods for outlier detection (e.g., percentile-based thresholds) to avoid disproportionately excluding certain demographics.
				- Expand gender encoding to include non-binary or other gender identities, or consider removing gender as a feature if it is not critical to the analysis.
				- Avoid artificially reducing the representation of any demographic group (e.g., females) unless justified by domain-specific requirements.
				- If age filtering is necessary, ensure it is justified and does not exclude relevant groups. Consider using age as a continuous variable or in broader bins.
				- Use a more inclusive approach to education normalization, such as categorical encoding or additional features to capture non-traditional education paths.
			- **severity**: high
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\preprocessing\feature_engineering.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 7
			- **problematic_sections**: 
				- value:
					- **code_snippet**:
						```python
	self.df['wealth_score'] = (0.6 * self.df['income'] + 0.4 * self.df['assets'])
						```
					- **issue_type**: Socioeconomic Bias
					- **explanation**: The wealth score is a composite of income and assets, which may amplify existing socioeconomic disparities. This could disadvantage individuals from lower-income backgrounds or those with fewer assets.
				- value:
					- **code_snippet**:
						```python
	self.df['high_income_area'] = self.df['neighborhood'].isin(high_income_areas).astype(int)
						```
					- **issue_type**: Residential Segregation Bias
					- **explanation**: Labeling neighborhoods as high-income areas based on income thresholds could reinforce residential segregation patterns and socioeconomic biases.
				- value:
					- **code_snippet**:
						```python
	self.df['good_credit'] = (self.df['credit_score'] > 700).astype(int)
						```
					- **issue_type**: Credit Scoring Bias
					- **explanation**: Binary classification of credit scores may perpetuate historical disadvantages faced by certain demographic groups, as credit scoring systems can be biased.
				- value:
					- **code_snippet**:
						```python
	weights = {'degree_level': 0.5, 'years_education': 0.3, 'test_scores': 0.2}
	self.df['education_score'] = (weights['degree_level'] * self.df['degree_level'] + weights['years_education'] * self.df['years_education'] + weights['test_scores'] * self.df['test_scores'])
						```
					- **issue_type**: Educational Bias
					- **explanation**: The education score may disadvantage individuals from non-traditional educational backgrounds or different cultural contexts, as it heavily weights formal education metrics.
			- **recommendations**: 
				- Consider alternative metrics for wealth assessment that account for socioeconomic diversity.
				- Avoid labeling neighborhoods based on income thresholds; instead, use more nuanced features.
				- Review credit scoring thresholds for potential biases and consider alternative creditworthiness indicators.
				- Include non-traditional educational achievements in the education score or use contextualized scoring methods.
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
					- **explanation**: Focusing on high-income customers could exclude lower-income groups, amplifying socioeconomic biases in the dataset.
				- value:
					- **code_snippet**:
						```python
	male = self.df[self.df['gender'] == 'M']
	female = self.df[self.df['gender'] == 'F']
						```
					- **issue_type**: Gender Binary Reinforcement
					- **explanation**: This approach reinforces a gender binary (M/F) and may exclude non-binary or other gender identities, leading to underrepresentation.
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
					- **issue_type**: Stratification Oversimplification
					- **explanation**: Stratifying only on education level may ignore other important demographic factors (e.g., race, gender) and their intersections, potentially introducing biases.
				- value:
					- **code_snippet**:
						```python
	age_group = self.df[
	    (self.df['age'] >= min_age) &
	    (self.df['age'] < max_age)
	]
						```
					- **issue_type**: Age-Based Sampling Bias
					- **explanation**: Sampling by age groups could introduce age-based biases and overlook intersectional factors (e.g., age combined with income or education).
			- **recommendations**: 
				- Include a broader income range or use stratified sampling to ensure representation of all socioeconomic groups.
				- Expand gender categories to include non-binary and other identities, or avoid gender-based sampling if not critical.
				- Stratify on multiple demographic factors (e.g., education, race, gender) to capture intersectional effects.
				- Consider intersectional sampling methods to account for multiple demographic factors simultaneously.
			- **severity**: medium

---

### normalization
_Normalize numerical features_

#### Parameters
- **enabled**: True
- **method**: standard
- **exclude_features**: 

#### Metrics
- **Duration**: 283.28 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **InstallmentPlans**: 
		- **before**: Int64
		- **after**: float64
	- **Age**: 
		- **before**: Int64
		- **after**: float64
	- **CreditHistory**: 
		- **before**: Int64
		- **after**: float64
	- **ExistingSavings**: 
		- **before**: Int64
		- **after**: float64
	- **LoanAmount**: 
		- **before**: Int64
		- **after**: float64
	- **InstallmentPercent**: 
		- **before**: Int64
		- **after**: float64
	- **EmploymentDuration**: 
		- **before**: Int64
		- **after**: float64
	- **OthersOnLoan**: 
		- **before**: Int64
		- **after**: float64
	- **ForeignWorker**: 
		- **before**: bool
		- **after**: float64
	- **Risk**: 
		- **before**: bool
		- **after**: float64
	- **Housing**: 
		- **before**: Int64
		- **after**: float64
	- **Dependents**: 
		- **before**: bool
		- **after**: float64
	- **Telephone**: 
		- **before**: bool
		- **after**: float64
	- **LoanPurpose**: 
		- **before**: Int64
		- **after**: float64
	- **CurrentResidenceDuration**: 
		- **before**: Int64
		- **after**: float64
	- **Job**: 
		- **before**: Int64
		- **after**: float64
	- **LoanDuration**: 
		- **before**: Int64
		- **after**: float64
	- **ExistingCreditsCount**: 
		- **before**: Int64
		- **after**: float64
	- **CheckingStatus**: 
		- **before**: Int64
		- **after**: float64
	- **Sex**: 
		- **before**: bool
		- **after**: float64
	- **OwnsProperty**: 
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

### dimensionality_reduction
_Reduce data dimensionality_

#### Parameters
- **enabled**: True
- **method**: pca
- **n_components**: None
- **target_explained_variance**: 0.95

#### Metrics
- **Duration**: 34.40 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 18 columns
- **Success**: True

#### Changes Made
- **added_columns**: 
	- component_14
	- component_11
	- component_8
	- component_12
	- component_7
	- component_4
	- component_17
	- component_6
	- component_13
	- component_2
	- component_10
	- component_16
	- component_5
	- component_15
	- component_18
	- component_1
	- component_3
	- component_9
- **removed_columns**: 
	- InstallmentPlans
	- Age
	- CreditHistory
	- ExistingSavings
	- LoanAmount
	- InstallmentPercent
	- EmploymentDuration
	- OthersOnLoan
	- ForeignWorker
	- Risk
	- Housing
	- Dependents
	- Telephone
	- LoanPurpose
	- CurrentResidenceDuration
	- Job
	- LoanDuration
	- ExistingCreditsCount
	- CheckingStatus
	- Sex
	- OwnsProperty
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
