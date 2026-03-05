import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Deepsha', 'Karan', 'Max', 'Abel'],
    'Department': ['HR', 'IT', 'Finance', 'IT']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Salary': [50000, 60000, 75000, 55000],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
})

df3 = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 4],
    'Project': ['P1', 'P2', 'P1', 'P3']
})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)
print("\nDataFrame 3:\n", df3)

# Inner join
inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner Join (only matching IDs):\n", inner_merge)

# Left join
left_merge = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join (all from df1):\n", left_merge)

# Right join
right_merge = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join (all from df2):\n", right_merge)

# Outer join
outer_merge = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Join (all from both):\n", outer_merge)

# Merge on different column names
merge_diff = pd.merge(df1, df3, left_on='ID', right_on='Emp_ID')
print("\nMerge on different columns:\n", merge_diff)

# Concatenation
df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nConcatenate vertically:\n", df_concat)

df_concat_h = pd.concat([df1, df3], axis=1)
print("\nConcatenate horizontally:\n", df_concat_h)
