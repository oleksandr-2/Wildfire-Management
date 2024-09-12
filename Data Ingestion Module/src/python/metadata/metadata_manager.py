import logging
import json
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

class MetadataManager:
    def __init__(self, metadata_file: str):
        """
        Initialize MetadataManager with the path to a metadata file.
        :param metadata_file: Path to the JSON file where metadata will be stored.
        """
        self.metadata_file = metadata_file
        self.metadata = self._load_metadata()

    def _load_metadata(self) -> Dict[str, Any]:
        """
        Load metadata from the JSON file.
        :return: Dictionary containing metadata.
        """
        try:
            with open(self.metadata_file, 'r') as file:
                metadata = json.load(file)
            logging.info("Metadata loaded successfully")
            return metadata
        except FileNotFoundError:
            logging.warning(f"Metadata file {self.metadata_file} not found. Creating a new one.")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode metadata JSON: {e}")
            return {}

    def _save_metadata(self) -> None:
        """
        Save metadata to the JSON file.
        """
        try:
            with open(self.metadata_file, 'w') as file:
                json.dump(self.metadata, file, indent=4)
            logging.info("Metadata saved successfully")
        except Exception as e:
            logging.error(f"Failed to save metadata: {e}")

    def add_metadata(self, key: str, value: Any) -> None:
        """
        Add or update metadata.
        :param key: Metadata key.
        :param value: Metadata value.
        """
        self.metadata[key] = value
        self._save_metadata()
        logging.info(f"Metadata added/updated: {key} = {value}")

    def get_metadata(self, key: str) -> Any:
        """
        Retrieve metadata by key.
        :param key: Metadata key.
        :return: Metadata value or None if the key does not exist.
        """
        return self.metadata.get(key, None)

    def delete_metadata(self, key: str) -> None:
        """
        Delete metadata by key.
        :param key: Metadata key.
        """
        if key in self.metadata:
            del self.metadata[key]
            self._save_metadata()
            logging.info(f"Metadata deleted: {key}")
        else:
            logging.warning(f"Metadata key {key} not found")

# Example usage
if __name__ == "__main__":
    metadata_file = 'metadata.json'
    manager = MetadataManager(metadata_file)

    # Add or update metadata
    manager.add_metadata('last_updated', '2024-08-08')
    manager.add_metadata('version', '1.0.0')

    # Retrieve metadata
    last_updated = manager.get_metadata('last_updated')
    print(f"Last updated: {last_updated}")

    # Delete metadata
    manager.delete_metadata('version')
