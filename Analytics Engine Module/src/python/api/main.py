from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
import numpy as np
import json
from fire_spread_nn import FireSpreadNN
from resource_allocation_rf import ResourceAllocationRF

# Initialize FastAPI app
app = FastAPI()

# Load or initialize models (placeholders)
fire_spread_model = FireSpreadNN(input_shape=10, num_classes=2)  # Example initialization
resource_allocation_model = ResourceAllocationRF(n_estimators=100, max_depth=10)  # Example initialization

# Example dummy data for models (replace with real model loading)
def load_dummy_data():
    np.random.seed(0)
    X = np.random.rand(100, 10)  # Example feature set
    y = np.random.randint(0, 2, size=(100,))  # Example labels
    return X, y

X_dummy, y_dummy = load_dummy_data()
fire_spread_model.train(X_dummy, y_dummy)
resource_allocation_model.train(X_dummy, y_dummy)

# Define data models
class PredictionRequest(BaseModel):
    features: List[float]

class ClassificationRequest(BaseModel):
    features: List[float]

# Define endpoints

@app.get("/")
def read_root():
    return {"message": "Welcome to the Analytics Engine API"}

@app.post("/predict/fire_spread")
def predict_fire_spread(request: PredictionRequest):
    features = np.array(request.features).reshape(1, -1)
    prediction = fire_spread_model.predict(features)
    return {"prediction": prediction.tolist()}

@app.post("/predict/resource_allocation")
def predict_resource_allocation(request: ClassificationRequest):
    features = np.array(request.features).reshape(1, -1)
    prediction = resource_allocation_model.predict(features)
    return {"prediction": prediction.tolist()}

@app.get("/status")
def get_status():
    return {"status": "API is up and running"}

# Error handling
@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    return {"error": str(exc.detail)}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
