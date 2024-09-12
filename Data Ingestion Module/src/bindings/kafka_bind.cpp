#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "kafka_core.hpp" // Assuming this is the header file for the C++ KafkaCore class

namespace py = pybind11;

// Binding class for KafkaCore
PYBIND11_MODULE(bindings, m) 
{
    // Bind the KafkaCore class
    py::class_<KafkaCore>(m, "KafkaCore")
        .def(py::init<>())  // Bind the default constructor
        .def("produce_message", &KafkaCore::produceMessage, "Produce a message to a Kafka topic")
        .def("consume_message", &KafkaCore::consumeMessage, "Consume a message from a Kafka topic")
        .def("set_configuration", &KafkaCore::setConfiguration, "Set the Kafka client configuration")
        .def("get_configuration", &KafkaCore::getConfiguration, "Get the current Kafka client configuration")
        .def("connect", &KafkaCore::connect, "Connect to the Kafka broker")
        .def("disconnect", &KafkaCore::disconnect, "Disconnect from the Kafka broker");
}
