import logging
import json
from datetime import datetime
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

class Auditor:
    def __init__(self, audit_log_file: str):
        """
        Initialize Auditor with the path to an audit log file.
        :param audit_log_file: Path to the JSON file where audit logs will be stored.
        """
        self.audit_log_file = audit_log_file

    def _log(self, message: str) -> None:
        """
        Append a log message to the audit log file.
        :param message: Log message.
        """
        log_entry = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'message': message
        }
        try:
            with open(self.audit_log_file, 'a') as file:
                json.dump(log_entry, file)
                file.write('\n')
            logging.info("Audit log entry added")
        except Exception as e:
            logging.error(f"Failed to write audit log: {e}")

    def log_validation_result(self, data: Dict[str, Any], is_valid: bool) -> None:
        """
        Log the result of data validation.
        :param data: Data that was validated.
        :param is_valid: Boolean indicating if the data was valid or not.
        """
        message = f"Data validation result: {'Valid' if is_valid else 'Invalid'}, Data: {data}"
        self._log(message)

# Example usage
if __name__ == "__main__":
    auditor = Auditor('audit_log.json')
    
    # Example data and validation result
    data = {
        'id': 'sensor_123',
        'timestamp': '2024-08-08T12:34:56Z',
        'value': 23.5
    }
    
    is_valid = True  # Example result from validation
    
    # Log validation result
    auditor.log_validation_result(data, is_valid)
