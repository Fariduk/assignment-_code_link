import numpy as np
import matplotlib.pyplot as plt

def visualize_data(data):
    """
    Function to visualize data using a histogram and calculate basic descriptive statistics.

    Parameters:
        data (array-like): The input data.

    Returns:
        None
    """
    # Calculate basic descriptive statistics
    mean_value = np.mean(data)
    median_value = np.median(data)
    std_dev = np.std(data)
    min_value = np.min(data)
    max_value = np.max(data)

    # Create a histogram
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.title('Histogram of Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Print basic descriptive statistics
    print("Basic Descriptive Statistics:")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Minimum Value: {min_value}")
    print(f"Maximum Value: {max_value}")

# Example usage:
data = np.random.normal(loc=0, scale=1, size=1000)  # Generate random data from a normal distribution
visualize_data(data)