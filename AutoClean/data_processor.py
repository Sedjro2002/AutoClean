"""Data processing utilities for AutoClean."""
from pathlib import Path
from typing import Tuple, Optional, Dict, Any
import pandas as pd
import numpy as np
import csv
from loguru import logger
import ydata_profiling
from .config import Config
from .dim_reduction import DimensionalityReducer

class DataProcessor:
    """Handles data loading and preprocessing operations."""
    
    def __init__(self, config: Config, audit_logger: Optional[Any] = None):
        self.audit_logger = audit_logger
        self.config = config
        self._setup_dim_reduction()
        
    def _setup_dim_reduction(self):
        """Setup dimensionality reduction based on config."""
        dim_reduction_config = self.config.dataset_config.get('dim_reduction', {})
        
        if dim_reduction_config.get('enabled', False):
            self.dim_reducer = DimensionalityReducer(
                method=dim_reduction_config.get('method', 'pca'),
                n_components=dim_reduction_config.get('n_components'),
                target_explained_variance=dim_reduction_config.get('target_explained_variance', 0.95)
            )
        else:
            self.dim_reducer = None

    def get_config(self):
        return self.config
        
    def load_csv(self, file_path: str) -> pd.DataFrame:
        """Load CSV file with automatic dialect detection."""
        try:
            with open(file_path, 'r') as csv_file:
                # Read first two lines for dialect detection
                temp_lines = csv_file.readline() + '\n' + csv_file.readline()
                dialect = csv.Sniffer().sniff(temp_lines, delimiters=';,')
            
            return pd.read_csv(file_path, delimiter=dialect.delimiter)
        except Exception as e:
            logger.error(f"Error loading CSV file {file_path}: {str(e)}")
            raise
            
    def process_data(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Process the data including dimensionality reduction if enabled."""
        
        # Generate initial profile
        profile = self.generate_profile(df, "before_preprocessing")
        metadata['initial_profile'] = profile
        
        # Apply dimensionality reduction if enabled
        if self.dim_reducer is not None:
            self.audit_logger.start_operation(
                name="Dimensionality Reduction",
                description="Apply dimensionality reduction to features",
                parameters={
                    "method": self.dim_reducer.method,
                    "n_components": self.dim_reducer.n_components,
                    "target_explained_variance": self.dim_reducer.target_explained_variance
                },
                df=df
            )
            df_before = df.copy()
            metadata = {}
            # Select numerical columns for reduction
            num_cols = df.select_dtypes(include=[np.number]).columns
            if len(num_cols) > 0:
                # Store original numerical data
                original_num_data = df[num_cols].copy()
                
                # Apply dimensionality reduction
                reduced_data, reduction_metadata = self.dim_reducer.fit_transform(df[num_cols])
                
                # Create new dataframe with reduced features
                reduced_cols = [f'component_{i+1}' for i in range(reduced_data.shape[1])]
                df_reduced = pd.DataFrame(reduced_data, columns=reduced_cols, index=df.index)
                
                # Replace numerical columns with reduced features
                df = df.drop(columns=num_cols)
                df = pd.concat([df, df_reduced], axis=1)
                
                metadata['dim_reduction'] = {
                    'original_features': num_cols.tolist(),
                    'reduced_features': reduced_cols,
                    **reduction_metadata
                }
                
                # Generate profile after reduction
                profile_reduced = self.generate_profile(df, "after_reduction")
                metadata['reduced_profile'] = profile_reduced
            else:
                logger.warning("No numerical columns found for dimensionality reduction")
            
            self.audit_logger.log_dataframe_changes(
                operation="Dimensionality Reduction",
                before_df=df_before,
                after_df=df
            )

            self.audit_logger.complete_operation(
                name="Dimensionality Reduction",
                description="Apply dimensionality reduction to features",
                parameters={
                    "method": self.dim_reducer.method,
                    "n_components": self.dim_reducer.n_components,
                    "target_explained_variance": self.dim_reducer.target_explained_variance
                },
                start_time=self.audit_logger.start_time,
                input_df=df_before,
                output_df=df,
                changes_made=metadata
            )
        
        return df, metadata
            
    def generate_profile(self, df: pd.DataFrame, output_prefix: str) -> Any:
        """Generate data profile reports."""
        try:
            # Sample data if it exceeds threshold
            self.audit_logger.start_operation(
                name="Data Profiling",
                description="Generate data profile reports",
                parameters={
                    "threshold": self.config.profile_threshold,
                    "sample_size": self.config.sample_size,
                    "output_prefix": output_prefix
                },
                df=df
            )
            profile_df = df
            if df.shape[0] > self.config.profile_threshold:
                profile_df = df.sample(self.config.sample_size)
                logger.info(f"Sampling {self.config.sample_size} rows for profiling")
            
            profile = ydata_profiling.ProfileReport(
                profile_df, 
                title="Data Profile Report",
                explorative=True
            )
            
            # Save reports
            profile.to_file(self.config.output_dir / f"{output_prefix}_profile.html")
            profile.to_file(self.config.output_dir / f"{output_prefix}_profile.json")
            
            self.audit_logger.complete_operation(
                name="Data Profiling",
                description="Generate data profile reports",
                parameters={
                    "threshold": self.config.profile_threshold,
                    "sample_size": self.config.sample_size,
                    "output_prefix": output_prefix
                },
                start_time=self.audit_logger.start_time,
                input_df=df,
                output_df=profile_df,
                changes_made={}
            )
            return profile
        except Exception as e:
            logger.error(f"Error generating profile: {str(e)}")
            raise
