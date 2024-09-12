#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // For binding STL containers
#include "dispersion_model.hpp"

namespace py = pybind11;

PYBIND11_MODULE(smoke_dispersion_bind, m) 
{
    m.doc() = "pybind11 bindings for the Smoke Dispersion component";

    py::class_<DispersionModel>(m, "DispersionModel")
        .def(py::init<>())
        .def("initialize", &DispersionModel::initialize)
        .def("runSimulation", &DispersionModel::runSimulation)
        .def("getConcentrationMap", &DispersionModel::getConcentrationMap)
        .def("setParameters", &DispersionModel::setParameters);
}
