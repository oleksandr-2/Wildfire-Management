import os

# Database settings
DATABASE = {
    'HOST': os.getenv('DB_HOST', 'localhost'),
    'PORT': int(os.getenv('DB_PORT', 5432)),
    'USER': os.getenv('DB_USER', 'user'),
    'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
    'NAME': os.getenv('DB_NAME', 'analytics_db')
}

# Kafka settings
KAFKA = {
    'BROKER': os.getenv('KAFKA_BROKER', 'localhost:9092'),
    'INPUT_TOPIC': os.getenv('KAFKA_INPUT_TOPIC', 'input_topic'),
    'OUTPUT_TOPIC': os.getenv('KAFKA_OUTPUT_TOPIC', 'output_topic'),
    'GROUP_ID': os.getenv('KAFKA_GROUP_ID', 'analytics_group')
}

# Logging settings
LOGGING = {
    'LEVEL': os.getenv('LOGGING_LEVEL', 'INFO'),
    'FILE': os.getenv('LOGGING_FILE', 'app.log')
}

# Machine Learning Model Paths
ML_MODELS = {
    'FIRE_SPREAD_MODEL': os.getenv('FIRE_SPREAD_MODEL_PATH', 'models/fire_spread_nn.h5'),
    'RESOURCE_ALLOCATION_MODEL': os.getenv('RESOURCE_ALLOCATION_MODEL_PATH', 'models/resource_allocation_rf.pkl')
}

# API settings
API = {
    'HOST': os.getenv('API_HOST', '0.0.0.0'),
    'PORT': int(os.getenv('API_PORT', 8000))
}

# Other settings
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Ensure all required environment variables are set
required_env_vars = [
    'DB_HOST', 'DB_PORT', 'DB_USER', 'DB_PASSWORD', 'DB_NAME',
    'KAFKA_BROKER', 'KAFKA_INPUT_TOPIC', 'KAFKA_OUTPUT_TOPIC', 'KAFKA_GROUP_ID',
    'LOGGING_LEVEL', 'LOGGING_FILE',
    'FIRE_SPREAD_MODEL_PATH', 'RESOURCE_ALLOCATION_MODEL_PATH',
    'API_HOST', 'API_PORT'
]

for var in required_env_vars:
    if os.getenv(var) is None:
        raise EnvironmentError(f"Required environment variable {var} is not set.")

