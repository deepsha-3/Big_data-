import numpy as np

# Reshaping arrays
arr = np.arange(12)
print(f"Original: {arr}")
print(f"Reshaped (3x4):\n{arr.reshape(3, 4)}")
print(f"Reshaped (2x6):\n{arr.reshape(2, 6)}")

# Mathematical operations
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"\nArray a: {a}")
print(f"Array b: {b}")
print(f"a + b: {a + b}")
print(f"a * b: {a * b}")
print(f"a ** 2: {a ** 2}")
print(f"np.sqrt(a): {np.sqrt(a)}")
print(f"np.exp(a): {np.exp(a)}")
print(f"np.log(a): {np.log(a)}")

# Linear algebra
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print(f"\nMatrix1:\n{matrix1}")
print(f"Matrix2:\n{matrix2}")
print(f"Matrix multiplication:\n{np.dot(matrix1, matrix2)}")
print(f"Transpose of matrix1:\n{np.transpose(matrix1)}")
print(f"Determinant of matrix1: {np.linalg.det(matrix1):.2f}")
print(f"Inverse of matrix1:\n{np.linalg.inv(matrix1)}")
