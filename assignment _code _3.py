import matplotlib.pyplot as plt
import seaborn as sns  # Seaborn is a statistical data visualization library

# Sample data or import your own data
data = ...  # Your data here

# Create the statistical graph
plt.figure(figsize=(8, 6))  # Set figure size
# Code to create the statistical graph using seaborn or matplotlib

plt.title('Title of the Graph', fontsize=14)  # Title with adjusted font size
plt.xlabel('X-axis Label', fontsize=12)  # X-axis label with adjusted font size
plt.ylabel('Y-axis Label', fontsize=12)  # Y-axis label with adjusted font size
plt.xticks(fontsize=10)  # Adjust X-axis tick font size
plt.yticks(fontsize=10)  # Adjust Y-axis tick font size
# Additional customization options like legends, grid, etc.

plt.tight_layout()  # Adjust layout to prevent overcrowding
plt.show()
