import logging
from pydantic import BaseModel, ValidationError, constr
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

class DataSchema(BaseModel):
    """
    Example schema for validating incoming data.
    Customize this schema based on your data requirements.
    """
    id: constr(regex=r'^[a-zA-Z0-9_-]{1,50}$')
    timestamp: str
    value: float

class Validator:
    def __init__(self):
        self.schema = DataSchema

    def validate(self, data: Dict[str, Any]) -> bool:
        """
        Validate data against the schema.
        :param data: Dictionary containing data to be validated.
        :return: True if data is valid, False otherwise.
        """
        try:
            self.schema(**data)
            logging.info("Data validation succeeded")
            return True
        except ValidationError as e:
            logging.error(f"Data validation failed: {e}")
            return False

# Example usage
if __name__ == "__main__":
    validator = Validator()
    
    # Example data
    valid_data = {
        'id': 'sensor_123',
        'timestamp': '2024-08-08T12:34:56Z',
        'value': 23.5
    }
    
    invalid_data = {
        'id': 'sensor_123',
        'timestamp': '2024-08-08T12:34:56Z',
        'value': 'invalid_value'
    }

    # Validate data
    print(f"Valid data: {validator.validate(valid_data)}")
    print(f"Invalid data: {validator.validate(invalid_data)}")
