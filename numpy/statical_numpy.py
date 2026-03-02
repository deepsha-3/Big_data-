import numpy as np

# Create sample data
data = np.array([23, 45, 67, 89, 12, 34, 56, 78, 91, 44])
print(f"Data: {data}")

# Basic statistical functions
print(f"Mean: {np.mean(data):.2f}")
print(f"Median: {np.median(data):.2f}")
print(f"Standard Deviation: {np.std(data):.2f}")
print(f"Variance: {np.var(data):.2f}")
print(f"Minimum: {np.min(data)}")
print(f"Maximum: {np.max(data)}")
print(f"Sum: {np.sum(data)}")
print(f"Product: {np.prod(data)}")
print(f"25th Percentile: {np.percentile(data, 25)}")
print(f"75th Percentile: {np.percentile(data, 75)}")

# For 2D arrays
data_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{data_2d}")
print(f"Mean of entire array: {np.mean(data_2d):.2f}")
print(f"Mean along rows (axis=1): {np.mean(data_2d, axis=1)}")
print(f"Mean along columns (axis=0): {np.mean(data_2d, axis=0)}")
