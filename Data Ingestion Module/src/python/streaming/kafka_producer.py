import logging
from typing import Dict
from confluent_kafka import Producer
import json

# Configure logging
logging.basicConfig(level=logging.INFO)

class KafkaProducer:
    def __init__(self, config: Dict[str, str]):
        """
        Initialize Kafka Producer with the provided configuration.
        :param config: Dictionary containing Kafka configuration parameters.
        """
        self.producer = Producer(config)
        logging.info("Kafka Producer initialized")

    def produce_message(self, topic: str, message: Dict[str, str]) -> None:
        """
        Produce a message to a Kafka topic.
        :param topic: Kafka topic to produce the message to.
        :param message: Dictionary containing the message to be sent.
        """
        try:
            self.producer.produce(topic, json.dumps(message))
            self.producer.flush()
            logging.info(f"Message produced to topic {topic}: {message}")
        except Exception as e:
            logging.error(f"Failed to produce message: {e}")

# Example usage
if __name__ == "__main__":
    kafka_config = {
        'bootstrap.servers': 'localhost:9092'
    }
    producer = KafkaProducer(kafka_config)
    test_message = {"key": "value"}
    producer.produce_message('test_topic', test_message)
