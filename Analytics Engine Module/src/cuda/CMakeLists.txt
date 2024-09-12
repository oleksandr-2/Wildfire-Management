# CMake configuration for CUDA sources

cmake_minimum_required(VERSION 3.18)
project(SmokeDispersionKernel CUDA)

# Set the CUDA standard
set(CMAKE_CUDA_STANDARD 14)
set(CMAKE_CUDA_STANDARD_REQUIRED ON)

# Add the CUDA source files
set(CUDA_SOURCES
    smoke_dispersion_kernel.cu
)

# Add executable or library target
cuda_add_library(smoke_dispersion_lib ${CUDA_SOURCES})

# Link any required libraries here (e.g., CUDA runtime)
target_link_libraries(smoke_dispersion_lib ${CUDA_LIBRARIES})

# Include directories if needed
include_directories(${CMAKE_SOURCE_DIR}/include)
