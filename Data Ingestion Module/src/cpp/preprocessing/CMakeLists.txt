cmake_minimum_required(VERSION 3.10)

# Set the project name
project(PreprocessorCore)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add source files
set(SOURCES
    src/cpp/preprocessing/preprocessor_core.cpp
)

# Add header files
set(HEADERS
    src/cpp/preprocessing/preprocessor_core.hpp
)

# Create the library
add_library(preprocessor_core ${SOURCES} ${HEADERS})

# Include directories
target_include_directories(preprocessor_core PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src/cpp/preprocessing)

# Link dependencies if needed (e.g., Boost, Apache Arrow, etc.)
# target_link_libraries(preprocessor_core <dependencies>)

# Add executable for testing or standalone execution if necessary
# add_executable(test_preprocessor_core test/test_preprocessor_core.cpp)
# target_link_libraries(test_preprocessor_core preprocessor_core)
