import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load dataset
def load_data(file_path):
    logger.info("Loading data from %s", file_path)
    if not os.path.exists(file_path):
        logger.error("Data file not found: %s", file_path)
        raise FileNotFoundError(f"Data file not found: {file_path}")
    data = pd.read_csv(file_path)
    return data

# Preprocess data
def preprocess_data(data):
    logger.info("Preprocessing data")
    # Assume the last column is the target variable (fire spread)
    X = data.iloc[:, :-1].values  # Features
    y = data.iloc[:, -1].values    # Target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

# Build the model
def build_model(input_shape):
    logger.info("Building the model")
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1)  # Output layer for regression
    ])

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    return model

# Train the model
def train_model(model, X_train, y_train, epochs=100, batch_size=32):
    logger.info("Training the model")
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    return history

# Save the model
def save_model(model, model_path):
    logger.info("Saving the model to %s", model_path)
    model.save(model_path)

def main():
    # File paths
    data_file_path = 'data/fire_spread_data.csv'  # Update with your actual data path
    model_save_path = 'models/fire_spread_nn.h5'

    # Load and preprocess data
    data = load_data(data_file_path)
    X_train, X_test, y_train, y_test = preprocess_data(data)

    # Build and train the model
    model = build_model(X_train.shape[1])
    train_model(model, X_train, y_train)

    # Save the trained model
    save_model(model, model_save_path)

    # Evaluate the model
    logger.info("Evaluating the model")
    test_loss, test_mae = model.evaluate(X_test, y_test)
    logger.info("Test MAE: %.3f", test_mae)

if __name__ == '__main__':
    main()
