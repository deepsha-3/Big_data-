import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Riya', 'Diya', 'Max', 'Tina', 'Priya'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [50000, 60000, 75000, 55000, 68000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})

print("Original DataFrame:\n", df)

# Basic information
print("\nDataFrame Info:")
print(df.info())

print("\nDataFrame Shape:", df.shape)
print("Column Names:", df.columns.tolist())
print("Index:", df.index.tolist())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# First and last few rows
print("\nFirst 3 rows:\n", df.head(3))
print("\nLast 2 rows:\n", df.tail(2))

# Selecting columns
print("\nSingle column (Name):\n", df['Name'])
print("\nMultiple columns:\n", df[['Name', 'Age', 'Salary']])

# Selecting rows
print("\nFirst row (iloc):\n", df.iloc[0])
print("\nRows 1-3 (iloc):\n", df.iloc[1:4])
print("\nRow with index 2 (loc):\n", df.loc[2])
