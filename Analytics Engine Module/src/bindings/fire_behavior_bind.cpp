#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // For binding STL containers
#include "fire_spread_model.hpp"

namespace py = pybind11;

PYBIND11_MODULE(fire_behavior_bind, m) 
{
    m.doc() = "pybind11 bindings for the Fire Behavior component";

    py::class_<FireSpreadModel>(m, "FireSpreadModel")
        .def(py::init<>())
        .def("initialize", &FireSpreadModel::initialize)
        .def("update", &FireSpreadModel::update)
        .def("getPrediction", &FireSpreadModel::getPrediction)
        .def("setParameters", &FireSpreadModel::setParameters);
}
