import logging
import psycopg2
import pymongo
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

class DataWriter:
    def __init__(self, postgres_config: Dict[str, Any], mongo_config: Dict[str, Any]):
        """
        Initialize DataWriter with PostgreSQL and MongoDB configurations.
        :param postgres_config: Dictionary containing PostgreSQL configuration parameters.
        :param mongo_config: Dictionary containing MongoDB configuration parameters.
        """
        try:
            self.postgres_conn = psycopg2.connect(**postgres_config)
            self.postgres_cursor = self.postgres_conn.cursor()
            logging.info("PostgreSQL connection established")
        except Exception as e:
            logging.error(f"Failed to connect to PostgreSQL: {e}")

        try:
            self.mongo_client = pymongo.MongoClient(**mongo_config)
            self.mongo_db = self.mongo_client['wildfire_db']
            logging.info("MongoDB connection established")
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB: {e}")

    def write_to_postgres(self, table: str, data: Dict[str, Any]) -> None:
        """
        Write data to PostgreSQL database.
        :param table: Table name where the data will be inserted.
        :param data: Dictionary containing the data to be inserted.
        """
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        try:
            self.postgres_cursor.execute(query, list(data.values()))
            self.postgres_conn.commit()
            logging.info(f"Data written to PostgreSQL table {table}: {data}")
        except Exception as e:
            logging.error(f"Failed to write data to PostgreSQL: {e}")
            self.postgres_conn.rollback()

    def write_to_mongo(self, collection: str, data: Dict[str, Any]) -> None:
        """
        Write data to MongoDB database.
        :param collection: Collection name where the data will be inserted.
        :param data: Dictionary containing the data to be inserted.
        """
        try:
            mongo_collection = self.mongo_db[collection]
            mongo_collection.insert_one(data)
            logging.info(f"Data written to MongoDB collection {collection}: {data}")
        except Exception as e:
            logging.error(f"Failed to write data to MongoDB: {e}")

    def close_connections(self) -> None:
        """
        Close the database connections.
        """
        if hasattr(self, 'postgres_conn'):
            self.postgres_cursor.close()
            self.postgres_conn.close()
            logging.info("PostgreSQL connection closed")
        if hasattr(self, 'mongo_client'):
            self.mongo_client.close()
            logging.info("MongoDB connection closed")

# Example usage
if __name__ == "__main__":
    postgres_config = 
    {
        'dbname': 'wildfire',
        'user': 'postgres',
        'password': 'password',
        'host': 'localhost',
        'port': '5432'
    }
    mongo_config = {
        'host': 'localhost',
        'port': 27017
    }

    data_writer = DataWriter(postgres_config, mongo_config)
    sample_data_postgres = {'column1': 'value1', 'column2': 'value2'}
    sample_data_mongo = {'field1': 'value1', 'field2': 'value2'}

    data_writer.write_to_postgres('sample_table', sample_data_postgres)
    data_writer.write_to_mongo('sample_collection', sample_data_mongo)
    data_writer.close_connections()
