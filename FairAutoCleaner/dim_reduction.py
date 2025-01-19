"""Dimensionality reduction module for AutoClean."""
from typing import Optional, Tuple, Union
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
import tensorflow as tf
from loguru import logger

class AutoEncoder(keras.Model):
    """Autoencoder implementation using Keras."""
    
    def __init__(self, input_dim: int, encoding_dim: int):
        """Initialize the autoencoder.
        
        Args:
            input_dim: Number of input features
            encoding_dim: Dimension of the encoded representation
        """
        super().__init__()
        
        # Encoder
        self.encoder = keras.Sequential([
            keras.layers.Dense(input_dim, activation='relu'),
            keras.layers.Dense(encoding_dim * 2, activation='relu'),
            keras.layers.Dense(encoding_dim, activation='relu')
        ])
        
        # Decoder
        self.decoder = keras.Sequential([
            keras.layers.Dense(encoding_dim * 2, activation='relu'),
            keras.layers.Dense(input_dim * 2, activation='relu'),
            keras.layers.Dense(input_dim, activation='linear')
        ])
        
    def call(self, x: tf.Tensor) -> tf.Tensor:
        """Forward pass through the autoencoder."""
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
        
    def encode(self, x: tf.Tensor) -> tf.Tensor:
        """Encode input data."""
        return self.encoder(x)

class DimensionalityReducer:
    """Handles dimensionality reduction using different algorithms."""
    
    def __init__(
        self,
        method: str = 'pca',
        n_components: Optional[int] = None,
        target_explained_variance: float = 0.95
    ):
        """Initialize the dimensionality reducer.
        
        Args:
            method: Reduction method ('pca' or 'autoencoder')
            n_components: Number of components to keep. If None, use target_explained_variance.
            target_explained_variance: Target explained variance ratio (for PCA only)
        """
        self.method = method.lower()
        self.n_components = n_components
        self.target_explained_variance = target_explained_variance
        self.model = None
        self.scaler = StandardScaler()
        
    def fit_transform(self, X: pd.DataFrame) -> Tuple[np.ndarray, dict]:
        """Fit the reducer and transform the data.
        
        Args:
            X: Input DataFrame
            
        Returns:
            Tuple of (transformed data, metadata)
        """
        # Scale the data
        X_scaled = self.scaler.fit_transform(X)
        
        if self.method == 'pca':
            return self._fit_transform_pca(X_scaled)
        elif self.method == 'autoencoder':
            return self._fit_transform_autoencoder(X_scaled)
        else:
            raise ValueError(f"Unknown method: {self.method}")
            
    def transform(self, X: pd.DataFrame) -> np.ndarray:
        """Transform new data using the fitted reducer."""
        if self.model is None:
            raise ValueError("Model not fitted yet")
            
        X_scaled = self.scaler.transform(X)
        
        if self.method == 'pca':
            return self.model.transform(X_scaled)
        else:
            return self.model.encode(X_scaled)
            
    def _fit_transform_pca(self, X_scaled: np.ndarray) -> Tuple[np.ndarray, dict]:
        """Fit and transform using PCA."""
        # Determine number of components
        if self.n_components is None:
            # Find number of components needed to explain target variance
            temp_pca = PCA()
            temp_pca.fit(X_scaled)
            cumsum = np.cumsum(temp_pca.explained_variance_ratio_)
            self.n_components = np.argmax(cumsum >= self.target_explained_variance) + 1
            
        # Fit PCA
        self.model = PCA(n_components=self.n_components)
        transformed = self.model.fit_transform(X_scaled)
        
        metadata = {
            'explained_variance_ratio': [float(v) for v in self.model.explained_variance_ratio_],
            'n_components': int(self.n_components),
            'total_variance_explained': float(sum(self.model.explained_variance_ratio_))
        }
        
        logger.info(f"PCA reduced dimensions from {X_scaled.shape[1]} to {self.n_components}")
        logger.info(f"Total variance explained: {metadata['total_variance_explained']:.4f}")
        
        return transformed, metadata
        
    def _fit_transform_autoencoder(self, X_scaled: np.ndarray) -> Tuple[np.ndarray, dict]:
        """Fit and transform using Autoencoder."""
        input_dim = X_scaled.shape[1]
        encoding_dim = self.n_components or max(1, input_dim // 2)
        
        # Create and compile autoencoder
        self.model = AutoEncoder(input_dim, encoding_dim)
        self.model.compile(optimizer='adam', loss='mse')
        
        # Convert to tensor
        X_tensor = tf.convert_to_tensor(X_scaled, dtype=tf.float32)
        
        # Train autoencoder
        history = self.model.fit(
            X_tensor, X_tensor,
            epochs=50,
            batch_size=32,
            validation_split=0.2,
            verbose=0
        )
        
        # Get encoded representation
        transformed = self.model.encode(X_tensor).numpy()
        
        metadata = {
            'encoding_dim': encoding_dim,
            'final_loss': float(history.history['loss'][-1]),
            'final_val_loss': float(history.history['val_loss'][-1])
        }
        
        logger.info(f"Autoencoder reduced dimensions from {input_dim} to {encoding_dim}")
        logger.info(f"Final training loss: {metadata['final_loss']:.4f}")
        logger.info(f"Final validation loss: {metadata['final_val_loss']:.4f}")
        
        return transformed, metadata
