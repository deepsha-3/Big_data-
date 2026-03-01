import numpy as np

# Different ways to create arrays
arr1 = np.array([1, 2, 3, 4, 5])  # From list
arr2 = np.zeros((3, 4))  # 3x4 array of zeros
arr3 = np.ones((2, 3))  # 2x3 array of ones
arr4 = np.arange(10)  # 0 to 9
arr5 = np.linspace(0, 10, 5)  # 5 equally spaced numbers from 0 to 10
arr6 = np.random.rand(3, 3)  # 3x3 random numbers
arr7 = np.eye(4)  # 4x4 identity matrix

print("Array from list:", arr1)
print("Zeros array:\n", arr2)
print("Ones array:\n", arr3)
print("Arange:", arr4)
print("Linspace:", arr5)
print("Random array:\n", arr6)
print("Identity matrix:\n", arr7)
