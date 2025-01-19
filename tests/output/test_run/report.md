# FairAutoCleaner Report

## Summary
- **Start Time**: 2025-01-19T05:39:23.715762
- **End Time**: None
- **Total Duration**: N/A
- **Total Operations**: 0

## Operations Details
### duplicate_handling
_Remove duplicate rows from the dataset_

#### Parameters
- **method**: auto

#### Metrics
- **Duration**: 64.47 ms
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
- **Duration**: 57.10 ms
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
- **Duration**: 58.34 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **country**: 
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
- **Duration**: 92.94 ms
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **dtype_changes**: 
	- **credit_score**: 
		- **before**: int64
		- **after**: Int64
	- **tenure**: 
		- **before**: int64
		- **after**: Int64
	- **customer_id**: 
		- **before**: int64
		- **after**: Int64
	- **credit_card**: 
		- **before**: int64
		- **after**: Int64
	- **country**: 
		- **before**: int64
		- **after**: Int64
	- **active_member**: 
		- **before**: int64
		- **after**: Int64
	- **churn**: 
		- **before**: int64
		- **after**: Int64
	- **age**: 
		- **before**: int64
		- **after**: Int64
	- **gender**: 
		- **before**: int64
		- **after**: Int64
	- **products_number**: 
		- **before**: int64
		- **after**: Int64

---

### Sensitive Feature Detection
_Use AI to detect potentially sensitive features_

#### Parameters

#### Metrics
- **Duration**: 40.85 seconds
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
		- **sensibility_level**: 1
		- **justification**: None
		- **recommendation**: None
		- **column**: customer_id
	- **credit_score**
		- **is_sensitive**: True
		- **sensibility_level**: 7
		- **justification**: Credit scores are sensitive financial data that can reveal personal financial health and creditworthiness. They can be used to discriminate against individuals in financial services.
		- **recommendation**: Anonymize or aggregate credit scores to reduce identifiability. Ensure compliance with financial data protection regulations like GDPR or CCPA.
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
		- **justification**: Gender is a protected characteristic and can lead to discrimination or bias in downstream applications, such as in predicting customer churn. It can also be used in conjunction with other data to re-identify individuals.
		- **recommendation**: Consider anonymizing or aggregating gender data. Ensure that any models using this feature are regularly audited for bias. Implement strict access controls and data governance policies to protect this sensitive information.
		- **column**: gender
	- **age**
		- **is_sensitive**: False
		- **sensibility_level**: 2
		- **justification**: Age is a common demographic feature and is generally considered non-sensitive. It does not directly reveal personal or confidential information.
		- **recommendation**: No special handling required. However, consider the context of use to ensure it does not contribute to age-based discrimination.
		- **column**: age
	- **tenure**
		- **is_sensitive**: False
		- **sensibility_level**: 1
		- **justification**: The 'tenure' feature represents the number of months a customer has been with the bank. This is non-sensitive, public information that does not reveal personal or confidential details.
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
		- **justification**: The 'credit_card' feature contains binary data indicating the presence or absence of a credit card. While it does not directly reveal personal information, it is highly sensitive as it relates to financial data. This feature could be used in conjunction with other data to re-identify individuals or infer financial status, posing a high risk of privacy violation.
		- **recommendation**: Consider anonymizing or aggregating this data to reduce the risk of re-identification. Ensure that access to this feature is restricted and that it is used only for legitimate purposes. Implement strong data security measures to protect this sensitive information.
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
		- **recommendation**: Consider anonymizing or aggregating the salary data to reduce the risk of re-identification. Access to this feature should be restricted and only provided to authorized personnel. Additionally, ensure compliance with relevant financial data protection regulations.
		- **column**: estimated_salary

---

### Code Bias Analysis
_Completed ai code bias analysis_

#### Parameters
- **paths**: 
	- C:/Users/habib/Documents/AutoClean/tests/preprocessing
- **analysis_type**: ai

#### Metrics
- **Duration**: 40.31 seconds
- **Input Shape**: 10000 rows x 12 columns
- **Output Shape**: 10000 rows x 12 columns
- **Success**: True

