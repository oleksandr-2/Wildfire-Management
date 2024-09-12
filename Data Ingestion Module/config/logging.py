import logging
import logging.config
import yaml

# Load logging configuration from YAML file
with open('config/logging_config.yaml', 'r') as file:
    logging_config = yaml.safe_load(file.read())

# Configure logging
logging.config.dictConfig(logging_config)

# Example usage
logger = logging.getLogger('my_module')

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.error('This is an error message')

# To use this YAML configuration in your Python application, you can load it using the logging.config module. Here’s how to do it