#include <cuda_runtime.h>
#include <device_launch_parameters.h>
#include <cmath>

// Constants for grid dimensions
const int GRID_WIDTH = 1024;
const int GRID_HEIGHT = 1024;

// Define kernel for smoke dispersion simulation
__global__ void smokeDispersionKernel(float* grid, float* newGrid, int width, int height, float dispersionRate) 
{
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < width && y < height) 
    {
        int index = y * width + x;

        // Compute the new smoke concentration
        float newConcentration = grid[index];
        if (grid[index] > 0.0f) 
        {
            // Spread to neighboring cells with dispersion effect
            float dispersion = 0.0f;
            if (x > 0) dispersion += grid[index - 1] * dispersionRate;
            if (x < width - 1) dispersion += grid[index + 1] * dispersionRate;
            if (y > 0) dispersion += grid[index - width] * dispersionRate;
            if (y < height - 1) dispersion += grid[index + width] * dispersionRate;

            newConcentration += dispersion;
            newConcentration = fminf(newConcentration, 1.0f); // Cap concentration
        }

        newGrid[index] = newConcentration;
    }
}

// Host function to launch the kernel
void runSmokeDispersionSimulation(float* h_grid, float* h_newGrid, int width, int height, float dispersionRate) 
{
    float* d_grid;
    float* d_newGrid;

    size_t size = width * height * sizeof(float);

    // Allocate device memory
    cudaMalloc(&d_grid, size);
    cudaMalloc(&d_newGrid, size);

    // Copy data to device
    cudaMemcpy(d_grid, h_grid, size, cudaMemcpyHostToDevice);

    // Define block and grid sizes
    dim3 blockSize(16, 16);
    dim3 gridSize((width + blockSize.x - 1) / blockSize.x, (height + blockSize.y - 1) / blockSize.y);

    // Launch kernel
    smokeDispersionKernel<<<gridSize, blockSize>>>(d_grid, d_newGrid, width, height, dispersionRate);

    // Copy results back to host
    cudaMemcpy(h_newGrid, d_newGrid, size, cudaMemcpyDeviceToHost);

    // Free device memory
    cudaFree(d_grid);
    cudaFree(d_newGrid);
}
