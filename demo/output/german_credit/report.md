# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-05-16T03:56:16.122873
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### Data Profiling
_Generate data profile reports_

#### Parameters
- **threshold**: 10000
- **sample_size**: 1000
- **output_prefix**: before_preprocessing

#### Metrics
- **Duration**: 14.00 seconds
- **Input Shape**: 5000 rows x 21 columns
- **Output Shape**: 5000 rows x 21 columns
- **Success**: True

#### Changes Made

---

### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 49.34 ms
- **Input Shape**: 5000 rows x 21 columns
- **Output Shape**: 4982 rows x 21 columns
- **Success**: True

#### Changes Made
- **row_count**: 
	- **before**: 5000
	- **after**: 4982
	- **difference**: 18
- **statistics_changes**: 
	- **LoanDuration**: 
		- **mean_change**: 0.06284102769971867
		- **std_change**: -0.02901147318032038
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **LoanAmount**: 
		- **mean_change**: 11.670535929345533
		- **std_change**: -3.1100957345688585
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **InstallmentPercent**: 
		- **mean_change**: 0.007162424729024508
		- **std_change**: -0.004294538834481054
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **CurrentResidenceDuration**: 
		- **mean_change**: 0.00489273384183031
		- **std_change**: -0.0013704296707364172
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **Age**: 
		- **mean_change**: 0.06117687675632055
		- **std_change**: -0.029625412711835608
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **ExistingCreditsCount**: 
		- **mean_change**: 0.001682938578883908
		- **std_change**: 0.0003256726389923026
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **Dependents**: 
		- **mean_change**: 0.0005947009233238099
		- **std_change**: 0.0005372196672418506
		- **min_change**: 0.0
		- **max_change**: 0.0

---

### missing_value_handling
_Handle missing values in the dataset_

#### Parameters
- **numerical_method**: knn
- **categorical_method**: knn

#### Metrics
- **Duration**: 41.74 ms
- **Input Shape**: 4982 rows x 21 columns
- **Output Shape**: 4982 rows x 21 columns
- **Success**: True

#### Changes Made

---

### outlier_handling
_Handle outliers in numerical features_

#### Parameters
- **method**: delete
- **outlier_param**: 1.5

#### Metrics
- **Duration**: 56.24 ms
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
- **Duration**: 678.65 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **ExistingCreditsCount**: 
		- **before**: int64
		- **after**: float64
	- **Sex**: 
		- **before**: object
		- **after**: bool
	- **LoanAmount**: 
		- **before**: int64
		- **after**: float64
	- **LoanDuration**: 
		- **before**: int64
		- **after**: float64
	- **ForeignWorker**: 
		- **before**: object
		- **after**: bool
	- **Dependents**: 
		- **before**: int64
		- **after**: bool
	- **InstallmentPercent**: 
		- **before**: int64
		- **after**: float64
	- **CurrentResidenceDuration**: 
		- **before**: int64
		- **after**: float64
	- **Age**: 
		- **before**: int64
		- **after**: float64
	- **Telephone**: 
		- **before**: object
		- **after**: bool
	- **Risk**: 
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
- **Duration**: 68.35 ms
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
- **Duration**: 63.73 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **CheckingStatus**: 
		- **before**: object
		- **after**: int64
	- **EmploymentDuration**: 
		- **before**: object
		- **after**: int64
	- **OthersOnLoan**: 
		- **before**: object
		- **after**: int64
	- **CreditHistory**: 
		- **before**: object
		- **after**: int64
	- **OwnsProperty**: 
		- **before**: object
		- **after**: int64
	- **ExistingSavings**: 
		- **before**: object
		- **after**: int64
	- **LoanPurpose**: 
		- **before**: object
		- **after**: int64
	- **Job**: 
		- **before**: object
		- **after**: int64
	- **Housing**: 
		- **before**: object
		- **after**: int64
	- **InstallmentPlans**: 
		- **before**: object
		- **after**: int64

---

### value_rounding
_Round numerical values to appropriate precision_

#### Parameters

