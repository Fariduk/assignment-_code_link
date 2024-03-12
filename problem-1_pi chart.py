import matplotlib.pyplot as plt

# Define data for the pie chart
sizes = [3, 7]  # Sizes of the slices
labels = ['Point 1', 'Point 2']  # Labels for the slices

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen'])

# Add a title
plt.title('Pie Chart')

# Show the plot
plt.show()
