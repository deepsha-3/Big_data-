import pandas as pd

df = pd.DataFrame({
   'Name': ['Riya', 'Diya', 'Max', 'Tina', 'Priya'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [50000, 60000, 75000, 55000, 68000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})

# Conditional filtering
print("Employees older than 30:")
print(df[df['Age'] > 30])

print("\nEmployees in IT department:")
print(df[df['Department'] == 'IT'])

print("\nEmployees with salary > 60000:")
print(df[df['Salary'] > 60000])

# Multiple conditions
print("\nEmployees in IT and age < 35:")
print(df[(df['Department'] == 'IT') & (df['Age'] < 35)])

print("\nEmployees in HR or with salary > 70000:")
print(df[(df['Department'] == 'HR') | (df['Salary'] > 70000)])

# Using query method
print("\nUsing query (age > 30):")
print(df.query('Age > 30'))

# isin method
print("\nEmployees in specific cities:")
print(df[df['City'].isin(['London', 'Paris', 'Tokyo'])])
