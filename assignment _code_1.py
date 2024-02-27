import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create scatter plot
plt.figure(figsize=(8, 6))  # Set figure size
plt.scatter(x, y, color='blue', label='Data points')  # Scatter plot
plt.title('Relationship between X and Y')  # Title
plt.xlabel('X-axis', fontsize=12)  # X-axis label with adjusted font size
plt.ylabel('Y-axis', fontsize=12)  # Y-axis label with adjusted font size
plt.xticks(fontsize=10)  # Adjust X-axis tick font size
plt.yticks(fontsize=10)  # Adjust Y-axis tick font size
plt.legend()  # Show legend
plt.grid(True)  # Show grid
plt.tight_layout()  # Adjust layout to prevent overcrowding
plt.show()