import pandas as pd
import numpy as np

# Create a sample dataset with various data types
np.random.seed(42)
n_rows = 1000

df = pd.DataFrame({
    'ID': range(1, n_rows + 1),
    'Name': [f'Customer_{i}' for i in range(1, n_rows + 1)],
    'Age': np.random.randint(18, 70, n_rows),
    'Gender': np.random.choice(['M', 'F'], n_rows),
    'Income': np.random.normal(50000, 15000, n_rows).round(0),
    'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_rows),
    'City': np.random.choice(['New York', 'London', 'Paris', 'Tokyo', 'Sydney'], n_rows),
    'Purchase_Amount': np.random.exponential(100, n_rows).round(2),
    'Purchase_Date': pd.date_range('2023-01-01', periods=n_rows, freq='D'),
    'Customer_Satisfaction': np.random.choice([1, 2, 3, 4, 5], n_rows),
    'Is_Active': np.random.choice([True, False], n_rows, p=[0.8, 0.2])
})

# Add some missing values
df.loc[np.random.choice(n_rows, 50), 'Income'] = np.nan
df.loc[np.random.choice(n_rows, 30), 'Age'] = np.nan

print("Dataset created with shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# 1. Basic Information
print("\n" + "="*50)
print("BASIC INFORMATION")
print("="*50)
print("\nDataFrame Info:")
print(df.info())

print("\nDataFrame Shape:", df.shape)
print("Number of Rows:", len(df))
print("Number of Columns:", len(df.columns))
print("Column Names:", df.columns.tolist())

