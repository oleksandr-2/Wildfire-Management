import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

class ResourceAllocationRF:
    def __init__(self, n_estimators=100, max_depth=None):
        """
        Initializes the Random Forest model.

        :param n_estimators: Number of trees in the forest
        :param max_depth: Maximum depth of the tree
        """
        self.model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)

    def train(self, X_train, y_train):
        """
        Trains the model.

        :param X_train: Training features
        :param y_train: Training labels
        """
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        """
        Evaluates the model on test data.

        :param X_test: Test features
        :param y_test: Test labels
        :return: Accuracy score
        """
        y_pred = self.model.predict(X_test)
        return accuracy_score(y_test, y_pred)

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
    # df = pd.read_csv('resource_allocation_data.csv')
    # X = df.drop('target', axis=1).values
    # y = df['target'].values

    # Placeholder for actual data loading
    X = np.random.rand(1000, 10)
    y = np.random.randint(0, 2, size=(1000,))

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize and train model
    model = ResourceAllocationRF(n_estimators=100, max_depth=10)
    model.train(X_train, y_train)

    # Evaluate model
    accuracy = model.evaluate(X_test, y_test)
    print(f'Test Accuracy: {accuracy}')