#### Metrics
- **Duration**: 167.98 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **ExistingCreditsCount**: 
		- **before**: float64
		- **after**: Int64
	- **LoanAmount**: 
		- **before**: float64
		- **after**: Int64
	- **CheckingStatus**: 
		- **before**: int64
		- **after**: Int64
	- **LoanDuration**: 
		- **before**: float64
		- **after**: Int64
	- **EmploymentDuration**: 
		- **before**: int64
		- **after**: Int64
	- **OthersOnLoan**: 
		- **before**: int64
		- **after**: Int64
	- **CreditHistory**: 
		- **before**: int64
		- **after**: Int64
	- **InstallmentPercent**: 
		- **before**: float64
		- **after**: Int64
	- **CurrentResidenceDuration**: 
		- **before**: float64
		- **after**: Int64
	- **OwnsProperty**: 
		- **before**: int64
		- **after**: Int64
	- **ExistingSavings**: 
		- **before**: int64
		- **after**: Int64
	- **LoanPurpose**: 
		- **before**: int64
		- **after**: Int64
	- **Age**: 
		- **before**: float64
		- **after**: Int64
	- **Job**: 
		- **before**: int64
		- **after**: Int64
	- **Housing**: 
		- **before**: int64
		- **after**: Int64
	- **InstallmentPlans**: 
		- **before**: int64
		- **after**: Int64

---

### Sensitive Feature Detection
_Use AI to detect potentially sensitive features_

#### Parameters

#### Metrics
- **Duration**: 2 minutes 54.81 seconds
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **sensitive_features**: 
	- Sex
	- Telephone
