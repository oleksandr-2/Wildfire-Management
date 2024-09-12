cmake_minimum_required(VERSION 3.10)

# Set the project name
project(cpp)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add subdirectories for each component
add_subdirectory(input_streams)
add_subdirectory(preprocessing)
add_subdirectory(conversion)
add_subdirectory(streaming)
add_subdirectory(storage)
add_subdirectory(health)

# Optionally, add other directories if needed
# add_subdirectory(<other_directory>)

# Include directories
include_directories(
    ${CMAKE_SOURCE_DIR}/src/cpp/input_streams
    ${CMAKE_SOURCE_DIR}/src/cpp/preprocessing
    ${CMAKE_SOURCE_DIR}/src/cpp/conversion
    ${CMAKE_SOURCE_DIR}/src/cpp/streaming
    ${CMAKE_SOURCE_DIR}/src/cpp/storage
    ${CMAKE_SOURCE_DIR}/src/cpp/health
    # Add other include directories if needed
)

# Link libraries if needed
# target_link_libraries(<target_name> <libraries>)

# Optionally, add other configurations or settings if needed
