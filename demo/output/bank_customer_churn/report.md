# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-05-16T11:11:36.242713
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 96.67 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made

---

### missing_value_handling
_Handle missing values in the dataset_

#### Parameters
- **numerical_method**: knn
- **categorical_method**: knn

#### Metrics
- **Duration**: 62.45 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made

---

### outlier_handling
_Handle outliers in numerical features_

#### Parameters
- **method**: delete
- **outlier_param**: 1.5

#### Metrics
- **Duration**: 129.18 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **row_count**: 
	- **before**: 10000
	- **after**: 9940
	- **difference**: 60
- **statistics_changes**: 
	- **customer_id**: 
		- **mean_change**: 86.4102780688554
		- **std_change**: 16.85943429537292
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **credit_score**: 
		- **mean_change**: -0.018437826961871906
		- **std_change**: -0.0234665280995614
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **age**: 
		- **mean_change**: -0.040814084507040604
		- **std_change**: -0.0026049139824380063
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **tenure**: 
		- **mean_change**: -0.0017336016096587414
		- **std_change**: -0.0002730755253685935
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **balance**: 
		- **mean_change**: -104.10812301005353
		- **std_change**: 16.55101395418751
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **products_number**: 
		- **mean_change**: -0.014908249496981885
		- **std_change**: -0.030911401623937018
		- **min_change**: 0.0
		- **max_change**: -1.0
	- **credit_card**: 
		- **mean_change**: 0.00013380281690134055
		- **std_change**: -6.021249330961931e-05
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **active_member**: 
		- **mean_change**: 0.0001917505030181177
		- **std_change**: -5.679760791910127e-06
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **estimated_salary**: 
		- **mean_change**: -28.210161684110062
		- **std_change**: 1.6448911010447773
		- **min_change**: 0.0
		- **max_change**: 0.0
	- **churn**: 
		- **mean_change**: -0.004806639839034205
		- **std_change**: -0.003580880383217855
		- **min_change**: 0.0
		- **max_change**: 0.0

---

### field_assignments
_Assign field types_

#### Parameters

#### Metrics
- **Duration**: 448.60 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **gender**: 
		- **before**: object
		- **after**: bool
	- **age**: 
		- **before**: int64
		- **after**: float64
	- **products_number**: 
		- **before**: int64
		- **after**: float64
	- **credit_card**: 
		- **before**: int64
		- **after**: bool
	- **churn**: 
		- **before**: int64
		- **after**: bool
	- **credit_score**: 
		- **before**: int64
		- **after**: float64
	- **customer_id**: 
		- **before**: int64
		- **after**: float64
	- **active_member**: 
		- **before**: int64
		- **after**: bool
	- **tenure**: 
		- **before**: int64
		- **after**: float64
- **statistics_changes**: 
	- **credit_card**: 
		- **mean_change**: None
		- **std_change**: None
		- **min_change**: None
		- **max_change**: None
	- **active_member**: 
		- **mean_change**: None
		- **std_change**: None
		- **min_change**: None
		- **max_change**: None
	- **churn**: 
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
- **Duration**: 76.92 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made

---

### categorical_encoding
_Encode categorical features_

#### Parameters
- **method**: 
	- label

#### Metrics
- **Duration**: 69.15 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **country**: 
		- **before**: object
		- **after**: int64

---

### value_rounding
_Round numerical values to appropriate precision_

#### Parameters

#### Metrics
- **Duration**: 106.85 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **age**: 
		- **before**: float64
		- **after**: Int64
	- **products_number**: 
		- **before**: float64
		- **after**: Int64
	- **country**: 
		- **before**: int64
		- **after**: Int64
	- **credit_score**: 
		- **before**: float64
		- **after**: Int64
	- **customer_id**: 
		- **before**: float64
		- **after**: Int64
	- **tenure**: 
		- **before**: float64
		- **after**: Int64

---

### Sensitive Feature Detection
_Use AI to detect potentially sensitive features_

#### Parameters

