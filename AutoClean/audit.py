"""Audit module for tracking and logging AutoClean operations."""
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any, Optional
import json
from datetime import datetime
import pandas as pd
from loguru import logger

@dataclass
class OperationMetrics:
    """Metrics for a single operation."""
    start_time: str
    end_time: str
    duration_seconds: float
    input_shape: tuple
    output_shape: tuple
    changes_made: Dict[str, Any]
    success: bool
    error: Optional[str] = None

@dataclass
class OperationAudit:
    """Audit information for a single operation."""
    operation_name: str
    description: str
    parameters: Dict[str, Any]
    metrics: OperationMetrics
    warnings: List[str] = field(default_factory=list)
    
@dataclass
class AutoCleanAudit:
    """Complete audit trail for AutoClean process."""
    start_time: str
    input_file: str | None = None
    configuration: Dict[str, Any] | None = field(default_factory=dict)
    operations: List[OperationAudit] = field(default_factory=list)
    end_time: Optional[str] = None
    total_duration_seconds: Optional[float] = None
    final_metrics: Dict[str, Any] = field(default_factory=dict)
    
    def add_operation(self, operation: OperationAudit):
        """Add an operation to the audit trail."""
        self.operations.append(operation)
        
    def complete_audit(self):
        """Complete the audit with final metrics."""
        self.end_time = datetime.now().isoformat()
        start = datetime.fromisoformat(self.start_time)
        end = datetime.fromisoformat(self.end_time)
        self.total_duration_seconds = (end - start).total_seconds()
        
        # Calculate final metrics
        total_operations = len(self.operations)
        successful_operations = sum(1 for op in self.operations if op.metrics.success)
        
        self.final_metrics = {
            "total_operations": total_operations,
            "successful_operations": successful_operations,
            "success_rate": successful_operations / total_operations if total_operations > 0 else 0,
            "total_warnings": sum(len(op.warnings) for op in self.operations),
            "operations_with_errors": [op.operation_name for op in self.operations if not op.metrics.success]
        }
        
    def save(self, filepath: str):
        """Save audit trail to JSON file."""
        self.complete_audit()
        with open(filepath, 'w') as f:
            json.dump(asdict(self), f, indent=2)
            
class AuditLogger:
    """Logger for AutoClean operations with detailed metrics."""
    
    def __init__(self, audit: AutoCleanAudit):
        self.audit = audit
        
    def start_operation(self, name: str, description: str, parameters: Dict[str, Any], df: pd.DataFrame) -> datetime:
        """Start logging an operation."""
        start_time = datetime.now()
        
        logger.info(f"Starting operation: {name}")
        logger.info(f"Description: {description}")
        logger.info(f"Parameters: {parameters}")
        logger.info(f"Input shape: {df.shape}")
        
        return start_time
        
    def complete_operation(
        self,
        name: str,
        description: str,
        parameters: Dict[str, Any],
        start_time: datetime,
        input_df: pd.DataFrame,
        output_df: pd.DataFrame,
        changes_made: Dict[str, Any],
        warnings: List[str] = None,
        error: str = None
    ):
        """Complete logging an operation and add it to audit trail."""
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        success = error is None
        
        # Log completion
        if success:
            logger.info(f"Completed operation: {name}")
        else:
            logger.error(f"Operation failed: {name}")
            logger.error(f"Error: {error}")
            
        logger.info(f"Duration: {duration:.4f} seconds")
        logger.info(f"Output shape: {output_df.shape}")
        
        # Log changes
        for change_type, details in changes_made.items():
            logger.info(f"{change_type}: {details}")
            
        # Log warnings
        if warnings:
            for warning in warnings:
                logger.warning(warning)
                
        # Create operation metrics
        metrics = OperationMetrics(
            start_time=start_time.isoformat(),
            end_time=end_time.isoformat(),
            duration_seconds=duration,
            input_shape=input_df.shape,
            output_shape=output_df.shape,
            changes_made=changes_made,
            success=success,
            error=error
        )
        
        # Create and add operation audit
        operation = OperationAudit(
            operation_name=name,
            description=description,
            parameters=parameters,
            metrics=metrics,
            warnings=warnings or []
        )
        
        self.audit.add_operation(operation)
        
    def log_dataframe_changes(
        self,
        operation: str,
        before_df: pd.DataFrame,
        after_df: pd.DataFrame
    ) -> Dict[str, Any]:
        """Log detailed changes in DataFrame before and after an operation."""
        changes = {}
        
        # Column changes
        added_cols = set(after_df.columns) - set(before_df.columns)
        removed_cols = set(before_df.columns) - set(after_df.columns)
        if added_cols:
            changes["added_columns"] = list(added_cols)
        if removed_cols:
            changes["removed_columns"] = list(removed_cols)
            
        # Data type changes
        dtype_changes = {}
        common_cols = set(before_df.columns) & set(after_df.columns)
        for col in common_cols:
            if before_df[col].dtype != after_df[col].dtype:
                dtype_changes[col] = {
                    "before": str(before_df[col].dtype),
                    "after": str(after_df[col].dtype)
                }
        if dtype_changes:
            changes["dtype_changes"] = dtype_changes
            
        # Missing values changes
        before_missing = before_df.isnull().sum().sum()
        after_missing = after_df.isnull().sum().sum()
        if before_missing != after_missing:
            changes["missing_values"] = {
                "before": int(before_missing),
                "after": int(after_missing),
                "difference": int(before_missing - after_missing)
            }
            
        # Row count changes
        if len(before_df) != len(after_df):
            changes["row_count"] = {
                "before": len(before_df),
                "after": len(after_df),
                "difference": len(before_df) - len(after_df)
            }
            
        # Column statistics changes
        numeric_cols = before_df.select_dtypes(include=['int64', 'float64']).columns
        stats_changes = {}
        for col in numeric_cols:
            if col in after_df.columns:
                before_stats = before_df[col].describe()
                after_stats = after_df[col].describe()
                if not before_stats.equals(after_stats):
                    stats_changes[col] = {
                        "mean_change": float(after_stats['mean'] - before_stats['mean']),
                        "std_change": float(after_stats['std'] - before_stats['std']),
                        "min_change": float(after_stats['min'] - before_stats['min']),
                        "max_change": float(after_stats['max'] - before_stats['max'])
                    }
        if stats_changes:
            changes["statistics_changes"] = stats_changes
            
        return changes
