import matplotlib.pyplot as plt

# Datasets
iteration_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elevation = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a scatter plot
plt.scatter(iteration_number, elevation)

# Add labels to the axes
plt.xlabel("Iteration Number")
plt.ylabel("Elevation (meters)")

# Add a title to the plot
plt.title("Fractal landscape generation process")

# Modify the size of the points that contain the center point of the bounding box to 84
plt.scatter([5], [60], s=84)

# Display the plot

plt.tight_layout()
plt.savefig("Edit_figure.png")