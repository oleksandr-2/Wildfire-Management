# Specify the minimum version of CMake
cmake_minimum_required(VERSION 3.10)

# Set the project name and version
project(ResourceOptimization VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the source files for the resource_optimization module
set(RESOURCE_OPTIMIZATION_SOURCES
    resource_allocator.cpp
)

# Add the header files for the resource_optimization module
set(RESOURCE_OPTIMIZATION_HEADERS
    resource_allocator.hpp
)

# Create a library from the source files
add_library(resource_optimization STATIC ${RESOURCE_OPTIMIZATION_SOURCES} ${RESOURCE_OPTIMIZATION_HEADERS})

# Include directories for the resource_optimization module
target_include_directories(resource_optimization PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Link other libraries if necessary (e.g., Boost)
# target_link_libraries(resource_optimization PRIVATE Boost::boost)

# Optionally, you can add tests or additional configurations here
