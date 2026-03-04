import pandas as pd
import numpy as np

# Create DataFrame with missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [np.nan, np.nan, np.nan, 4, 5]
})

print("Original DataFrame with missing values:\n", df)

# Checking for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nTotal missing values:", df.isnull().sum().sum())

# Dropping missing values
print("\nDrop rows with any missing values:")
print(df.dropna())

print("\nDrop rows where all values are missing:")
print(df.dropna(how='all'))

print("\nDrop columns with any missing values:")
print(df.dropna(axis=1))

# Filling missing values
print("\nFill missing values with 0:")
print(df.fillna(0))

print("\nFill missing values with column mean:")
print(df.fillna(df.mean()))

print("\nForward fill (propagate last valid observation):")
print((df.ffill()))

print("\nBackward fill:")
print((df.bfill()))

# Interpolation
print("\nInterpolate missing values:")
print(df.interpolate())
