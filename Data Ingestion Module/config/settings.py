import os
from pathlib import Path
import configparser

class Settings:
    def __init__(self):
        # Define the path to the configuration file
        self.config_file = Path(__file__).resolve().parent / 'config.ini'
        
        # Create a ConfigParser object
        self.config = configparser.ConfigParser()
        
        # Load the configuration file
        self.config.read(self.config_file)
        
        # Load the settings into attributes
        self.load_settings()
    
    def load_settings(self):
        # Load general settings
        self.kafka_broker = self.config.get('Kafka', 'Broker', fallback='localhost:9092')
        self.kafka_topic = self.config.get('Kafka', 'Topic', fallback='default_topic')
        self.postgresql_host = self.config.get('PostgreSQL', 'Host', fallback='localhost')
        self.postgresql_port = self.config.getint('PostgreSQL', 'Port', fallback=5432)
        self.postgresql_user = self.config.get('PostgreSQL', 'User', fallback='user')
        self.postgresql_password = self.config.get('PostgreSQL', 'Password', fallback='password')
        self.mongodb_host = self.config.get('MongoDB', 'Host', fallback='localhost')
        self.mongodb_port = self.config.getint('MongoDB', 'Port', fallback=27017)
        self.mongodb_user = self.config.get('MongoDB', 'User', fallback='user')
        self.mongodb_password = self.config.get('MongoDB', 'Password', fallback='password')
        self.log_level = self.config.get('Logging', 'Level', fallback='INFO')
        self.debug_mode = self.config.getboolean('General', 'DebugMode', fallback=False)
    
    def __getitem__(self, key):
        return getattr(self, key, None)

# Instantiate and use the Settings class
settings = Settings()

# Example usage
if __name__ == "__main__":
    print(f"Kafka Broker: {settings.kafka_broker}")
    print(f"PostgreSQL Host: {settings.postgresql_host}")
    print(f"MongoDB Port: {settings.mongodb_port}")
    print(f"Debug Mode: {settings.debug_mode}")
