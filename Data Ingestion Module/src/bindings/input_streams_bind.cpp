#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "input_handler.hpp" // Assuming this is the header file for the C++ InputHandler class

namespace py = pybind11;

// Binding class for InputHandler
PYBIND11_MODULE(bindings, m) 
{
    // Bind the InputHandler class
    py::class_<InputHandler>(m, "InputHandler")
        .def(py::init<>())  // Bind the default constructor
        .def("start", &InputHandler::start, "Start processing input streams")
        .def("stop", &InputHandler::stop, "Stop processing input streams")
        .def("get_status", &InputHandler::getStatus, "Get the status of the input handler")
        .def("set_configuration", &InputHandler::setConfiguration, "Set the configuration for the input handler")
        .def("get_configuration", &InputHandler::getConfiguration, "Get the current configuration of the input handler");
}
