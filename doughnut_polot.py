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

# Count the occurrences of each value in the last column (assuming it represents the categories)
categories = {}
for row in data:
    categories[row[-1]] = categories.get(row[-1], 0) + 1

# Extract labels and sizes for the doughnut plot
labels = ['Inactive', 'Active']
sizes = [categories.get(0, 0), categories.get(1, 0)]

# Create a doughnut plot
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))

# Add a circle in the center to make it a doughnut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
plt.title('Doughnut Plot of Active vs Inactive')

# Show the plot
plt.show()