#### Metrics
- **Duration**: 1 minutes 41.00 seconds
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
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
		- **sensibility_level**: 4
		- **justification**: The 'customer_id' feature is a unique identifier for customers, which could potentially be used to re-identify individuals if combined with other data. While it does not directly reveal personal information, it poses a risk if linked to external datasets.
		- **recommendation**: Anonymize or pseudonymize the 'customer_id' to prevent re-identification. Ensure it is not stored alongside other sensitive data without proper safeguards.
		- **column**: customer_id
	- **credit_score**
		- **is_sensitive**: False
		- **sensibility_level**: 6
		- **justification**: Credit scores are financial data that can indirectly reveal personal financial health and creditworthiness. While not a direct identifier, they can be sensitive and may lead to discrimination or bias in lending or other financial decisions.
		- **recommendation**: Anonymize or aggregate credit scores into broader categories (e.g., low, medium, high) to reduce sensitivity. Ensure compliance with financial data protection regulations (e.g., GDPR, CCPA).
		- **column**: credit_score
	- **country**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'country' feature contains binary values (1 and 0) and lacks context about which countries these values represent. Without additional identifiers or mappings, it does not directly reveal personal or sensitive information.
		- **recommendation**: None
		- **column**: country
	- **gender**
		- **is_sensitive**: False
		- **sensibility_level**: 6
		- **justification**: Gender is a protected characteristic under many privacy and anti-discrimination laws. While the data is binary (True/False), it can still lead to bias in predictive models, especially in financial contexts like churn prediction.
		- **recommendation**: Anonymize or aggregate the data to avoid direct identification. Ensure the model is audited for gender bias and consider excluding this feature if it does not significantly improve predictive performance.
		- **column**: gender
	- **age**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: Age is a demographic attribute but does not directly reveal personal or confidential information. In the context of bank customer churn prediction, it is unlikely to pose significant privacy risks or bias concerns.
		- **recommendation**: None
		- **column**: age
	- **tenure**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'tenure' feature represents the duration of a customer's relationship with the bank, which is non-sensitive and does not reveal personal or confidential information. It is a numerical value that does not pose any risk of discrimination or bias.
		- **recommendation**: None
		- **column**: tenure
	- **balance**
		- **is_sensitive**: False
		- **sensibility_level**: 6
		- **justification**: The 'balance' feature contains financial data, which is inherently sensitive. While it does not directly identify individuals, it could potentially be used in combination with other features to re-identify customers or infer financial status, leading to privacy concerns or discrimination risks.
		- **recommendation**: Anonymize or aggregate the data to reduce granularity (e.g., binning into ranges). Ensure compliance with financial data protection regulations (e.g., GDPR, CCPA). Limit access to this feature to authorized personnel only.
		- **column**: balance
	- **products_number**
		- **is_sensitive**: False
		- **sensibility_level**: 0
		- **justification**: The feature 'products_number' represents the count of products a customer has with the bank. It does not contain any personal identifiers, protected characteristics, or other sensitive information.
		- **recommendation**: None
		- **column**: products_number
	- **credit_card**
		- **is_sensitive**: False
		- **sensibility_level**: 9
		- **justification**: The 'credit_card' feature indicates whether a customer has a credit card, which is financial data. Financial data is highly sensitive and can be used for identity theft or fraud if exposed. Additionally, in the context of a bank customer churn prediction dataset, this feature could indirectly reveal financial behaviors or vulnerabilities of customers.
		- **recommendation**: Anonymize or aggregate this feature to reduce sensitivity. If possible, avoid storing this data in raw form and use encryption for storage. Ensure compliance with financial data protection regulations like PCI-DSS.
		- **column**: credit_card
	- **active_member**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: The 'active_member' feature indicates whether a customer is an active member of the bank (True/False). This is non-sensitive, public information and does not reveal personal or confidential details. It also does not pose a risk of discrimination or bias.
		- **recommendation**: None
		- **column**: active_member
	- **estimated_salary**
		- **is_sensitive**: False
		- **sensibility_level**: 7
		- **justification**: The 'estimated_salary' feature contains financial data, which is inherently sensitive. While it does not directly identify individuals, it could potentially be used in combination with other features to re-identify customers or infer personal financial status, leading to privacy concerns or discrimination risks.
		- **recommendation**: Anonymize or aggregate the salary data (e.g., binning into salary ranges) to reduce re-identification risk. Ensure compliance with financial data protection regulations (e.g., GDPR, CCPA) and limit access to authorized personnel only.
		- **column**: estimated_salary

