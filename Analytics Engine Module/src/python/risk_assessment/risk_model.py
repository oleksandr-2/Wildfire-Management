from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

class RiskModel:
    def __init__(self):
        """
        Initializes the RiskModel with a Bayesian Network.
        """
        self.model = BayesianNetwork()
        self._create_structure()
        self._fit_model()

    def _create_structure(self):
        """
        Defines the structure of the Bayesian Network.
        """
        # Define the structure of the network
        self.model.add_edges_from([
            ('Weather', 'FireRisk'),
            ('FuelType', 'FireRisk'),
            ('Topography', 'FireRisk')
        ])

    def _fit_model(self):
        """
        Fits the model with sample data.
        """
        # Example data for fitting the model
        data = pd.DataFrame(data={
            'Weather': ['Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Cloudy'],
            'FuelType': ['Grass', 'Bush', 'Forest', 'Grass', 'Forest'],
            'Topography': ['Flat', 'Hilly', 'Mountainous', 'Flat', 'Mountainous'],
            'FireRisk': ['High', 'Medium', 'Low', 'High', 'Medium']
        })

        # Convert categorical data to numerical
        for column in data.columns:
            data[column] = data[column].astype('category').cat.codes

        # Fit the model
        self.model.fit(data, estimator=MaximumLikelihoodEstimator)

    def predict_risk(self, weather, fuel_type, topography):
        """
        Predicts the fire risk based on input conditions.

        :param weather: Weather condition (e.g., 'Sunny', 'Cloudy', 'Rainy')
        :param fuel_type: Type of fuel (e.g., 'Grass', 'Bush', 'Forest')
        :param topography: Topography type (e.g., 'Flat', 'Hilly', 'Mountainous')
        :return: Predicted fire risk level
        """
        # Convert inputs to numerical
        conditions = {
            'Weather': weather,
            'FuelType': fuel_type,
            'Topography': topography
        }
        for key in conditions.keys():
            conditions[key] = pd.Series([conditions[key]]).astype('category').cat.codes[0]

        # Perform inference
        inference = VariableElimination(self.model)
        result = inference.map_query(variables=['FireRisk'], evidence=conditions)
        risk_level = result['FireRisk']

        # Convert numerical result back to categorical
        risk_levels = ['Low', 'Medium', 'High']
        return risk_levels[risk_level]

# Example usage
if __name__ == "__main__":
    model = RiskModel()
    risk = model.predict_risk('Sunny', 'Forest', 'Mountainous')
    print(f"Predicted Fire Risk: {risk}")
