"""Data sampling module."""
import pandas as pd
import numpy as np
from typing import List, Optional
from sklearn.model_selection import train_test_split

class DataSampler:
    """Handles data sampling operations."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        
    def sample_high_value_customers(
        self,
        income_threshold: float = 100000,
        sample_size: Optional[int] = None
    ) -> pd.DataFrame:
        """Sample customers with high income.
        
        Note: Focusing on high-income customers could create or amplify
        representation biases in the dataset.
        """
        high_value = self.df[self.df['income'] >= income_threshold]
        if sample_size and len(high_value) > sample_size:
            return high_value.sample(n=sample_size)
        return high_value
    
    def balanced_gender_sample(self, sample_size: int) -> pd.DataFrame:
        """Create a gender-balanced sample.
        
        Note: While attempting to balance gender, this approach:
        1. Reinforces gender binary
        2. May not account for intersectional factors
        """
        male = self.df[self.df['gender'] == 'M']
        female = self.df[self.df['gender'] == 'F']
        
        size_per_group = sample_size // 2
        
        sampled = pd.concat([
            male.sample(n=size_per_group, replace=True),
            female.sample(n=size_per_group, replace=True)
        ])
        
        return sampled
    
    def stratified_education_split(
        self,
        test_size: float = 0.2,
        random_state: Optional[int] = None
    ) -> tuple:
        """Create a stratified split based on education level.
        
        Note: Stratifying only on education level might miss other important
        demographic factors and their intersections.
        """
        return train_test_split(
            self.df,
            test_size=test_size,
            stratify=self.df['education'],
            random_state=random_state
        )
    
    def sample_by_age_group(self, group_sizes: dict) -> pd.DataFrame:
        """Sample specific sizes from different age groups.
        
        Note: This type of demographic-based sampling could introduce
        age-based biases and ignore intersectional factors.
        """
        samples = []
        for age_range, size in group_sizes.items():
            min_age, max_age = age_range
            age_group = self.df[
                (self.df['age'] >= min_age) &
                (self.df['age'] < max_age)
            ]
            if len(age_group) > 0:
                samples.append(
                    age_group.sample(
                        n=min(size, len(age_group)),
                        replace=True
                    )
                )
        
        return pd.concat(samples, ignore_index=True)
