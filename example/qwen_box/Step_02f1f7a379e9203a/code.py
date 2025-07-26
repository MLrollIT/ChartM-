import matplotlib.pyplot as plt

# Defining the coordinates 
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y = [0, 100, 200, 250, 300, 350, 400, 450, 500, 550]

# Plotting the coordinates using step plot
plt.step(x, y, where='mid')

# Setting plot title
plt.title('Flight Path Visualization Using Volumetric Data')

# Setting X-axis label
plt.xlabel('Spatial Coordinates')

# Setting Y-axis label
plt.ylabel('Altitude (feet)')

# Displaying grid
plt.grid(True)

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")