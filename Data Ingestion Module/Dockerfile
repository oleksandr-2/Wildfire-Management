# Stage 1: Build C++ components
FROM ubuntu:20.04 AS cpp-builder

# Install dependencies for building C++ components
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    libboost-all-dev \
    libpq-dev \
    libmongocxx-dev \
    librdkafka-dev \
    python3-dev \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy C++ source code and CMakeLists.txt
COPY src/cpp /app/src/cpp
COPY src/cpp/CMakeLists.txt /app/src/cpp

# Build C++ components
RUN cd /app/src/cpp && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make

# Stage 2: Build Python components
FROM python:3.9-slim AS python-builder

# Install Python dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python source code
COPY src/python /app/src/python

# Install pybind11 and other necessary packages
RUN pip install pybind11

# Stage 3: Final image
FROM ubuntu:20.04

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y \
    libboost-all-dev \
    libpq-dev \
    libmongocxx1 \
    librdkafka1 \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy C++ binaries from builder stage
COPY --from=cpp-builder /app/src/cpp/build /app/bin

# Copy Python environment and source code from builder stage
COPY --from=python-builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=python-builder /usr/local/bin /usr/local/bin
COPY src/python /app/src/python
COPY config/settings.py /app/config/
COPY config/logging_config.yaml /app/config/

# Set environment variables
ENV PYTHONPATH=/app/src/python

# Expose API port
EXPOSE 8000

# Start the application
CMD ["python3", "/app/src/python/api/main.py"]

# Build the Docker image with: docker build -t wildfire-cop-system .
# Run the Docker container with: docker run -p 8000:8000 wildfire-cop-system
