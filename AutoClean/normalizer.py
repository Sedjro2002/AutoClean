"""Normalization module for AutoClean."""
from typing import List, Dict, Any
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from loguru import logger

class DataNormalizer:
    """Handles data normalization using different methods."""
    
    SCALER_MAP = {
        'standard': StandardScaler,
        'minmax': MinMaxScaler,
        'robust': RobustScaler
    }
    
    def __init__(
        self,
        method: str = 'standard',
        exclude_features: List[str] = None
    ):
        """Initialize the normalizer.
        
        Args:
            method: Normalization method ('standard', 'minmax', or 'robust')
            exclude_features: List of features to exclude from normalization
        """
        self.method = method.lower()
        self.exclude_features = exclude_features or []
        
        if self.method not in self.SCALER_MAP:
            raise ValueError(f"Unknown normalization method: {method}")
            
        self.scaler = self.SCALER_MAP[self.method]()
        self.feature_stats = {}
        
    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fit the normalizer and transform the data.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Normalized DataFrame
        """
        # Select features to normalize
        features_to_normalize = [col for col in df.columns 
                               if col not in self.exclude_features]
        
        if not features_to_normalize:
            logger.warning("No features selected for normalization")
            return df
            
        # Store original data for excluded features
        excluded_data = df[self.exclude_features].copy() if self.exclude_features else None
        
        # Fit and transform selected features
        normalized_data = self.scaler.fit_transform(df[features_to_normalize])
        
        # Store feature statistics
        if isinstance(self.scaler, StandardScaler):
            self.feature_stats = {
                'mean': dict(zip(features_to_normalize, self.scaler.mean_)),
                'std': dict(zip(features_to_normalize, self.scaler.scale_))
            }
        elif isinstance(self.scaler, MinMaxScaler):
            self.feature_stats = {
                'min': dict(zip(features_to_normalize, self.scaler.min_)),
                'scale': dict(zip(features_to_normalize, self.scaler.scale_))
            }
        elif isinstance(self.scaler, RobustScaler):
            self.feature_stats = {
                'center': dict(zip(features_to_normalize, self.scaler.center_)),
                'scale': dict(zip(features_to_normalize, self.scaler.scale_))
            }
            
        # Create normalized DataFrame
        normalized_df = pd.DataFrame(
            normalized_data,
            columns=features_to_normalize,
            index=df.index
        )
        
        # Add back excluded features
        if excluded_data is not None:
            normalized_df = pd.concat([normalized_df, excluded_data], axis=1)
            
        logger.info(f"Normalized {len(features_to_normalize)} features using {self.method} scaling")
        for stat_name, stat_dict in self.feature_stats.items():
            logger.debug(f"Feature {stat_name}s: {stat_dict}")
            
        return normalized_df
        
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform new data using the fitted normalizer."""
        if not hasattr(self.scaler, 'mean_'):
            raise ValueError("Normalizer not fitted yet")
            
        # Select features to normalize
        features_to_normalize = [col for col in df.columns 
                               if col not in self.exclude_features]
                               
        if not features_to_normalize:
            return df
            
        # Store original data for excluded features
        excluded_data = df[self.exclude_features].copy() if self.exclude_features else None
        
        # Transform selected features
        normalized_data = self.scaler.transform(df[features_to_normalize])
        
        # Create normalized DataFrame
        normalized_df = pd.DataFrame(
            normalized_data,
            columns=features_to_normalize,
            index=df.index
        )
        
        # Add back excluded features
        if excluded_data is not None:
            normalized_df = pd.concat([normalized_df, excluded_data], axis=1)
            
        return normalized_df
