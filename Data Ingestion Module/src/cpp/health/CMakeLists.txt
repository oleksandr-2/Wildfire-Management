cmake_minimum_required(VERSION 3.10)

# Set the project name
project(HealthCheckerCore)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add source files
set(SOURCES
    src/cpp/health/health_checker_core.cpp
)

# Add header files
set(HEADERS
    src/cpp/health/health_checker_core.hpp
)

# Create the library
add_library(health_checker_core ${SOURCES} ${HEADERS})

# Include directories
target_include_directories(health_checker_core PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/health)