---

### Fairness Analysis credit_score
_Analyze and mitigate bias for feature credit_score_

#### Parameters

#### Metrics
- **Duration**: 57.66 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: nan
		- **statistical_parity_difference**: nan
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.20880913539967375
			- **group_1_positive_rate**: 0.1892374900714853
		- **is_biased**: False
		- **bias_reasons**: 
	- **mitigated**: None
	- **method**: None

---

### Fairness Analysis gender
_Analyze and mitigate bias for feature gender_

#### Parameters

#### Metrics
- **Duration**: 56.95 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: 0.659495800004512
		- **statistical_parity_difference**: -0.08321756363929683
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.16117755289788407
			- **group_1_positive_rate**: 0.2443951165371809
		- **is_biased**: True
		- **bias_reasons**: 
			- Disparate Impact de 0.6595 < 0.8 (sous-représentation du groupe non privilégié)
			- Statistical Parity Difference de 0.0832 > 0.05
	- **mitigated**: 
		- **disparate_impact**: 1.0000000000000002
		- **statistical_parity_difference**: 5.551115123125783e-17
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.16117755289788407
			- **group_1_positive_rate**: 0.2443951165371809
		- **is_biased**: False
		- **bias_reasons**: 
	- **method**: Reweighing

---

### Fairness Analysis balance
_Analyze and mitigate bias for feature balance_

#### Parameters

#### Metrics
- **Duration**: 56.76 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: nan
		- **statistical_parity_difference**: nan
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.14623338257016247
			- **group_1_positive_rate**: 0.23528411024157878
		- **is_biased**: False
		- **bias_reasons**: 
	- **mitigated**: None
	- **method**: None

---

### Fairness Analysis credit_card
_Analyze and mitigate bias for feature credit_card_

#### Parameters

#### Metrics
- **Duration**: 33.34 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: 1.029569585569129
		- **statistical_parity_difference**: 0.005830444374409077
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.20300751879699247
			- **group_1_positive_rate**: 0.1971770744225834
		- **is_biased**: False
		- **bias_reasons**: 
	- **mitigated**: None
	- **method**: None

---

### Fairness Analysis estimated_salary
_Analyze and mitigate bias for feature estimated_salary_

#### Parameters

#### Metrics
- **Duration**: 79.40 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **original**: 
		- **disparate_impact**: nan
		- **statistical_parity_difference**: nan
		- **equal_opportunity_difference**: None
		- **average_odds_difference**: None
		- **group_metrics**: 
			- **group_0_positive_rate**: 0.19508757801489832
			- **group_1_positive_rate**: 0.2026945505730947
		- **is_biased**: False
		- **bias_reasons**: 
	- **mitigated**: None
	- **method**: None

---

### Fairness Analysis
_Analyze and mitigate bias for each sensitive feature_

#### Parameters

