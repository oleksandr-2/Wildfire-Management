#include <pybind11/pybind11.h>
#include "health_checker_core.hpp" // Assuming this is the header file for the C++ HealthCheckerCore class

namespace py = pybind11;

// Binding class for HealthCheckerCore
PYBIND11_MODULE(bindings, m) 
{
    // Bind the HealthCheckerCore class
    py::class_<HealthCheckerCore>(m, "HealthCheckerCore")
        .def(py::init<>())  // Bind the default constructor
        .def("check_system_health", &HealthCheckerCore::checkSystemHealth, "Check the health of the system")
        .def("get_performance_metrics", &HealthCheckerCore::getPerformanceMetrics, "Get performance metrics of the system")
        .def("set_thresholds", &HealthCheckerCore::setThresholds, "Set thresholds for health checks")
        .def("get_thresholds", &HealthCheckerCore::getThresholds, "Get current thresholds for health checks")
        .def("report_health_status", &HealthCheckerCore::reportHealthStatus, "Report the current health status of the system");
}
