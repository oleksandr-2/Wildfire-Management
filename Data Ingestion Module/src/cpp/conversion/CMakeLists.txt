cmake_minimum_required(VERSION 3.10)

# Set the project name
project(ConverterCore)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add source files
set(SOURCES
    src/cpp/conversion/converter_core.cpp
)

# Add header files
set(HEADERS
    src/cpp/conversion/converter_core.hpp
)

# Create the library
add_library(converter_core ${SOURCES} ${HEADERS})

# Include directories
target_include_directories(converter_core PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/conversion)

# Link dependencies if needed (e.g., Boost, Apache Arrow, etc.)
# target_link_libraries(converter_core <dependencies>)

# Add executable for testing or standalone execution if necessary
# add_executable(test_converter_core test/test_converter_core.cpp)
# target_link_libraries(test_converter_core converter_core)
