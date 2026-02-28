import numpy as np

# Creating a 2D array
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

print(f"Original array:\n{arr}")

# Basic indexing
print(f"Element at [0, 0]: {arr[0, 0]}")
print(f"Element at [1, 2]: {arr[1, 2]}")
print(f"First row: {arr[0]}")
print(f"Second column: {arr[:, 1]}")

# Slicing
print(f"First two rows, first two columns:\n{arr[:2, :2]}")
print(f"All rows, columns 1 to 3:\n{arr[:, 1:3]}")
print(f"Last row: {arr[-1]}")
print(f"Last column: {arr[:, -1]}")

# Boolean indexing
print(f"Elements > 50: {arr[arr > 50]}")

# "array indexing and slicing using NumPy"
# "numpy/arr_indexing_slicing.py"