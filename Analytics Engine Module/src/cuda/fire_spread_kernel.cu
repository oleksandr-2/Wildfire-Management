#include <cuda_runtime.h>
#include <device_launch_parameters.h>
#include <cmath>

// Constants for grid dimensions
const int GRID_WIDTH = 1024;
const int GRID_HEIGHT = 1024;

// Define kernel for fire spread simulation
__global__ void fireSpreadKernel(float* grid, float* newGrid, int width, int height, float spreadFactor) 
{
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < width && y < height) 
    {
        int index = y * width + x;

        // Compute the new fire intensity
        float newIntensity = grid[index];
        if (grid[index] > 0.0f) 
        {
            // Spread to neighboring cells
            if (x > 0) newIntensity += grid[index - 1] * spreadFactor;
            if (x < width - 1) newIntensity += grid[index + 1] * spreadFactor;
            if (y > 0) newIntensity += grid[index - width] * spreadFactor;
            if (y < height - 1) newIntensity += grid[index + width] * spreadFactor;

            newIntensity = fminf(newIntensity, 1.0f); // Cap intensity
        }

        newGrid[index] = newIntensity;
    }
}

// Host function to launch the kernel
void runFireSpreadSimulation(float* h_grid, float* h_newGrid, int width, int height, float spreadFactor) 
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
    fireSpreadKernel<<<gridSize, blockSize>>>(d_grid, d_newGrid, width, height, spreadFactor);

    // Copy results back to host
    cudaMemcpy(h_newGrid, d_newGrid, size, cudaMemcpyDeviceToHost);

    // Free device memory
    cudaFree(d_grid);
    cudaFree(d_newGrid);
}