#### Metrics
- **Duration**: 289.81 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
	- **credit_score**: 
		- **original**: 
			- **disparate_impact**: nan
			- **statistical_parity_difference**: nan
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.20880913539967375
				- **group_1_positive_rate**: 0.1892374900714853
			- **is_biased**: False
			- **bias_reasons**: 
		- **mitigated**: None
		- **method**: None
	- **gender**: 
		- **original**: 
			- **disparate_impact**: 0.659495800004512
			- **statistical_parity_difference**: -0.08321756363929683
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.16117755289788407
				- **group_1_positive_rate**: 0.2443951165371809
			- **is_biased**: True
			- **bias_reasons**: 
				- Disparate Impact de 0.6595 < 0.8 (sous-représentation du groupe non privilégié)
				- Statistical Parity Difference de 0.0832 > 0.05
		- **mitigated**: 
			- **disparate_impact**: 1.0000000000000002
			- **statistical_parity_difference**: 5.551115123125783e-17
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.16117755289788407
				- **group_1_positive_rate**: 0.2443951165371809
			- **is_biased**: False
			- **bias_reasons**: 
		- **method**: Reweighing
	- **balance**: 
		- **original**: 
			- **disparate_impact**: nan
			- **statistical_parity_difference**: nan
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.14623338257016247
				- **group_1_positive_rate**: 0.23528411024157878
			- **is_biased**: False
			- **bias_reasons**: 
		- **mitigated**: None
		- **method**: None
	- **credit_card**: 
		- **original**: 
			- **disparate_impact**: 1.029569585569129
			- **statistical_parity_difference**: 0.005830444374409077
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.20300751879699247
				- **group_1_positive_rate**: 0.1971770744225834
			- **is_biased**: False
			- **bias_reasons**: 
		- **mitigated**: None
		- **method**: None
	- **estimated_salary**: 
		- **original**: 
			- **disparate_impact**: nan
			- **statistical_parity_difference**: nan
			- **equal_opportunity_difference**: None
			- **average_odds_difference**: None
			- **group_metrics**: 
				- **group_0_positive_rate**: 0.19508757801489832
				- **group_1_positive_rate**: 0.2026945505730947
			- **is_biased**: False
			- **bias_reasons**: 
		- **mitigated**: None
		- **method**: None

---

### Code Bias Analysis
_Completed ai code bias analysis_

#### Parameters
- **paths**: 
	- C:/Users/habib/Documents/AutoClean/demo/input/code
- **analysis_type**: ai

