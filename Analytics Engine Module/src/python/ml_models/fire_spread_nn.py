import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

class FireSpreadNN:
    def __init__(self, input_shape, num_classes):
        """
        Initializes the FireSpreadNN model.

        :param input_shape: Shape of the input features
        :param num_classes: Number of output classes
        """
        self.model = self._build_model(input_shape, num_classes)

    def _build_model(self, input_shape, num_classes):
        """
        Builds a neural network model.

        :param input_shape: Shape of the input features
        :param num_classes: Number of output classes
        :return: Compiled Keras model
        """
        model = Sequential([
            Dense(64, activation='relu', input_shape=(input_shape,)),
            Dropout(0.5),
            Dense(64, activation='relu'),
            Dropout(0.5),
            Dense(num_classes, activation='softmax')
        ])

        model.compile(optimizer=Adam(), 
                      loss='categorical_crossentropy', 
                      metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, X_val, y_val, epochs=10, batch_size=32):
        """
        Trains the model.

        :param X_train: Training features
        :param y_train: Training labels
        :param X_val: Validation features
        :param y_val: Validation labels
        :param epochs: Number of epochs
        :param batch_size: Batch size
        """
        self.model.fit(X_train, y_train, 
                       validation_data=(X_val, y_val),
                       epochs=epochs, 
                       batch_size=batch_size)

    def evaluate(self, X_test, y_test):
        """
        Evaluates the model on test data.

        :param X_test: Test features
        :param y_test: Test labels
        :return: Test loss and accuracy
        """
        return self.model.evaluate(X_test, y_test)

    def predict(self, X):
        """
        Makes predictions using the trained model.

        :param X: Input features
        :return: Predictions
        """
        return self.model.predict(X)

# Example usage
if __name__ == "__main__":
    # Load your dataset here
    # df = pd.read_csv('fire_spread_data.csv')
    # X = df.drop('target', axis=1).values
    # y = pd.get_dummies(df['target']).values

    # Placeholder for actual data loading
    X = np.random.rand(1000, 10)
    y = np.random.randint(0, 2, size=(1000, 1))
    y = tf.keras.utils.to_categorical(y)

    # Split data
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # Initialize and train model
    model = FireSpreadNN(input_shape=X_train.shape[1], num_classes=y_train.shape[1])
    model.train(X_train, y_train, X_val, y_val, epochs=10, batch_size=32)

    # Evaluate model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')
