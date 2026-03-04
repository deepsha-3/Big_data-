import pandas as pd

# Create sample data
df = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Salary': [50000, 60000, 75000, 65000, 52000, 80000, 70000, 48000],
    'Experience': [2, 5, 8, 4, 3, 10, 6, 1]
})

print("Original Data:\n", df)

# Basic groupby
dept_group = df.groupby('Department')
print("\nGroups:", dept_group.groups.keys())

# Aggregation functions
print("\nMean salary by department:")
print(df.groupby('Department')['Salary'].mean())

print("\nMultiple aggregation functions:")
print(df.groupby('Department').agg({
    'Salary': ['mean', 'min', 'max', 'count'],
    'Experience': ['mean', 'sum']
}))

print("\nSum of salaries by department:")
print(df.groupby('Department')['Salary'].sum())

print("\nDepartment statistics:")
print(df.groupby('Department').describe())

# Transformations
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
df['Salary_vs_Dept_Avg'] = df['Salary'] - df['Dept_Avg_Salary']

print("\nDataFrame with department averages:")
print(df)

# Filtering groups
print("\nDepartments with average salary > 60000:")
dept_avg = df.groupby('Department')['Salary'].mean()
print(dept_avg[dept_avg > 60000])
