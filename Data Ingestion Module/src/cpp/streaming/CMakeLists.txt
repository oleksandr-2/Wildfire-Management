cmake_minimum_required(VERSION 3.10)

# Set the project name
project(KafkaCore)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Find the librdkafka library
find_package(PkgConfig REQUIRED)
pkg_check_modules(LIBRDKAFKA REQUIRED librdkafka++)

# Add source files
set(SOURCES
    src/cpp/streaming/kafka_core.cpp
)

# Add header files
set(HEADERS
    src/cpp/streaming/kafka_core.hpp
)

# Create the library
add_library(kafka_core ${SOURCES} ${HEADERS})

# Include directories
target_include_directories(kafka_core PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/streaming ${LIBRDKAFKA_INCLUDE_DIRS})

# Link librdkafka library
target_link_libraries(kafka_core ${LIBRDKAFKA_LIBRARIES})

# Add executable for testing or standalone execution if necessary
# add_executable(test_kafka_core test/test_kafka_core.cpp)
# target_link_libraries(test_kafka_core kafka_core ${LIBRDKAFKA_LIBRARIES})
