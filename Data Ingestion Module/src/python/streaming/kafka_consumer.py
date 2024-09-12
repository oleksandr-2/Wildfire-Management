import logging
from typing import Callable, Dict
from confluent_kafka import Consumer, KafkaException, KafkaError

# Configure logging
logging.basicConfig(level=logging.INFO)

class KafkaConsumer:
    def __init__(self, config: Dict[str, str], topics: [str]):
        """
        Initialize Kafka Consumer with the provided configuration and topics.
        :param config: Dictionary containing Kafka configuration parameters.
        :param topics: List of Kafka topics to subscribe to.
        """
        self.consumer = Consumer(config)
        self.consumer.subscribe(topics)
        logging.info("Kafka Consumer initialized")

    def consume_messages(self, callback: Callable[[Dict[str, str]], None]) -> None:
        """
        Continuously consume messages from Kafka and pass them to the callback function.
        :param callback: Function to process each consumed message.
        """
        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        logging.error(f"Consumer error: {msg.error()}")
                        break
                message = msg.value().decode('utf-8')
                callback(message)
        except KeyboardInterrupt:
            logging.info("Consumer interrupted")
        except KafkaException as e:
            logging.error(f"Kafka exception: {e}")
        finally:
            self.consumer.close()

# Example usage
if __name__ == "__main__":
    kafka_config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'test_group',
        'auto.offset.reset': 'earliest'
    }
    def process_message(message):
        logging.info(f"Received message: {message}")

    consumer = KafkaConsumer(kafka_config, ['test_topic'])
    consumer.consume_messages(process_message)
