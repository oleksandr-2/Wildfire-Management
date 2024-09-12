# Specify the minimum version of CMake
cmake_minimum_required(VERSION 3.10)

# Set the project name and version
project(SmokeDispersion VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the source files for the smoke_dispersion module
set(SMOKE_DISPERSION_SOURCES
    dispersion_model.cpp
)

# Add the header files for the smoke_dispersion module
set(SMOKE_DISPERSION_HEADERS
    dispersion_model.hpp
)

# Create a library from the source files
add_library(smoke_dispersion STATIC ${SMOKE_DISPERSION_SOURCES} ${SMOKE_DISPERSION_HEADERS})

# Include directories for the smoke_dispersion module
target_include_directories(smoke_dispersion PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Link other libraries if necessary (e.g., Boost)
# target_link_libraries(smoke_dispersion PRIVATE Boost::boost)

# Optionally, you can add tests or additional configurations here
