import pandas as pd

# Creating DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Kathmandu', 'Sydney'],
    'Salary': [50000, 60000, 75000, 55000, 68000]
}

df = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df)

# Creating DataFrame from list of lists
data2 = [
    ['Dipisha', 25, 'New York', 50000],
    ['Basanta', 30, 'London', 60000],
    ['Darshan', 35, 'Paris', 75000]
]
df2 = pd.DataFrame(data2, columns=['Name', 'Age', 'City', 'Salary'])
print("\nDataFrame from list:\n", df2)

# Creating DataFrame from NumPy array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'], index=['Row1', 'Row2', 'Row3'])
print("\nDataFrame from NumPy array:\n", df3)