- **results**: 
	- **CheckingStatus**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'CheckingStatus' contains numerical values (e.g., 3, 0) without clear context or labels, making it difficult to associate with personal or sensitive information. It appears to be a categorical or ordinal feature in the German credit dataset, likely representing some form of credit status.
		- **recommendation**: None
		- **column**: CheckingStatus
	- **LoanDuration**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'LoanDuration' feature represents numerical values indicating the duration of loans. It does not contain personal identifiers, protected characteristics, or other sensitive information. The data is generic and does not pose a risk of revealing confidential details or causing bias.
		- **recommendation**: None
		- **column**: LoanDuration
	- **CreditHistory**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'CreditHistory' feature contains numerical values representing credit history categories, which are not directly identifiable or linked to personal information. It does not reveal sensitive details about individuals.
		- **recommendation**: None
		- **column**: CreditHistory
	- **LoanPurpose**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'LoanPurpose' feature contains numerical values representing loan purposes, which are not directly or indirectly linked to personal or sensitive information. It does not reveal any protected characteristics or confidential data.
		- **recommendation**: None
		- **column**: LoanPurpose
	- **LoanAmount**
		- **is_sensitive**: False
		- **sensibility_level**: 5
		- **justification**: The 'LoanAmount' feature contains financial data, which is potentially sensitive as it could reveal personal financial status or creditworthiness. While not directly identifying, it could contribute to re-identification when combined with other features.
		- **recommendation**: Anonymize or aggregate the data to reduce granularity, and ensure compliance with financial data protection regulations (e.g., GDPR, CCPA).
		- **column**: LoanAmount
	- **ExistingSavings**
		- **is_sensitive**: False
		- **sensibility_level**: 5
		- **justification**: The 'ExistingSavings' feature represents financial data, which is potentially sensitive as it could reveal personal financial status. While the values are numerical and not directly identifiable, they could indirectly contribute to profiling or discrimination based on financial standing.
		- **recommendation**: Consider anonymizing or aggregating the data to reduce granularity. Ensure compliance with financial data protection regulations (e.g., GDPR, CCPA) if applicable.
		- **column**: ExistingSavings
	- **EmploymentDuration**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'EmploymentDuration' represents numerical values indicating the duration of employment. It does not directly or indirectly reveal personal or confidential information, nor does it pose a risk of discrimination or bias.
		- **recommendation**: None
		- **column**: EmploymentDuration
	- **InstallmentPercent**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'InstallmentPercent' contains numerical values representing percentages, which are non-sensitive and do not reveal personal or confidential information. It is unlikely to contribute to bias or discrimination.
		- **recommendation**: None
		- **column**: InstallmentPercent
	- **Sex**
		- **is_sensitive**: False
		- **sensibility_level**: 8
		- **justification**: The 'Sex' feature contains binary gender information, which is a protected characteristic under many privacy and anti-discrimination laws. It can lead to bias in credit risk assessment models if not handled carefully.
		- **recommendation**: Consider anonymizing or aggregating this feature to prevent direct discrimination. Ensure fairness-aware modeling techniques are applied to mitigate bias in downstream applications.
		- **column**: Sex
	- **OthersOnLoan**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'OthersOnLoan' contains numerical values (counts of other loans) and does not directly or indirectly reveal personal, confidential, or protected information. It is unlikely to contribute to bias or discrimination in downstream applications.
		- **recommendation**: None
		- **column**: OthersOnLoan
	- **CurrentResidenceDuration**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature represents the duration of current residence in years, which is non-sensitive public information. It does not reveal personal or confidential details and has no direct link to protected characteristics or other sensitive categories.
		- **recommendation**: None
		- **column**: CurrentResidenceDuration
	- **OwnsProperty**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'OwnsProperty' feature indicates whether an individual owns property (values 0 or 2). This is non-sensitive, public information and does not directly or indirectly reveal personal or confidential details. It also does not pose a risk of discrimination or bias.
		- **recommendation**: None
		- **column**: OwnsProperty
	- **Age**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: Age is a demographic attribute but does not directly reveal personal or confidential information. It is commonly used in datasets for analysis and modeling.
		- **recommendation**: None
		- **column**: Age
	- **InstallmentPlans**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'InstallmentPlans' contains binary values (1, 1, 1, 1, 1) indicating whether installment plans are available. This is non-sensitive, public information with no direct or indirect identifiers or potential for bias.
		- **recommendation**: None
		- **column**: InstallmentPlans
	- **Housing**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'Housing' feature contains numerical values (1, 2) without clear context indicating personal or sensitive information. It appears to represent categorical data (e.g., housing type or status) and does not directly or indirectly identify individuals or reveal protected characteristics.
		- **recommendation**: None
		- **column**: Housing
	- **ExistingCreditsCount**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The feature 'ExistingCreditsCount' represents the number of existing credits a person has, which is not directly identifiable or linked to personal or protected characteristics. It is a numerical attribute with low risk of revealing sensitive information or causing bias.
		- **recommendation**: None
		- **column**: ExistingCreditsCount
	- **Job**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'Job' feature consists of numerical values (1, 0, 3, etc.) without clear context indicating personal or sensitive information. It appears to represent job categories or classifications, which are generally non-sensitive unless tied to specific individuals or discriminatory practices.
		- **recommendation**: No specific handling is required unless further analysis reveals that these numerical values correlate with protected characteristics or discriminatory outcomes.
		- **column**: Job
	- **Dependents**
		- **is_sensitive**: False
		- **sensibility_level**: 4
		- **justification**: The 'Dependents' feature indicates whether an individual has dependents, which could indirectly reveal family status or personal responsibilities. While not directly identifying, it may contribute to bias in credit risk assessments if used improperly.
		- **recommendation**: Consider anonymizing or aggregating this feature to reduce potential bias. Ensure it is not used in a discriminatory manner in credit risk models.
		- **column**: Dependents
	- **Telephone**
		- **is_sensitive**: False
		- **sensibility_level**: 7
		- **justification**: Telephone numbers are direct personal identifiers and can reveal individual identities. Even partial or masked numbers may still pose re-identification risks when combined with other data.
		- **recommendation**: Anonymize or pseudonymize telephone numbers. If not required for analysis, consider removing this feature entirely to mitigate privacy risks.
		- **column**: Telephone
	- **ForeignWorker**
		- **is_sensitive**: False
		- **sensibility_level**: 5
		- **justification**: The 'ForeignWorker' feature indicates whether an individual is a foreign worker, which could indirectly reveal nationality or immigration status. While not directly identifying, it may contribute to bias or discrimination in credit risk assessments.
		- **recommendation**: Consider anonymizing or aggregating this feature to prevent potential bias. Ensure compliance with anti-discrimination laws and regulations when using this feature in credit risk models.
		- **column**: ForeignWorker

---

### Fairness Analysis Sex
_Analyze and mitigate bias for feature Sex_

#### Parameters

#### Metrics
- **Duration**: 22.15 ms
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

### Fairness Analysis Telephone
_Analyze and mitigate bias for feature Telephone_

#### Parameters

