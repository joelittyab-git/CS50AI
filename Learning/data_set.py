import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(0)

# Generate class 0 (label = 0)
x1_class0 = np.random.normal(2, 0.5, 50)
x2_class0 = np.random.normal(2, 0.5, 50)
y_class0 = np.zeros(50)

# Generate class 1 (label = 1)
x1_class1 = np.random.normal(4, 0.5, 50)
x2_class1 = np.random.normal(4, 0.5, 50)
y_class1 = np.ones(50)

# Combine the data
x1 = np.concatenate([x1_class0, x1_class1])
x2 = np.concatenate([x2_class0, x2_class1])
y = np.concatenate([y_class0, y_class1])

# Create a DataFrame
df = pd.DataFrame({
    'x1': x1,
    'x2': x2,
    'y': y
})

# Save to CSV
df.to_csv("perceptron_regression_dataset.csv", index=False)

# Plot
plt.scatter(df[df.y == 0].x1, df[df.y == 0].x2, color='blue', label='Class 0')
plt.scatter(df[df.y == 1].x1, df[df.y == 1].x2, color='red', label='Class 1')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Linearly Separable Data')
plt.legend()
plt.grid(True)
plt.show()
