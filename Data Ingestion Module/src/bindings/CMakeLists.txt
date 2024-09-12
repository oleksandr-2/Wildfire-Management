cmake_minimum_required(VERSION 3.14)
project(bindings)

# Find pybind11 package
find_package(pybind11 REQUIRED)

# Define the modules to build
pybind11_add_module(bindings
    input_streams_bind.cpp
    preprocessor_bind.cpp
    converter_bind.cpp
    kafka_bind.cpp
    data_writer_bind.cpp
    health_checker_bind.cpp
)

# Include directories for C++ headers
target_include_directories(bindings
    PRIVATE ${PROJECT_SOURCE_DIR}/../cpp
)

# Link against the necessary libraries (if any)
# target_link_libraries(bindings PRIVATE ${OTHER_LIBRARIES})

# Optionally, set compiler options
# target_compile_options(bindings PRIVATE -Wall -Wextra)

# Add any additional compile definitions if needed
# target_compile_definitions(bindings PRIVATE SOME_DEFINITION)
