
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
data = np.random.normal(100, 15, 1000)  # 1000 points, mean=100, std=15

plt.figure(figsize=(12, 5))

# Simple histogram
plt.subplot(1, 2, 1)
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histogram (30 bins)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# Histogram with density plot
plt.subplot(1, 2, 2)
plt.hist(data, bins=30, density=True, color='lightcoral', 
         edgecolor='black', alpha=0.7, label='Histogram')

# Add density curve
from scipy import stats
x = np.linspace(data.min(), data.max(), 100)
pdf = stats.norm.pdf(x, np.mean(data), np.std(data))
plt.plot(x, pdf, 'b-', linewidth=2, label='Normal Distribution')

plt.title('Histogram with Density Curve')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
