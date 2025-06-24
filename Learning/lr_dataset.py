import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic data
np.random.seed(42)
x = np.linspace(1, 10, 20)
y = 1.5 * x + 4 + np.random.normal(0, 1.5, size=x.shape)

# Create DataFrame
df = pd.DataFrame({'x': x, 'y': y})

# Save to CSV
df.to_csv('Learning/res/noisy_linear_data.csv', index=False)

# Plot the data
plt.scatter(df['x'], df['y'], color='green', label='Noisy Data')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Noisy Linear Data (not through origin)')
plt.legend()
plt.grid(True)
plt.show()