#### Metrics
- **Duration**: 1 minutes 43.46 seconds
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\demo\input\code\data_cleaner.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 7
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
					- **explanation**: Removing records based on income thresholds may disproportionately exclude high-income individuals, potentially skewing the dataset towards lower-income groups. This could introduce socioeconomic bias.
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
					- **explanation**: Binary encoding of gender reinforces a gender binary and excludes non-binary or other gender identities, leading to potential discrimination and exclusion.
				- value:
					- **code_snippet**:
						```python
	def reduce_females(self, ratio: float = 0.5) -> pd.DataFrame:
	        """Reduce the number of females in the dataset.
	        
	        """
	        num_females = int(self.df[self.df['gender'] == 0].shape[0] * ratio)
	        return self.df[self.df['gender'] == 0].sample(num_females, random_state=42)
						```
					- **issue_type**: Data filtering
					- **explanation**: Artificially reducing the number of females in the dataset introduces gender bias and may lead to underrepresentation of women in the analysis.
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
					- **explanation**: Filtering by age may exclude younger or older individuals, leading to age-based discrimination and a lack of representation for these groups.
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
					- **explanation**: Mapping education levels to a simplified numeric scale may disadvantage individuals with non-traditional education paths or unrecognized qualifications.
			- **recommendations**: 
				- Avoid hard income thresholds; consider using percentiles or other statistical methods to identify outliers.
				- Use a more inclusive gender encoding scheme (e.g., allowing for non-binary or other gender identities).
				- Do not artificially reduce the representation of any gender; ensure balanced sampling if necessary.
				- Justify age filtering with a clear rationale and consider including broader age ranges if possible.
				- Expand the education mapping to include non-traditional education paths or provide an 'Other' category.
			- **severity**: high
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\demo\input\code\feature_engineering.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 8
			- **problematic_sections**: 
				- value:
					- **code_snippet**:
						```python
	self.df['wealth_score'] = (
	            0.6 * self.df['income'] +
	            0.4 * self.df['assets']
	        )
						```
					- **issue_type**: Socioeconomic Bias
					- **explanation**: The wealth score is a composite of income and assets, which may amplify existing socioeconomic disparities. This could disproportionately disadvantage individuals or groups with lower income or asset levels.
				- value:
					- **code_snippet**:
						```python
	neighborhood_means = self.df.groupby('neighborhood')['income'].mean()
	        high_income_areas = neighborhood_means[neighborhood_means > high_income_threshold].index
	        self.df['high_income_area'] = self.df['neighborhood'].isin(high_income_areas).astype(int)
						```
					- **issue_type**: Residential Segregation Bias
					- **explanation**: Labeling neighborhoods as 'high income' based on income thresholds may reinforce residential segregation patterns and socioeconomic biases, potentially disadvantaging residents of lower-income areas.
				- value:
					- **code_snippet**:
						```python
	self.df['good_credit'] = (self.df['credit_score'] > 700).astype(int)
						```
					- **issue_type**: Credit Scoring Bias
					- **explanation**: Binary classification of credit scores as 'good' or not may perpetuate historical disadvantages faced by certain demographic groups, as credit scoring systems often reflect systemic biases.
				- value:
					- **code_snippet**:
						```python
	weights = {
	            'degree_level': 0.5,
	            'years_education': 0.3,
	            'test_scores': 0.2
	        }
	        
	        self.df['education_score'] = (
	            weights['degree_level'] * self.df['degree_level'] +
	            weights['years_education'] * self.df['years_education'] +
	            weights['test_scores'] * self.df['test_scores']
	        )
						```
					- **issue_type**: Educational Bias
					- **explanation**: The education score weights traditional metrics like degree level and test scores, which may disadvantage individuals from non-traditional educational backgrounds or different cultural contexts.
			- **recommendations**: 
				- Consider alternative or supplementary metrics for wealth scoring that account for cost of living or regional economic disparities.
				- Avoid binary classifications of neighborhoods based on income; instead, use continuous or more nuanced features.
				- Review credit scoring thresholds for potential biases and consider using percentile-based classifications.
				- Include diverse educational metrics (e.g., certifications, vocational training) in the education score to reduce bias.
				- Conduct fairness audits on the engineered features to ensure they do not disproportionately impact marginalized groups.
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
					- **explanation**: The method 'sample_high_value_customers' focuses exclusively on high-income customers, which could exclude or underrepresent lower-income groups, potentially amplifying socioeconomic biases in the dataset.
				- value:
					- **code_snippet**:
						```python
	male = self.df[self.df['gender'] == 'M']
	female = self.df[self.df['gender'] == 'F']
						```
					- **issue_type**: Gender Binary Reinforcement
					- **explanation**: The method 'balanced_gender_sample' enforces a binary gender classification (M/F), which excludes non-binary or other gender identities, reinforcing gender stereotypes and excluding marginalized groups.
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
					- **explanation**: The method 'stratified_education_split' stratifies only on education level, ignoring other demographic factors (e.g., race, gender, income), which could lead to imbalances in these dimensions.
				- value:
					- **code_snippet**:
						```python
	age_group = self.df[
	    (self.df['age'] >= min_age) &
	    (self.df['age'] < max_age)
	]
						```
					- **issue_type**: Age-Based Bias
					- **explanation**: The method 'sample_by_age_group' samples based on age ranges, which could introduce age-based biases and overlook intersectional factors (e.g., age combined with income or education).
			- **recommendations**: 
				- Expand the 'sample_high_value_customers' method to include a broader range of income levels or use weighted sampling to ensure representation of lower-income groups.
				- Modify the 'balanced_gender_sample' method to include non-binary or other gender identities, or avoid gender-based sampling if not critical to the analysis.
				- Enhance the 'stratified_education_split' method to include multiple stratification variables (e.g., race, gender, income) to ensure balanced representation across demographics.
				- Review the 'sample_by_age_group' method to ensure age-based sampling is necessary and consider intersectional factors (e.g., age and income) to avoid biased outcomes.
			- **severity**: medium

---

### normalization
_Normalize numerical features_

#### Parameters
- **enabled**: True
- **method**: standard
- **exclude_features**: 

#### Metrics
- **Duration**: 129.86 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **gender**: 
		- **before**: bool
		- **after**: float64
	- **age**: 
		- **before**: Int64
		- **after**: float64
	- **products_number**: 
		- **before**: Int64
		- **after**: float64
	- **credit_card**: 
		- **before**: bool
		- **after**: float64
	- **churn**: 
		- **before**: bool
		- **after**: float64
	- **country**: 
		- **before**: Int64
		- **after**: float64
	- **credit_score**: 
		- **before**: Int64
		- **after**: float64
	- **customer_id**: 
		- **before**: Int64
		- **after**: float64
	- **active_member**: 
		- **before**: bool
		- **after**: float64
	- **tenure**: 
		- **before**: Int64
		- **after**: float64
