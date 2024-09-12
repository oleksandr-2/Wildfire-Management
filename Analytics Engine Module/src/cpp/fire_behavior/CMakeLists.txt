# Specify the minimum version of CMake
cmake_minimum_required(VERSION 3.10)

# Set the project name and version
project(FireBehavior VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the source files for the fire_behavior module
set(FIRE_BEHAVIOR_SOURCES
    fire_spread_model.cpp
)

# Add the header files for the fire_behavior module
set(FIRE_BEHAVIOR_HEADERS
    fire_spread_model.hpp
)

# Create a library from the source files
add_library(fire_behavior STATIC ${FIRE_BEHAVIOR_SOURCES} ${FIRE_BEHAVIOR_HEADERS})

# Include directories for the fire_behavior module
target_include_directories(fire_behavior PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Link other libraries if necessary (e.g., Eigen, Boost)
# target_link_libraries(fire_behavior PRIVATE Eigen3::Eigen Boost::boost)

# Optionally, you can add tests or additional configurations here
