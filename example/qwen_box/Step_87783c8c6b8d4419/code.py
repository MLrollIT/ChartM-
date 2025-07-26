import matplotlib.pyplot as plt

# Specify the values of spatial positions
x = [-3, -2, -1, 0, 1, 2, 3]

# Specify the values of probability amplitudes
y = [0.1, 0.5, 0.8, 1.0, 0.8, 0.5, 0.1]

# Create a step plot
plt.step(x, y, where='mid')

# Add a title to the plot
plt.title('Quantum Particle Wave Function Visualization')

# Add a label to the x-axis
plt.xlabel('Spatial Positions')

# Add a label to the y-axis
plt.ylabel('Probability Amplitudes')

# Add a grid to the plot
plt.grid(True)

# Add a marker to the data points that contain the center point of the bounding box
plt.plot(1, 0.8, marker='o', markersize=17.31)

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")