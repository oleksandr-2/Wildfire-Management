#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "data_writer_core.hpp" // Assuming this is the header file for the C++ DataWriterCore class

namespace py = pybind11;

// Binding class for DataWriterCore
PYBIND11_MODULE(bindings, m) 
{
    // Bind the DataWriterCore class
    py::class_<DataWriterCore>(m, "DataWriterCore")
        .def(py::init<>())  // Bind the default constructor
        .def("write_to_postgres", &DataWriterCore::writeToPostgres, "Write data to PostgreSQL database")
        .def("write_to_mongodb", &DataWriterCore::writeToMongoDB, "Write data to MongoDB database")
        .def("set_postgres_configuration", &DataWriterCore::setPostgresConfiguration, "Set PostgreSQL database configuration")
        .def("set_mongodb_configuration", &DataWriterCore::setMongoDBConfiguration, "Set MongoDB database configuration")
        .def("get_postgres_configuration", &DataWriterCore::getPostgresConfiguration, "Get the current PostgreSQL database configuration")
        .def("get_mongodb_configuration", &DataWriterCore::getMongoDBConfiguration, "Get the current MongoDB database configuration")
        .def("flush", &DataWriterCore::flush, "Flush the data writer to ensure all data is written");
}