#### Metrics
- **Duration**: 15.38 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: 0.5797187679736617
		- **statistical_parity_difference**: -0.33818045081284553
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.46647230320699706
			- **group_1_positive_rate**: 0.8046527540198426
		- **is_biased**: True
		- **bias_reasons**: 
			- Disparate Impact de 0.5797 < 0.8 (sous-représentation du groupe non privilégié)
			- Statistical Parity Difference de 0.3382 > 0.05
	- **mitigated**: 
		- **disparate_impact**: 1.0
		- **statistical_parity_difference**: 0.0
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.46647230320699706
			- **group_1_positive_rate**: 0.8046527540198426
		- **is_biased**: False
		- **bias_reasons**: 
	- **method**: Reweighing

---

### Fairness Analysis
_Analyze and mitigate bias for each sensitive feature_

#### Parameters

#### Metrics
- **Duration**: 37.53 ms
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
	- **Telephone**: 
		- **original**: 
			- **disparate_impact**: 0.5797187679736617
			- **statistical_parity_difference**: -0.33818045081284553
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.46647230320699706
				- **group_1_positive_rate**: 0.8046527540198426
			- **is_biased**: True
			- **bias_reasons**: 
				- Disparate Impact de 0.5797 < 0.8 (sous-représentation du groupe non privilégié)
				- Statistical Parity Difference de 0.3382 > 0.05
		- **mitigated**: 
			- **disparate_impact**: 1.0
			- **statistical_parity_difference**: 0.0
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.46647230320699706
				- **group_1_positive_rate**: 0.8046527540198426
			- **is_biased**: False
			- **bias_reasons**: 
		- **method**: Reweighing

---

### Code Bias Analysis
_Completed ai code bias analysis_

#### Parameters
- **paths**: 
	- C:/Users/habib/Documents/AutoClean/demo/input/code
- **analysis_type**: ai

