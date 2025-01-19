"""Normalization module for AutoClean."""
from typing import List, Dict, Any, Optional
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from loguru import logger

class DataNormalizer:
    """Handles data normalization using different methods.
    
    Attributes:
        SCALER_MAP: Mapping of supported normalization methods to their scaler classes
        method: The normalization method to use
        exclude_features: List of features to exclude from normalization
        scaler: The instantiated scaler object
        feature_stats: Dictionary storing feature statistics from normalization
    """
    
    SCALER_MAP = {
        'standard': StandardScaler,
        'minmax': MinMaxScaler,
        'robust': RobustScaler
    }
    
    def __init__(
        self,
        method: str = 'standard',
        exclude_features: Optional[List[str]] = None
    ):
        """Initialize the normalizer.
        
        Args:
            method: Normalization method ('standard', 'minmax', or 'robust')
            exclude_features: List of features to exclude from normalization
            
        Raises:
            TypeError: If method is not a string or exclude_features contains non-string values
            ValueError: If method is invalid or exclude_features contains invalid column names
        """
        if not isinstance(method, str):
            raise TypeError(f"method must be a string, got {type(method)}")
            
        self.method = method.lower()
        
        if exclude_features is not None:
            if not isinstance(exclude_features, list):
                raise TypeError(f"exclude_features must be a list, got {type(exclude_features)}")
            if not all(isinstance(f, str) for f in exclude_features):
                raise TypeError("All exclude_features must be strings")
                
        self.exclude_features = exclude_features or []
        
        if self.method not in self.SCALER_MAP:
            raise ValueError(f"Unknown normalization method: {method}. Must be one of: {list(self.SCALER_MAP.keys())}")
            
        self.scaler = self.SCALER_MAP[self.method]()
        self.feature_stats = {}
        
    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fit the normalizer and transform the data.
        
        Args:
            df: Input DataFrame to normalize
            
        Returns:
            Normalized DataFrame
            
        Raises:
            ValueError: If DataFrame is empty or contains invalid columns
        """
        if df.empty:
            raise ValueError("Input DataFrame cannot be empty")
            
        # Select features to normalize
        features_to_normalize = [col for col in df.columns 
                               if col not in self.exclude_features]
        
        if not features_to_normalize:
            logger.warning("No features selected for normalization")
            return df
            
        # Validate columns exist
        invalid_cols = [col for col in self.exclude_features if col not in df.columns]
        if invalid_cols:
            raise ValueError(f"Invalid columns in exclude_features: {invalid_cols}")
            
        # Store original data for excluded features
        excluded_data = df[self.exclude_features].copy() if self.exclude_features else None
        
        # Fit and transform selected features
        try:
            normalized_data = self.scaler.fit_transform(df[features_to_normalize])
        except Exception as e:
            raise ValueError(f"Error during normalization: {str(e)}")
        
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
        """Transform new data using the fitted normalizer.
        
        Args:
            df: Input DataFrame to transform
            
        Returns:
            Transformed DataFrame
            
        Raises:
            ValueError: If normalizer not fitted or DataFrame contains invalid columns
        """
        if not hasattr(self.scaler, 'mean_'):
            raise ValueError("Normalizer not fitted yet")
            
        # Select features to normalize
        features_to_normalize = [col for col in df.columns 
                               if col not in self.exclude_features]
                               
        if not features_to_normalize:
            return df
            
        # Validate columns exist
        invalid_cols = [col for col in self.exclude_features if col not in df.columns]
        if invalid_cols:
            raise ValueError(f"Invalid columns in exclude_features: {invalid_cols}")
            
        # Store original data for excluded features
        excluded_data = df[self.exclude_features].copy() if self.exclude_features else None
        
        # Transform selected features
        try:
            normalized_data = self.scaler.transform(df[features_to_normalize])
        except Exception as e:
            raise ValueError(f"Error during transformation: {str(e)}")
        
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
