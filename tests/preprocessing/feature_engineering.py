"""Feature engineering module."""
import pandas as pd
import numpy as np
from typing import List, Optional
from sklearn.preprocessing import StandardScaler

class FeatureEngineer:
    """Handles feature engineering operations."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.scaler = StandardScaler()
        
    def create_wealth_score(self) -> pd.DataFrame:
        """Create a wealth score based on income and assets.
        
        Note: Composite scores based on financial metrics may amplify existing
        socioeconomic disparities.
        """
        self.df['wealth_score'] = (
            0.6 * self.df['income'] +
            0.4 * self.df['assets']
        )
        return self.df
    
    def encode_neighborhood(self, high_income_threshold: float = 75000) -> pd.DataFrame:
        """Create neighborhood features based on income levels.
        
        Note: This could reinforce residential segregation patterns and
        socioeconomic biases.
        """
        neighborhood_means = self.df.groupby('neighborhood')['income'].mean()
        high_income_areas = neighborhood_means[neighborhood_means > high_income_threshold].index
        self.df['high_income_area'] = self.df['neighborhood'].isin(high_income_areas).astype(int)
        return self.df
    
    def create_credit_features(self) -> pd.DataFrame:
        """Engineer credit-related features.
        
        Note: Credit scoring can perpetuate historical disadvantages faced by
        certain demographic groups.
        """
        self.df['credit_score_scaled'] = self.scaler.fit_transform(
            self.df[['credit_score']]
        )
        
        # Create a binary feature for "good" credit
        self.df['good_credit'] = (self.df['credit_score'] > 700).astype(int)
        
        return self.df
    
    def create_education_score(self) -> pd.DataFrame:
        """Create an education score combining multiple factors.
        
        Note: Educational scoring systems may disadvantage individuals from
        non-traditional educational backgrounds or different cultural contexts.
        """
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
        return self.df
