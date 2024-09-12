# Use an official Python runtime as a parent image
FROM python:3.11-slim AS python-base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python source code
COPY src/python /app/src/python
COPY config /app/config
COPY scripts /app/scripts

# Use an official C++ image for building the C++ components
FROM gcc:12 AS cpp-base

# Set the working directory
WORKDIR /app

# Install dependencies for building C++ components
RUN apt-get update && \
    apt-get install -y cmake libeigen3-dev libboost-all-dev libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the C++ source code
COPY src/cpp /app/src/cpp

# Build the C++ components
WORKDIR /app/src/cpp
RUN mkdir build && cd build && cmake .. && make

# Use an official CUDA image for CUDA components
FROM nvidia/cuda:12.2-base-ubuntu22.04 AS cuda-base

# Set the working directory
WORKDIR /app

# Install CUDA dependencies
RUN apt-get update && \
    apt-get install -y cmake

# Copy CUDA source code and build
COPY src/cuda /app/src/cuda
WORKDIR /app/src/cuda
RUN mkdir build && cd build && cmake .. && make

# Create the final image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install runtime dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy built C++ components
COPY --from=cpp-base /app/src/cpp/build /app/src/cpp/build

# Copy built CUDA components
COPY --from=cuda-base /app/src/cuda/build /app/src/cuda/build

# Copy the Python source code and configuration files
COPY src/python /app/src/python
COPY config /app/config
COPY scripts /app/scripts

# Set the entry point for the container
CMD ["python", "src/python/api/main.py"]
