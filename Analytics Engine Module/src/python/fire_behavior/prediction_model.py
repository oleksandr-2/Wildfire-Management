import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

class FireBehaviorPredictionModel:
    def __init__(self):
        self.model = self._build_model()
    
    def _build_model(self):
        model = Sequential([
            Dense(64, activation='relu', input_shape=(10,)),  # Example input shape
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')  # Example output
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, filepath):
        self.model.save(filepath)

    def load(self, filepath):
        self.model = tf.keras.models.load_model(filepath)

# Example usage
if __name__ == "__main__":
    # Example data
    X_train = np.random.rand(100, 10)  # 100 samples with 10 features
    y_train = np.random.randint(2, size=100)  # Binary classification

    model = FireBehaviorPredictionModel()
    model.train(X_train, y_train)
    predictions = model.predict(X_train)
    print(predictions)
