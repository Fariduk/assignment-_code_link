import matplotlib.pyplot as plt

def create_statistical_graph(data, title, x_label, y_label):
    """
    Function to create a statistical graph (e.g., histogram) using matplotlib.

    Parameters:
        data (list or array): The data points for the graph.
        title (str): The title of the graph.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))  # Set figure size
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')  # Histogram
    plt.title(title)  # Title
    plt.xlabel(x_label)  # X-axis label
    plt.ylabel(y_label)  # Y-axis label
    plt.grid(True)  # Show grid
    plt.tight_layout()  # Adjust layout to prevent overcrowding
    plt.show()

# Example usage:
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
title = 'Statistical Graph Example'
x_label = 'Data Points'
y_label = 'Frequency'

create_statistical_graph(data, title, x_label, y_label)