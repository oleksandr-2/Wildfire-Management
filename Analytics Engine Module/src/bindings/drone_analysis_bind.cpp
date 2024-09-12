#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // For binding STL containers
#include "image_processor.hpp"

namespace py = pybind11;

PYBIND11_MODULE(drone_analysis_bind, m) 
{
    m.doc() = "pybind11 bindings for the Drone Analysis component";

    py::class_<ImageProcessor>(m, "ImageProcessor")
        .def(py::init<>())
        .def("initialize", &ImageProcessor::initialize)
        .def("processImage", &ImageProcessor::processImage)
        .def("getFireDetectionResults", &ImageProcessor::getFireDetectionResults)
        .def("setParameters", &ImageProcessor::setParameters);
}
