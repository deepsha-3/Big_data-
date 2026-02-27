# Pie Charts
import matplotlib.pyplot as plt

# Sample data
sizes = [30, 25, 20, 15, 10]
labels = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'orange']
explode = (0.1, 0, 0, 0, 0)  # explode the 1st slice

plt.figure(figsize=(10, 5))

# Simple pie chart
plt.subplot(1, 2, 1)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular
plt.title('Simple Pie Chart')

# Exploded pie chart
plt.subplot(1, 2, 2)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('Exploded Pie Chart with Shadow')

plt.tight_layout()
plt.show()
