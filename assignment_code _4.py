import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Perform data analysis (in this case, fitting a polynomial curve)
coefficients = np.polyfit(x, y, 3)
p = np.poly1d(coefficients)

# Plot the data and the fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Data', color='blue')
plt.plot(x, p(x), label='Fitted Curve', color='red')
plt.title('Example Data Analysis with Fitted Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
