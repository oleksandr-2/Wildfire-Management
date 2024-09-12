cmake_minimum_required(VERSION 3.14)
project(WildfireCoPSystem LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(pybind11 REQUIRED)
find_package(Boost REQUIRED)
find_package(Threads REQUIRED)
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(Arrow REQUIRED)
find_package(Kafka REQUIRED)
find_package(PostgreSQL REQUIRED)

# Include directories for C++ libraries
include_directories(${Boost_INCLUDE_DIRS})
include_directories(${Python3_INCLUDE_DIRS})
include_directories(${Arrow_INCLUDE_DIRS})
include_directories(${Kafka_INCLUDE_DIRS})
include_directories(${PostgreSQL_INCLUDE_DIRS})

# Define the source directory
set(SOURCE_DIR "${CMAKE_SOURCE_DIR}/src/cpp")

# Add subdirectories
add_subdirectory(${SOURCE_DIR})

# Add Python bindings
add_subdirectory(${CMAKE_SOURCE_DIR}/bindings)

# Set the output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Define the build target for the main executable (if applicable)
add_executable(wildfire_cop_app 
    ${SOURCE_DIR}/main.cpp
    # Add other source files here
)

# Link libraries to the main executable
target_link_libraries(wildfire_cop_app 
    PRIVATE
    Boost::Boost
    pybind11::module
    ${Arrow_LIBRARIES}
    ${Kafka_LIBRARIES}
    ${PostgreSQL_LIBRARIES}
    Threads::Threads
)

# Add custom targets for C++ components
# Example:
# add_custom_target(run_all_tests
#     COMMAND ${CMAKE_CTEST_COMMAND}
#     DEPENDS wildfire_cop_app
# )

# Include additional directories
include_directories(${CMAKE_SOURCE_DIR}/src/cpp)

# Add custom targets
add_custom_target(run ALL
    COMMAND ${CMAKE_COMMAND} --build . --target all
    DEPENDS wildfire_cop_app
)

# Install rules
install(TARGETS wildfire_cop_app
    RUNTIME DESTINATION bin
)

# Enable testing
enable_testing()

# Include CTest for running tests
include(CTest)


# # Run CMake to configure and generate the build system: 
# mkdir build
# cd build
# cmake ..
# make
