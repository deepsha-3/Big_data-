import matplotlib.pyplot as plt
import numpy as np

# Generate multiple datasets
np.random.seed(42)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(80, 5, 200)
data4 = np.random.normal(120, 15, 200)

data = [data1, data2, data3, data4]
labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

plt.figure(figsize=(10, 6))
box = plt.boxplot(data, labels=labels, patch_artist=True)

# Customize colors
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Box Plot Comparison')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.grid(True, alpha=0.3, axis='y')
plt.show()
