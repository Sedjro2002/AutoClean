"""Data cleaning and preprocessing module."""
import pandas as pd
import numpy as np
from typing import List, Optional

class DataCleaner:
    """Handles data cleaning and preprocessing operations."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        
    def remove_outliers_by_income(self, threshold: float = 100000) -> pd.DataFrame:
        """Remove records where income is above a threshold.
        
        Note: This could introduce bias by disproportionately excluding certain demographics.
        """
        return self.df[self.df['income'] <= threshold]
    
    def impute_missing_values(self, strategy: str = 'mean') -> pd.DataFrame:
        """Impute missing values using specified strategy.
        
        Args:
            strategy: One of 'mean', 'median', 'mode'
        """
        for column in self.df.select_dtypes(include=[np.number]):
            if strategy == 'mean':
                self.df[column].fillna(self.df[column].mean(), inplace=True)
            elif strategy == 'median':
                self.df[column].fillna(self.df[column].median(), inplace=True)
            
        return self.df
    
    def encode_gender(self) -> pd.DataFrame:
        """Encode gender column to numeric values.
        
        Note: Binary encoding of gender may reinforce gender binary assumptions
        and exclude non-binary individuals.
        """
        gender_map = {'M': 1, 'F': 0}
        self.df['gender'] = self.df['gender'].map(gender_map)
        return self.df
    
    def reduce_females(self, ratio: float = 0.5) -> pd.DataFrame:
        """Reduce the number of females in the dataset.
        
        """
        num_females = int(self.df[self.df['gender'] == 0].shape[0] * ratio)
        return self.df[self.df['gender'] == 0].sample(num_females, random_state=42)
    
    def filter_by_age(self, min_age: int = 18, max_age: int = 65) -> pd.DataFrame:
        """Filter dataset by age range.
        
        Note: Age filtering could introduce age-based discrimination.
        """
        return self.df[(self.df['age'] >= min_age) & (self.df['age'] <= max_age)]
    
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
