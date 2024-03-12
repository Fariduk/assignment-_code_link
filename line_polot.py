import matplotlib.pyplot as plt

# Provided data
data = [
    [7.882365, 2.451059, 10.333424, 1],
    [7.802009, 2.871678, 10.673688, 1],
    [6.773546, 3.206522, 9.980068, 1],
    [7.520603, 2.587964, 10.108567, 0],
    [7.180145, 2.786635, 10.96678,1],
    [9.09601,2.851705,11.947715 ,1],
    [7.162053,  2.256303, 9.418356,0],
    [5.377034,  3.266608, 8.643642,1],
    [6.66821,   2.643383, 9.311593,1],
    [6.981954,  3.214644, 10.196598,1],
    [7.145822,  2.539955, 9.685777,0],
    [6.08287,   2.688748, 8.771618,1],
    [7.553989,  2.827967, 10.381956,1],
    [6.898539,  3.010729, 9.909268,1],
    [7.217321,  2.366199, 9.58352,0],
    [6.7331,    2.728312, 9.461412,0],
    # Add more data rows as needed
]

# Extract x and y values from each row
x_values = range(len(data))
y_values = [row[1] for row in data]

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Row', fontsize=14)
plt.ylabel('Y Values', fontsize=14)
plt.title('Line Plot of Data by Row', fontsize=16)

# Show the plot
plt.show()

