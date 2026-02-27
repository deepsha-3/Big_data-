import pandas as pd
import numpy as np

# Create sample data for demonstration
# CSV file
df_csv = pd.DataFrame({
    'ID': range(1, 11),
    'Name': [f'Person_{i}' for i in range(1, 11)],
    'Age': np.random.randint(20, 60, 10),
    'Salary': np.random.randint(30000, 100000, 10)
})

# Save to CSV
df_csv.to_csv('sample_data.csv', index=False)
print("CSV file created: sample_data.csv")

# Read CSV
df_from_csv = pd.read_csv('sample_data.csv')
print("\nData from CSV:")
print(df_from_csv.head())

# Excel file (requires openpyxl or xlrd)
df_csv.to_excel('sample_data.xlsx', index=False, sheet_name='Sheet1')
print("\nExcel file created: sample_data.xlsx")

# Read Excel
df_from_excel = pd.read_excel('sample_data.xlsx', sheet_name='Sheet1')
print("\nData from Excel:")
print(df_from_excel.head())

# JSON file
df_csv.to_json('sample_data.json', orient='records')
print("\nJSON file created: sample_data.json")

# Read JSON
df_from_json = pd.read_json('sample_data.json')
print("\nData from JSON:")
print(df_from_json.head())
