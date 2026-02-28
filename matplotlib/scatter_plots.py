# Scatter Plots
import matplotlib.pyplot as plt
import numpy as np

# Generate data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5
colors = np.random.rand(100)
sizes = np.random.rand(100) * 100

plt.figure(figsize=(12, 5))

# Basic scatter plot
plt.subplot(1, 2, 1)
plt.scatter(x, y, color='blue', alpha=0.6, edgecolor='black')
plt.title('Basic Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)

# Scatter plot with color and size variation
plt.subplot(1, 2, 2)
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, 
                      cmap='viridis', edgecolor='black')
plt.colorbar(scatter, label='Color Value')
plt.title('Scatter Plot with Color and Size')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
