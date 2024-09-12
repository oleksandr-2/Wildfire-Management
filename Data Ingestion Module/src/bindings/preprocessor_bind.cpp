#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "preprocessor_core.hpp" // Assuming this is the header file for the C++ PreprocessorCore class

namespace py = pybind11;

// Binding class for PreprocessorCore
PYBIND11_MODULE(bindings, m) 
{
    // Bind the PreprocessorCore class
    py::class_<PreprocessorCore>(m, "PreprocessorCore")
        .def(py::init<>())  // Bind the default constructor
        .def("process_data", &PreprocessorCore::processData, "Process input data")
        .def("configure", &PreprocessorCore::configure, "Configure the preprocessor")
        .def("get_configuration", &PreprocessorCore::getConfiguration, "Get the current configuration")
        .def("reset", &PreprocessorCore::reset, "Reset the preprocessor state");
}