- **statistics_changes**: 
	- **customer_id**: 
		- **mean_change**: -15691026.979678068
		- **std_change**: -71952.04550673866
		- **min_change**: -15565702.741862116
		- **max_change**: -15815688.267352125
	- **credit_score**: 
		- **mean_change**: -650.5103621730382
		- **std_change**: -95.6297819024242
		- **min_change**: -353.1100693508616
		- **max_change**: -847.9354235776307
	- **country**: 
		- **mean_change**: -0.7469818913480886
		- **std_change**: 0.17176843577301637
		- **min_change**: -0.9018904022073339
		- **max_change**: -0.4871319919875632
	- **age**: 
		- **mean_change**: -38.88098591549296
		- **std_change**: -9.485151232115578
		- **min_change**: -19.9915722431304
		- **max_change**: -86.93365138689815
	- **tenure**: 
		- **mean_change**: -5.011066398390342
		- **std_change**: -1.8918509959177234
		- **min_change**: -1.7328801921710564
		- **max_change**: -8.274773564951563
	- **balance**: 
		- **mean_change**: -76381.78116498995
		- **std_change**: -62412.956166034535
		- **min_change**: -1.2238548591929517
		- **max_change**: -250895.293748992
	- **products_number**: 
		- **mean_change**: -1.5152917505030181
		- **std_change**: 0.44930734923153837
		- **min_change**: -1.9356772821188288
		- **max_change**: -0.30403644484387415
	- **estimated_salary**: 
		- **mean_change**: -100062.02971931589
		- **std_change**: -57511.1376584936
		- **min_change**: -13.31972811312438
		- **max_change**: -199990.74235849816
- **feature_stats**: 
	- **mean**: 
		- **customer_id**: 15691026.979678068
		- **credit_score**: 650.5103621730382
		- **country**: 0.7469818913480886
		- **gender**: 0.45321931589537223
		- **age**: 38.88098591549296
		- **tenure**: 5.011066398390342
		- **balance**: 76381.78116498995
		- **products_number**: 1.5152917505030181
		- **credit_card**: 0.7056338028169014
		- **active_member**: 0.5152917505030181
		- **estimated_salary**: 100062.02971931589
		- **churn**: 0.1988933601609658
	- **std**: 
		- **customer_id**: 71949.42609752051
		- **credit_score**: 96.6249714302311
		- **country**: 0.8282402047076739
		- **gender**: 0.49780675728107887
		- **age**: 10.484674099831663
		- **tenure**: 2.8917558299931727
		- **balance**: 62410.81660235307
		- **products_number**: 0.5507152523102268
		- **credit_card**: 0.45575732483313935
		- **active_member**: 0.49976610766092716
		- **estimated_salary**: 57509.24467136138
		- **churn**: 0.39916762324222405

---

### dimensionality_reduction
_Reduce data dimensionality_

#### Parameters
- **enabled**: True
- **method**: pca
- **n_components**: None
- **target_explained_variance**: 0.95

#### Metrics
- **Duration**: 26.46 ms
- **Input Shape**: 9940 rows x 12 columns
- **Output Shape**: 9940 rows x 12 columns
- **Success**: True

#### Changes Made
- **added_columns**: 
	- component_10
	- component_9
	- component_11
	- component_5
	- component_3
	- component_8
	- component_1
	- component_12
	- component_4
	- component_6
	- component_7
	- component_2
- **removed_columns**: 
	- gender
	- age
	- products_number
	- credit_card
	- churn
	- country
	- estimated_salary
	- credit_score
	- customer_id
	- balance
	- active_member
	- tenure
- **explained_variance_ratio**: 
	- 0.12391027522432616
	- 0.09976944921521487
	- 0.09170578064433561
	- 0.08624100953912858
	- 0.08477911963924477
	- 0.08300677385783405
	- 0.08254473490900796
	- 0.08182843871078954
	- 0.08087751346301383
	- 0.07858664683535288
	- 0.055241778715748605
	- 0.051508479246003026
- **n_components**: 12
- **total_variance_explained**: 0.9999999999999999

---
