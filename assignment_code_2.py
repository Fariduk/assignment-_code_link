import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 30, 35, 40]

# Create bar chart
plt.figure(figsize=(8, 6))  # Set figure size
plt.bar(categories, values, color='skyblue')  # Bar chart
plt.title('Comparison of Categories')  # Title
plt.xlabel('Categories', fontsize=12)  # X-axis label with adjusted font size
plt.ylabel('Values', fontsize=12)  # Y-axis label with adjusted font size
plt.xticks(fontsize=10, rotation=45)  # Adjust X-axis tick font size and rotate labels for better readability
plt.yticks(fontsize=10)  # Adjust Y-axis tick font size
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Show grid lines for Y-axis
plt.tight_layout()  # Adjust layout to prevent overcrowding
plt.show()
