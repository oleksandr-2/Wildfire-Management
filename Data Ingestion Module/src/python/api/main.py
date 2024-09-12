from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn

# Initialize FastAPI app
app = FastAPI()

class DataIngestionRequest(BaseModel):
    """
    Schema for the data ingestion request.
    Customize this schema based on your data requirements.
    """
    id: str
    timestamp: str
    value: float

# In-memory storage (for demonstration purposes)
data_store: Dict[str, Any] = {}

@app.post("/ingest/")
async def ingest_data(request: DataIngestionRequest):
    """
    Endpoint for ingesting data into the system.
    :param request: DataIngestionRequest object containing the data to be ingested.
    :return: Confirmation message.
    """
    data_id = request.id
    if data_id in data_store:
        raise HTTPException(status_code=400, detail="Data with this ID already exists.")
    
    # Store the data (in a real system, this would involve more complex operations)
    data_store[data_id] = request.dict()
    
    return {"message": "Data ingested successfully", "data": data_store[data_id]}

@app.get("/data/{data_id}")
async def get_data(data_id: str):
    """
    Endpoint for retrieving ingested data by ID.
    :param data_id: ID of the data to retrieve.
    :return: Data associated with the given ID.
    """
    if data_id not in data_store:
        raise HTTPException(status_code=404, detail="Data not found.")
    
    return {"data": data_store[data_id]}

@app.delete("/data/{data_id}")
async def delete_data(data_id: str):
    """
    Endpoint for deleting ingested data by ID.
    :param data_id: ID of the data to delete.
    :return: Confirmation message.
    """
    if data_id not in data_store:
        raise HTTPException(status_code=404, detail="Data not found.")
    
    del data_store[data_id]
    
    return {"message": "Data deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
