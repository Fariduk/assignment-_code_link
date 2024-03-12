import matplotlib.pyplot as plt

# Data
data = [
    [6.740513, 2.623066, 9.363579, 0],
    [6.405758, 3.271373, 9.677131, 1],
    [8.046769, 2.752229, 10.798998, 1],
    # Add more rows...
]

# Extracting columns
var1 = [row[0] for row in data]
var2 = [row[1] for row in data]

# Plotting the points
plt.plot(var1, var2, 'o', markersize=8)

# Labeling axes
plt.xlabel('var1', fontsize=14)
plt.ylabel('var2', fontsize=14)

# Adding grid
plt.grid(True)

# Displaying the plot
plt.show()
