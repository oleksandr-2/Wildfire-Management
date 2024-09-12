cmake_minimum_required(VERSION 3.16)
project(AnalyticsEngineModule)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable CUDA
find_package(CUDA REQUIRED)
enable_language(CUDA)

# Add subdirectories
add_subdirectory(src/cpp)
add_subdirectory(src/cuda)
add_subdirectory(bindings)
add_subdirectory(tests)

# Define install targets
install(DIRECTORY src/cpp/ DESTINATION include)
install(DIRECTORY src/cuda/ DESTINATION include)
install(DIRECTORY bindings/ DESTINATION include)
