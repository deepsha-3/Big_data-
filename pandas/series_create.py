import pandas as pd
import numpy as np

# Creating Series from different sources
s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s3 = pd.Series({'A': 100, 'B': 200, 'C': 300})
s4 = pd.Series(np.random.randn(5))

print("Series from list:\n", s1)
print("\nSeries with custom index:\n", s2)
print("\nSeries from dictionary:\n", s3)
print("\nSeries from NumPy array:\n", s4)

# Series operations
print(f"\nFirst element: {s2['a']}")
print(f"Values > 3: {s2[s2 > 3]}")
print(f"Mean: {s2.mean()}")
print(f"Sum: {s2.sum()}")
