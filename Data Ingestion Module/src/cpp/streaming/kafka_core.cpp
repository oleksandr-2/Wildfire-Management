#include "kafka_core.hpp"
#include <librdkafka/rdkafkacpp.h>
#include <iostream>

KafkaCore::KafkaCore(const std::string& brokers, const std::string& topic)
    : brokers_(brokers), topic_(topic), kafka_handle_(nullptr) 
{
    initialize_producer();
    initialize_consumer();
}

KafkaCore::~KafkaCore() 
{
    // Cleanup Kafka resources
    delete static_cast<RdKafka::Consumer*>(kafka_handle_);
    delete static_cast<RdKafka::Producer*>(kafka_handle_);
}

void KafkaCore::initialize_producer() 
{
    // Initialize Kafka producer
    RdKafka::Producer* producer = RdKafka::Producer::create(RdKafka::Conf::create(RdKafka::Conf::CONF_GLOBAL), nullptr);
    if (!producer) 
    {
        std::cerr << "Failed to create Kafka producer" << std::endl;
        return;
    }
    kafka_handle_ = producer;
}

void KafkaCore::initialize_consumer() 
{
    // Initialize Kafka consumer
    RdKafka::Consumer* consumer = RdKafka::Consumer::create(RdKafka::Conf::create(RdKafka::Conf::CONF_GLOBAL), nullptr);
    if (!consumer) 
    {
        std::cerr << "Failed to create Kafka consumer" << std::endl;
        return;
    }
    kafka_handle_ = consumer;
}

void KafkaCore::produce(const std::string& message) 
{
    RdKafka::Producer* producer = static_cast<RdKafka::Producer*>(kafka_handle_);
    RdKafka::ErrorCode resp = producer->produce(topic_, RdKafka::Producer::RK_MSG_COPY,
                                                message.data(), message.size(),
                                                nullptr, nullptr);
    if (resp != RdKafka::ERR_NO_ERROR) 
    {
        std::cerr << "Produce failed: " << RdKafka::err2str(resp) << std::endl;
    }
    producer->poll(0);
}

std::string KafkaCore::consume() 
{
    RdKafka::Consumer* consumer = static_cast<RdKafka::Consumer*>(kafka_handle_);
    RdKafka::Message* msg = consumer->consume(topic_, 0, 1000);
    if (msg->err() != RdKafka::ERR_NO_ERROR) 
    {
        std::cerr << "Consume failed: " << msg->errstr() << std::endl;
        delete msg;
        return "";
    }
    std::string message(static_cast<const char*>(msg->payload()), msg->len());
    delete msg;
    return message;
}
