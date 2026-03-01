import numpy as np

# Array properties
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(f"Array:\n{arr}")
print(f"Shape: {arr.shape}")
print(f"Dimensions: {arr.ndim}")
print(f"Size (total elements): {arr.size}")
print(f"Data type: {arr.dtype}")
print(f"Item size (bytes): {arr.itemsize}")
print(f"Total memory: {arr.nbytes} bytes")
