#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "converter_core.hpp" // Assuming this is the header file for the C++ ConverterCore class

namespace py = pybind11;

// Binding class for ConverterCore
PYBIND11_MODULE(bindings, m) 
{
    // Bind the ConverterCore class
    py::class_<ConverterCore>(m, "ConverterCore")
        .def(py::init<>())  // Bind the default constructor
        .def("convert", &ConverterCore::convert, "Convert data from one format to another")
        .def("set_conversion_parameters", &ConverterCore::setConversionParameters, "Set parameters for conversion")
        .def("get_conversion_parameters", &ConverterCore::getConversionParameters, "Get the current conversion parameters")
        .def("reset", &ConverterCore::reset, "Reset the converter state");
}
