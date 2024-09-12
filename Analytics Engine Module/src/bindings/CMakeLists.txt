cmake_minimum_required(VERSION 3.10)
project(bindings)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find pybind11
find_package(pybind11 REQUIRED)

# Add source files for bindings
set(BINDING_SOURCES
    fire_behavior_bind.cpp
    resource_optimization_bind.cpp
    risk_assessment_bind.cpp
    smoke_dispersion_bind.cpp
    drone_analysis_bind.cpp
)

# Create a library for Python bindings
pybind11_add_module(drone_analysis_bind MODULE 
    ${BINDING_SOURCES}
)

# Link libraries if needed (e.g., C++ libraries)
target_link_libraries(drone_analysis_bind PRIVATE
    # Add your C++ libraries here, if any
)

# Include directories if needed
target_include_directories(drone_analysis_bind PRIVATE
    # Add your include directories here, if any
)
