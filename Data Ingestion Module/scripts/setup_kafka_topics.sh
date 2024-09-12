#!/bin/bash

# Define Kafka properties
KAFKA_BIN_DIR="/path/to/kafka/bin"  # Update this to the path where Kafka is installed
ZK_CONNECT="localhost:2181"         # Zookeeper connection string
KAFKA_BROKER="localhost:9092"       # Kafka broker connection string

# Function to create a Kafka topic
create_topic() {
    local topic_name=$1
    local partitions=$2
    local replication_factor=$3
    echo "Creating topic: $topic_name"
    ${KAFKA_BIN_DIR}/kafka-topics.sh --create \
        --zookeeper ${ZK_CONNECT} \
        --replication-factor ${replication_factor} \
        --partitions ${partitions} \
        --topic ${topic_name}
}

# Function to list Kafka topics
list_topics() {
    echo "Listing topics:"
    ${KAFKA_BIN_DIR}/kafka-topics.sh --list \
        --zookeeper ${ZK_CONNECT}
}

# Create topics
create_topic "default_topic" 3 1
create_topic "another_topic" 5 2

# List topics to confirm creation
list_topics

echo "Kafka topics setup completed."

# Make the script executable: chmod +x scripts/setup_kafka_topics.sh
# Run the script: ./scripts/setup_kafka_topics.sh
