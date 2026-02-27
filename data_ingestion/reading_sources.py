import pandas as pd
import io

# 1. Reading from string (simulating text data)
data_string = """ID,Name,Age,Salary
1,Diya,25,50000
2,Kartik,30,60000
3,Dipisha,22,75000
4,Karan,25,55000"""

df_from_string = pd.read_csv(io.StringIO(data_string))
print("Data from string:")
print(df_from_string)

# 2. Reading from clipboard (commented as it requires actual clipboard data)
# df_from_clipboard = pd.read_clipboard()
# print(df_from_clipboard)

# 3. Reading from URL (example with GitHub raw data)
try:
    url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
    df_from_url = pd.read_csv(url)
    print("\nData from URL (first 5 rows):")
    print(df_from_url.head())
except:
    print("\nURL read failed (might need internet connection)")