#### Changes Made
- **results**: 
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\tests\preprocessing\data_cleaner.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 8
			- **problematic_sections**: 
				- value:
					- **code_snippet**:
						```python
						def remove_outliers_by_income(self, threshold: float = 100000) -> pd.DataFrame:
						    return self.df[self.df['income'] <= threshold]
						```
					- **issue_type**: Data filtering
					- **explanation**: Removing records based on income threshold could disproportionately exclude certain demographics, particularly those in high-income brackets, which may correlate with specific racial or geographic groups.
				- value:
					- **code_snippet**:
						```python
						def encode_gender(self) -> pd.DataFrame:
						    gender_map = {'M': 1, 'F': 0}
						    self.df['gender'] = self.df['gender'].map(gender_map)
						```
					- **issue_type**: Feature engineering
					- **explanation**: Binary encoding of gender reinforces gender binary assumptions and excludes non-binary individuals, potentially leading to discrimination and bias in the model.
				- value:
					- **code_snippet**:
						```python
						def reduce_females(self, ratio: float = 0.5) -> pd.DataFrame:
						    num_females = int(self.df[self.df['gender'] == 0].shape[0] * ratio)
						    return self.df[self.df['gender'] == 0].sample(num_females, random_state=42)
						```
					- **issue_type**: Data filtering
					- **explanation**: Reducing the number of females in the dataset introduces gender bias, which could lead to unfair treatment and discrimination against females in the model's predictions.
				- value:
					- **code_snippet**:
						```python
						def filter_by_age(self, min_age: int = 18, max_age: int = 65) -> pd.DataFrame:
						    return self.df[(self.df['age'] >= min_age) & (self.df['age'] <= max_age)]
						```
					- **issue_type**: Data filtering
					- **explanation**: Filtering by age range could introduce age-based discrimination, excluding younger or older individuals who may have different characteristics or needs.
				- value:
					- **code_snippet**:
						```python
						def normalize_education(self) -> pd.DataFrame:
						    edu_map = {
						        'Some High School': 0,
						        'High School': 1,
						        'Some College': 2,
						        'Bachelors': 3,
						        'Masters': 4,
						        'PhD': 5
						    }
						    self.df['education'] = self.df['education'].map(edu_map)
						```
					- **issue_type**: Feature engineering
					- **explanation**: Simplification of education levels might disadvantage those with non-traditional education paths, leading to bias against individuals with alternative educational backgrounds.
			- **recommendations**: 
				- Consider using more nuanced income thresholds or alternative methods to handle outliers without disproportionately affecting certain demographics.
				- Expand gender encoding to include non-binary and other gender identities to avoid reinforcing gender binary assumptions.
				- Avoid reducing the representation of any gender in the dataset to prevent gender bias.
				- Use broader age ranges or consider the impact of age filtering on different demographic groups.
				- Include more granular education categories or consider alternative ways to represent educational background to avoid disadvantaging non-traditional education paths.
			- **severity**: high
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\tests\preprocessing\feature_engineering.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 8
			- **problematic_sections**: 
				- value:
					- **code_snippet**:
						```python
						self.df['wealth_score'] = (0.6 * self.df['income'] + 0.4 * self.df['assets'])
						```
					- **issue_type**: Amplification of socioeconomic disparities
					- **explanation**: The creation of a wealth score based solely on income and assets may amplify existing socioeconomic disparities, as it does not account for other factors that might influence wealth distribution.
				- value:
					- **code_snippet**:
						```python
						self.df['high_income_area'] = self.df['neighborhood'].isin(high_income_areas).astype(int)
						```
					- **issue_type**: Reinforcement of residential segregation
					- **explanation**: Labeling neighborhoods as high-income areas based on income thresholds can reinforce residential segregation patterns and socioeconomic biases.
				- value:
					- **code_snippet**:
						```python
						self.df['good_credit'] = (self.df['credit_score'] > 700).astype(int)
						```
					- **issue_type**: Perpetuation of historical disadvantages
					- **explanation**: Creating a binary feature for 'good' credit based on a fixed threshold may perpetuate historical disadvantages faced by certain demographic groups, as credit scoring systems can be biased.
				- value:
					- **code_snippet**:
						```python
						self.df['education_score'] = (weights['degree_level'] * self.df['degree_level'] + weights['years_education'] * self.df['years_education'] + weights['test_scores'] * self.df['test_scores'])
						```
					- **issue_type**: Disadvantage to non-traditional educational backgrounds
					- **explanation**: The education score may disadvantage individuals from non-traditional educational backgrounds or different cultural contexts, as it heavily weights degree level and test scores.
			- **recommendations**: 
				- Consider including additional factors in the wealth score calculation to account for a more comprehensive view of wealth.
				- Avoid labeling neighborhoods based solely on income thresholds; consider using a more nuanced approach that includes multiple socioeconomic indicators.
				- Evaluate the credit scoring threshold and consider using a more dynamic or context-aware method to determine 'good' credit.
				- Incorporate alternative educational metrics that account for non-traditional educational paths and cultural differences in the education score calculation.
			- **severity**: high
	- value:
		- **file**: C:\Users\habib\Documents\AutoClean\tests\preprocessing\sampling.py
		- **analysis**: 
			- **is_problematic**: True
			- **sensitivity_level**: 7
			- **problematic_sections**: 
				- value:
					- **code_snippet**:
						```python
						high_value = self.df[self.df['income'] >= income_threshold]
						```
					- **issue_type**: Data Filtering
					- **explanation**: Filtering data based on income threshold could exclude lower-income groups, leading to representation bias and potentially unfair treatment of economically disadvantaged individuals.
				- value:
					- **code_snippet**:
						```python
						male = self.df[self.df['gender'] == 'M']
						female = self.df[self.df['gender'] == 'F']
						```
					- **issue_type**: Gender Binary Reinforcement
					- **explanation**: The code reinforces a gender binary by only considering 'M' and 'F' genders, which excludes non-binary and other gender identities, leading to exclusion and misrepresentation.
				- value:
					- **code_snippet**:
						```python
						return train_test_split(self.df, test_size=test_size, stratify=self.df['education'], random_state=random_state)
						```
					- **issue_type**: Stratification Bias
					- **explanation**: Stratifying only on education level might miss other important demographic factors and their intersections, potentially leading to biased model outcomes.
				- value:
					- **code_snippet**:
						```python
						age_group = self.df[(self.df['age'] >= min_age) & (self.df['age'] < max_age)]
						```
					- **issue_type**: Age-Based Sampling
					- **explanation**: Sampling based on age groups could introduce age-based biases and ignore intersectional factors, leading to unfair treatment of certain age groups.
			- **recommendations**: 
				- Consider including a broader range of income levels to avoid excluding economically disadvantaged groups.
				- Expand gender categories to include non-binary and other gender identities to ensure inclusivity.
				- Incorporate multiple demographic factors for stratification to capture intersectional effects.
				- Ensure that age-based sampling considers intersectional factors and does not disproportionately affect certain age groups.
			- **severity**: high

---

### Fairness Analysis credit_score
_Analyze and mitigate bias for feature credit_score_

#### Parameters

#### Metrics
- **Duration**: 35.78 ms
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
- **Duration**: 16.13 ms
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
- **Duration**: 14.90 ms
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
- **Duration**: 14.26 ms
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
- **Duration**: 13.85 ms
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
- **Duration**: 97.93 ms
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
