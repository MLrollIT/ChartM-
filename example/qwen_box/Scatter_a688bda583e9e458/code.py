import matplotlib.pyplot as plt

# Data
distance = [5, 10, 15, 20, 25, 30, 35, 40, 45]
food_collected = [2, 4, 7, 9, 11, 13, 16, 18, 21]

# Create scatter plot
plt.scatter(distance, food_collected, color='r')

# Add title and labels to the axes
plt.title('Foraging Behavior of Ant Colony')
plt.xlabel('Distance Traveled (mm)')
plt.ylabel('Food Collected (mg)')

# Modify the shape of the points that contain the center point of the bounding box to a triangle
plt.scatter([20, 30, 40], [10, 13, 18], color='r', marker='^')

# Show the plot

plt.tight_layout()
plt.savefig("Edit_figure.png")