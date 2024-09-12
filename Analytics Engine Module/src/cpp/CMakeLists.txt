# Specify the minimum version of CMake
cmake_minimum_required(VERSION 3.10)

# Set the project name and version
project(AnalyticsEngineModule VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add subdirectories for each module
add_subdirectory(fire_behavior)
add_subdirectory(resource_optimization)
add_subdirectory(risk_assessment)
add_subdirectory(smoke_dispersion)
add_subdirectory(drone_analysis)

# Optionally, you can add additional configurations here
