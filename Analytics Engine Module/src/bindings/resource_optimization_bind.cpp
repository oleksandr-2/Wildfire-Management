#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // For binding STL containers
#include "resource_allocator.hpp"

namespace py = pybind11;

PYBIND11_MODULE(resource_optimization_bind, m) 
{
    m.doc() = "pybind11 bindings for the Resource Optimization component";

    py::class_<ResourceAllocator>(m, "ResourceAllocator")
        .def(py::init<>())
        .def("initialize", &ResourceAllocator::initialize)
        .def("optimize", &ResourceAllocator::optimize)
        .def("getOptimalResources", &ResourceAllocator::getOptimalResources)
        .def("setParameters", &ResourceAllocator::setParameters);
}
