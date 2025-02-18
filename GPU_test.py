import torch
import time

# Define matrix size
size = 20000

# Generate random matrices
matrix1 = torch.randn(size, size)
matrix2 = torch.randn(size, size)

# Function to measure time taken for matrix multiplication
def matrix_multiplication(device):
    matrix1_device = matrix1.to(device)
    matrix2_device = matrix2.to(device)
    
    start_time = time.time()
    result = torch.mm(matrix1_device, matrix2_device)
    torch.cuda.synchronize() if device == "cuda" else None  # Ensure all GPU work is finished
    end_time = time.time()
    
    return end_time - start_time

# Compute on CPU
cpu_time = matrix_multiplication("cpu")
print(f"Time taken on CPU: {cpu_time:.4f} seconds")

# Check if GPU is available and compute on GPU
if torch.cuda.is_available():
    gpu_time = matrix_multiplication("cuda")
    print(f"Time taken on GPU: {gpu_time:.4f} seconds")
else:
    print("GPU is not available on this device.")

