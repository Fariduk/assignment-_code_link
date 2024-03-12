import matplotlib.pyplot as plt

# Define the points
x1, y1 = 3, 5
x2, y2 = 7, 2

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the points
ax.plot(x1, y1, 'o', markersize=8, color='black', label='Point 1')
ax.plot(x2, y2, 'o', markersize=8, color='black', label='Point 2')

# Plot the line passing through both points
# Find the slope and intercept of the line
slope = (y2 - y1) / (x2 - x1)
intercept = y1 - slope * x1

# Define the x values for the line
x_values = [x1, x2]

# Define the corresponding y values for the line using the equation of the line
y_values = [slope * x + intercept for x in x_values]

# Plot the line
ax.plot(x_values, y_values, '-', linewidth=2, color='black', label='Line')

# Set the range for both x and y axes
ax.set_xlim(0, 10)  # Adjust as needed
ax.set_ylim(0, 8)   # Adjust as needed

# Label the axes
ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Y', fontsize=14)

# Set the font size for tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Add a grid
ax.grid(True)

# Add legend
ax.legend(fontsize=12)

# Show the plot
plt.show()