#### Metrics
- **Duration**: 1 minutes 34.41 seconds
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **results**: 
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\demo\input\code\data_cleaner.py
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
					- **issue_type**: Data filtering bias
					- **explanation**: Removing records based on income thresholds may disproportionately exclude high-income individuals from certain demographics, reinforcing existing biases in the data.
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
					- **issue_type**: Gender bias
					- **explanation**: Binary encoding of gender excludes non-binary individuals and reinforces gender binary assumptions, which can lead to biased model outcomes.
				- value:
					- **code_snippet**:
						```python
	def reduce_females(self, ratio: float = 0.5) -> pd.DataFrame:
	        """Reduce the number of females in the dataset.
	        
	        """
	        num_females = int(self.df[self.df['gender'] == 0].shape[0] * ratio)
	        return self.df[self.df['gender'] == 0].sample(num_females, random_state=42)
						```
					- **issue_type**: Gender bias
					- **explanation**: Artificially reducing the number of females in the dataset introduces gender bias and may skew model results, disadvantaging female representation.
				- value:
					- **code_snippet**:
						```python
	def filter_by_age(self, min_age: int = 18, max_age: int = 65) -> pd.DataFrame:
	        """Filter dataset by age range.
	        
	        Note: Age filtering could introduce age-based discrimination.
	        """
	        return self.df[(self.df['age'] >= min_age) & (self.df['age'] <= max_age)]
						```
					- **issue_type**: Age bias
					- **explanation**: Filtering by age range may exclude younger or older individuals, leading to age-based discrimination in model outcomes.
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
					- **issue_type**: Education bias
					- **explanation**: Mapping education levels to numeric values may oversimplify or misrepresent non-traditional education paths, disadvantaging certain groups.
			- **recommendations**: 
				- Avoid hard income thresholds for outlier removal; consider using percentile-based methods or domain-specific insights to avoid demographic bias.
				- Expand gender encoding to include non-binary or other gender identities, or consider removing gender as a feature if not critical to the model.
				- Do not artificially reduce the representation of any gender; ensure balanced representation or use techniques like stratified sampling.
				- Review the necessity of age filtering; if required, ensure the age range is justified and does not exclude relevant demographics.
				- Include non-traditional education paths in the education mapping or use more granular categories to avoid disadvantaging certain groups.
			- **severity**: high
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\demo\input\code\feature_engineering.py
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
					- **explanation**: The wealth score is calculated using income and assets, which may amplify existing socioeconomic disparities. This could disadvantage individuals or groups with historically lower access to financial resources.
				- value:
					- **code_snippet**:
						```python
	self.df['high_income_area'] = self.df['neighborhood'].isin(high_income_areas).astype(int)
						```
					- **issue_type**: Residential Segregation Bias
					- **explanation**: Labeling neighborhoods as high-income areas based on income thresholds may reinforce residential segregation patterns and socioeconomic biases, disproportionately affecting marginalized communities.
				- value:
					- **code_snippet**:
						```python
	self.df['good_credit'] = (self.df['credit_score'] > 700).astype(int)
						```
					- **issue_type**: Credit Scoring Bias
					- **explanation**: Binary classification of credit scores may perpetuate historical disadvantages faced by certain demographic groups, as credit scoring systems can reflect systemic biases.
				- value:
					- **code_snippet**:
						```python
	self.df['education_score'] = (weights['degree_level'] * self.df['degree_level'] + weights['years_education'] * self.df['years_education'] + weights['test_scores'] * self.df['test_scores'])
						```
					- **issue_type**: Educational Bias
					- **explanation**: The education score combines degree level, years of education, and test scores, which may disadvantage individuals from non-traditional educational backgrounds or different cultural contexts.
			- **recommendations**: 
				- Consider alternative metrics for wealth scoring that account for systemic inequalities, such as cost-of-living adjustments or regional economic factors.
				- Avoid binary classifications for sensitive attributes like credit scores; use continuous scales or fairness-aware algorithms.
				- Include demographic fairness checks when creating composite scores (e.g., education or wealth scores) to ensure equitable representation.
				- Document the potential biases of neighborhood-based features and consider alternative approaches, such as community engagement or localized economic indicators.
				- Regularly audit the model for disparate impact on protected groups, especially for features derived from socioeconomic or demographic data.
			- **severity**: high
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\demo\input\code\sampling.py
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
					- **explanation**: The method 'sample_high_value_customers' filters data based on income, which could exclude lower-income groups and amplify representation biases in the dataset. This may disproportionately affect certain demographics.
				- value:
					- **code_snippet**:
						```python
	male = self.df[self.df['gender'] == 'M']
	female = self.df[self.df['gender'] == 'F']
						```
					- **issue_type**: Gender Binary Reinforcement
					- **explanation**: The method 'balanced_gender_sample' enforces a gender binary (M/F), ignoring non-binary or other gender identities. This could marginalize underrepresented groups and reinforce stereotypes.
				- value:
					- **code_snippet**:
						```python
	stratify=self.df['education']
						```
					- **issue_type**: Limited Demographic Stratification
					- **explanation**: The method 'stratified_education_split' stratifies only on education level, potentially missing other important demographic factors (e.g., race, income) and their intersections, leading to biased splits.
				- value:
					- **code_snippet**:
						```python
	age_group = self.df[(self.df['age'] >= min_age) & (self.df['age'] < max_age)]
						```
					- **issue_type**: Age-Based Bias
					- **explanation**: The method 'sample_by_age_group' samples based on age ranges, which could introduce age-based biases and overlook intersectional factors (e.g., age combined with income or race).
			- **recommendations**: 
				- Include lower-income groups in sampling to avoid representation biases.
				- Expand gender categories beyond binary (M/F) to include non-binary and other identities.
				- Stratify on multiple demographic factors (e.g., education, income, race) to ensure balanced representation.
				- Consider intersectional factors (e.g., age + income + race) when sampling to avoid oversimplified demographic splits.
			- **severity**: medium

---

### normalization
_Normalize numerical features_

#### Parameters
- **enabled**: True
- **method**: standard
- **exclude_features**: 

