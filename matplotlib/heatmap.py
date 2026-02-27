import matplotlib.pyplot as plt
import numpy as np

# Generate correlation matrix
np.random.seed(42)
data = np.random.randn(100, 5)
correlation_matrix = np.corrcoef(data.T)

plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label='Correlation Coefficient')
plt.title('Correlation Heatmap')

# Add labels
variables = ['Var1', 'Var2', 'Var3', 'Var4', 'Var5']
plt.xticks(range(len(variables)), variables)
plt.yticks(range(len(variables)), variables)

# Add correlation values
for i in range(len(variables)):
    for j in range(len(variables)):
        plt.text(j, i, f'{correlation_matrix[i, j]:.2f}', 
                ha='center', va='center', color='white' if abs(correlation_matrix[i, j]) > 0.5 else 'black')

plt.show()

