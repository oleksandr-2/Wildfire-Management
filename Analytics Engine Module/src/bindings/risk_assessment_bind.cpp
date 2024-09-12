#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // For binding STL containers
#include "risk_calculator.hpp"

namespace py = pybind11;

PYBIND11_MODULE(risk_assessment_bind, m) 
{
    m.doc() = "pybind11 bindings for the Risk Assessment component";

    py::class_<RiskCalculator>(m, "RiskCalculator")
        .def(py::init<>())
        .def("initialize", &RiskCalculator::initialize)
        .def("calculateRisk", &RiskCalculator::calculateRisk)
        .def("getRiskMap", &RiskCalculator::getRiskMap)
        .def("setParameters", &RiskCalculator::setParameters);
}