#### Metrics
- **Duration**: 116.72 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **ExistingCreditsCount**: 
		- **before**: Int64
		- **after**: float64
	- **Sex**: 
		- **before**: bool
		- **after**: float64
	- **LoanAmount**: 
		- **before**: Int64
		- **after**: float64
	- **CheckingStatus**: 
		- **before**: Int64
		- **after**: float64
	- **LoanDuration**: 
		- **before**: Int64
		- **after**: float64
	- **EmploymentDuration**: 
		- **before**: Int64
		- **after**: float64
	- **ForeignWorker**: 
		- **before**: bool
		- **after**: float64
	- **OthersOnLoan**: 
		- **before**: Int64
		- **after**: float64
	- **Dependents**: 
		- **before**: bool
		- **after**: float64
	- **CreditHistory**: 
		- **before**: Int64
		- **after**: float64
	- **InstallmentPercent**: 
		- **before**: Int64
		- **after**: float64
	- **CurrentResidenceDuration**: 
		- **before**: Int64
		- **after**: float64
	- **OwnsProperty**: 
		- **before**: Int64
		- **after**: float64
	- **ExistingSavings**: 
		- **before**: Int64
		- **after**: float64
	- **LoanPurpose**: 
		- **before**: Int64
		- **after**: float64
	- **Age**: 
		- **before**: Int64
		- **after**: float64
	- **Job**: 
		- **before**: Int64
		- **after**: float64
	- **Telephone**: 
		- **before**: bool
		- **after**: float64
	- **Housing**: 
		- **before**: Int64
		- **after**: float64
	- **Risk**: 
		- **before**: bool
		- **after**: float64
	- **InstallmentPlans**: 
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
		- **mean_change**: -1.3099779160811083
		- **std_change**: -0.05742134241925845
		- **min_change**: -1.2388487017038337
		- **max_change**: -1.40174277839956
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
		- **mean_change**: -1.1981529813290503
		- **std_change**: 0.17195311912251598
		- **min_change**: -1.44693257396541
		- **max_change**: -0.8240248238372061
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
		- **OwnsProperty**: 1.3099779160811083
		- **Age**: 35.98594659706886
		- **InstallmentPlans**: 1.1092150170648465
		- **Housing**: 1.0620357357960248
		- **ExistingCreditsCount**: 1.4669745031118249
		- **Job**: 1.1981529813290503
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
		- **OwnsProperty**: 1.0574155780923433
		- **Age**: 10.6052436930396
		- **InstallmentPlans**: 0.5332899014565414
		- **Housing**: 0.5957473189417688
		- **ExistingCreditsCount**: 0.5646014571473831
		- **Job**: 0.8280641426472531
		- **Dependents**: 0.3712050084113143
		- **Telephone**: 0.4924028423139223
		- **ForeignWorker**: 0.15519037023607435
		- **Risk**: 0.4720160765497867

---

### Data Profiling
_Generate data profile reports_

#### Parameters
- **threshold**: 10000
- **sample_size**: 1000
- **output_prefix**: after_preprocessing

#### Metrics
- **Duration**: 48.24 seconds
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 21 columns
- **Success**: True

#### Changes Made

---

### dimensionality_reduction
_Reduce data dimensionality_

#### Parameters
- **enabled**: True
- **method**: pca
- **n_components**: None
- **target_explained_variance**: 0.95

#### Metrics
- **Duration**: 35.57 ms
- **Input Shape**: 4981 rows x 21 columns
- **Output Shape**: 4981 rows x 18 columns
- **Success**: True

#### Changes Made
- **added_columns**: 
	- component_5
	- component_17
	- component_3
	- component_6
	- component_8
	- component_16
	- component_13
	- component_10
	- component_7
	- component_9
	- component_1
	- component_14
	- component_12
	- component_11
	- component_15
	- component_2
	- component_18
	- component_4
- **removed_columns**: 
	- ExistingCreditsCount
	- Sex
	- LoanAmount
	- CheckingStatus
	- LoanDuration
	- EmploymentDuration
	- ForeignWorker
	- OthersOnLoan
	- Dependents
	- CreditHistory
	- InstallmentPercent
	- CurrentResidenceDuration
	- OwnsProperty
	- ExistingSavings
	- LoanPurpose
	- Age
	- Job
	- Telephone
	- Housing
	- Risk
	- InstallmentPlans
- **explained_variance_ratio**: 
	- 0.2972879917998952
	- 0.0629405821542624
	- 0.05417286233874022
	- 0.04894043632595014
	- 0.04869390177053954
	- 0.0469734724849335
	- 0.04562647569102889
	- 0.04467983839857955
	- 0.0423656931556035
	- 0.03909906126194705
	- 0.036791965826506276
	- 0.0340866168149801
	- 0.030799103977649123
	- 0.030530781836829776
	- 0.028403340561237306
	- 0.024876917188334645
	- 0.021462842071720507
	- 0.019026551904551055
- **n_components**: 18
- **total_variance_explained**: 0.9567584355632889

---

### Data Profiling
_Generate data profile reports_

#### Parameters
- **threshold**: 10000
- **sample_size**: 1000
- **output_prefix**: after_dim_reduction

#### Metrics
- **Duration**: 38.25 seconds
- **Input Shape**: 4981 rows x 18 columns
- **Output Shape**: 4981 rows x 18 columns
- **Success**: True

#### Changes Made

---
