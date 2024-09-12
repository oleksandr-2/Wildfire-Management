cmake_minimum_required(VERSION 3.10)

# Set the project name
project(DataWriterCore)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Find PostgreSQL and MongoDB client libraries
find_package(PkgConfig REQUIRED)
pkg_check_modules(POSTGRESQL REQUIRED libpqxx)
pkg_check_modules(MONGODB REQUIRED libmongocxx)

# Add source files
set(SOURCES
    src/cpp/storage/data_writer_core.cpp
)

# Add header files
set(HEADERS
    src/cpp/storage/data_writer_core.hpp
)

# Create the library
add_library(data_writer_core ${SOURCES} ${HEADERS})

# Include directories
target_include_directories(data_writer_core PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/storage ${POSTGRESQL_INCLUDE_DIRS} ${MONGODB_INCLUDE_DIRS})

# Link PostgreSQL and MongoDB libraries
target_link_libraries(data_writer_core ${POSTGRESQL_LIBRARIES} ${MONGODB_LIBRARIES})
