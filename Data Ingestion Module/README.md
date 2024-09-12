# Comprehensive Wildfire Common Operating Picture (CoP) System

## Overview

The Comprehensive Wildfire Common Operating Picture (CoP) System is an advanced modular platform designed to enhance real-time situational awareness, decision support, and resource management for wildfire operations. The system integrates data from multiple sources, including AI-controlled drones, to provide a comprehensive view for incident management teams.

## Project Structure

The project is organized into the following main components:

- **Data Ingestion Module**: Collects and standardizes data from various sources.
- **Analytics Engine Module**: Processes data and generates actionable insights.
- **Visualization Module**: Presents data through interactive and user-friendly interfaces.
- **Decision Support Module**: Assists in strategic decision-making.
- **Collaboration Module**: Facilitates communication and data sharing.
- **Synthetic Environment Module**: Provides training and simulation capabilities.
- **Security Module**: Ensures system and data security.
- **Resilience Module**: Maintains system availability and data integrity.
- **Autonomous Drone Operations Module**: Manages AI-controlled drone operations.
- **Automated Drone Station Module**: Handles automated drone logistics.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop) (for containerization)
- [Kubernetes](https://kubernetes.io/docs/setup/) (for orchestration)
- [CMake](https://cmake.org/install/) (for building C++ components)
- [Python](https://www.python.org/downloads/) (for Python components)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/wildfire-cop-system.git
    cd wildfire-cop-system
    ```

2. **Build C++ components**:

    ```bash
    mkdir build
    cd build
    cmake ..
    make
    ```

3. **Install Python dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Kafka and databases**:

    ```bash
    ./scripts/setup_kafka_topics.sh
    ./scripts/init_databases.sh
    ```

5. **Run Docker Compose** to start all services:

    ```bash
    docker-compose up
    ```

## Usage

1. **Start the application**:

    The system will start automatically using Docker Compose. You can access the API at `http://localhost:8000`.

2. **Interacting with the API**:

    Use the FastAPI documentation at `http://localhost:8000/docs` to interact with the API endpoints.

3. **Running Tests**:

    Run unit tests for C++ components:

    ```bash
    cd build
    ctest
    ```

    Run Python tests:

    ```bash
    pytest
    ```

## Configuration

Configuration files are located in the `config/` directory:

- `settings.py`: Contains configuration settings for the Python application.
- `logging_config.yaml`: Configures logging for the application.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [your.email@example.com](mailto:your.email@example.com).

