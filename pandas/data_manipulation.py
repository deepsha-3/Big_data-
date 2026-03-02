import pandas as pd

df = pd.DataFrame({
    'Name': ['Riya', 'Diya', 'Max', 'Tina', 'Priya'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Kathmandu', 'Sydney'],
    'Salary': [50000, 60000, 75000, 55000, 68000]
})

print("Original DataFrame:\n", df)

# Adding new columns
df['Bonus'] = df['Salary'] * 0.1
df['Total Compensation'] = df['Salary'] + df['Bonus']
df['Age Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Senior')

print("\nDataFrame with new columns:\n", df)

# Modifying values
df.loc[df['Name'] == 'Alice', 'City'] = 'Boston'
df['Salary'] = df['Salary'] * 1.05  # 5% raise for everyone

print("\nModified DataFrame:\n", df)

# Dropping columns
df_without_bonus = df.drop('Bonus', axis=1)
print("\nDataFrame without Bonus column:\n", df_without_bonus)

# Renaming columns
df_renamed = df.rename(columns={'Name': 'Employee Name', 'City': 'Location'})
print("\nRenamed columns:\n", df_renamed.columns.tolist())
