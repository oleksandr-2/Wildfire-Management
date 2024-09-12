# Specify the minimum version of CMake
cmake_minimum_required(VERSION 3.10)

# Set the project name and version
project(DroneAnalysis VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Find OpenCV package
find_package(OpenCV REQUIRED)

# Add the source files for the drone_analysis module
set(DRONE_ANALYSIS_SOURCES
    image_processor.cpp
)

# Add the header files for the drone_analysis module
set(DRONE_ANALYSIS_HEADERS
    image_processor.hpp
)

# Create a library from the source files
add_library(drone_analysis STATIC ${DRONE_ANALYSIS_SOURCES} ${DRONE_ANALYSIS_HEADERS})

# Include directories for the drone_analysis module
target_include_directories(drone_analysis PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Link OpenCV libraries
target_link_libraries(drone_analysis PRIVATE ${OpenCV_LIBS})

# Optionally, you can add tests or additional configurations here
