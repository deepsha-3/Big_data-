import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]
errors = [2, 3, 4, 5, 2]

# Simple bar chart
plt.figure(figsize=(10, 5))
plt.bar(categories, values, color='skyblue', edgecolor='navy', alpha=0.7)
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(True, alpha=0.3, axis='y')
plt.show()

# Bar chart with error bars
plt.figure(figsize=(10, 5))
plt.bar(categories, values, yerr=errors, capsize=5, 
        color='lightcoral', edgecolor='darkred', alpha=0.7)
plt.title('Bar Chart with Error Bars')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(True, alpha=0.3, axis='y')
plt.show()

# Horizontal bar chart
plt.figure(figsize=(10, 5))
plt.barh(categories, values, color='lightgreen', edgecolor='darkgreen')
plt.title('Horizontal Bar Chart')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.grid(True, alpha=0.3, axis='x')
plt.show()
