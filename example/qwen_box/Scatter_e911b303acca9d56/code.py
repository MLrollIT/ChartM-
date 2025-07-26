import matplotlib.pyplot as plt

# Depth measurements in meters
depth = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

# Corresponding elevation changes in meters
elevation_change = [0, -100, -200, -300, -400, -500, -600, -700, -800, -900]

# Create the scatter plot
plt.scatter(depth, elevation_change, color='b')

# Adding labels and title
plt.xlabel('Depth (meters)')
plt.ylabel('Elevation Change (meters)')
plt.title('Ocean Floor Elevation Changes Based on Depth')

# Show the plot
plt.grid(True)

# Modify the edge color and width of the points that contain the center point of the bounding box
bbox = plt.gca().bbox_to_transform((0.5, 0.5))
plt.scatter([0.5], [0.5], color='b', edgecolor='#37d5a4', linewidth=2.7)

# Save the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")