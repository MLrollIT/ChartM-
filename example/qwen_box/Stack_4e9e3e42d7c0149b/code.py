import matplotlib.pyplot as plt
import numpy as np

# Define data points
months = ['January', 'February', 'March', 'April', 'May']
video1 = [10, 15, 20, 8, 12]
video2 = [7, 9, 14, 6, 10]
video3 = [5, 6, 8, 3, 4]
video4 = [3, 5, 7, 2, 3]
video5 = [2, 3, 5, 1, 2]

# Create a stack plot
plt.stackplot(months, video1, video2, video3, video4, video5, labels=['Video 1', 'Video 2', 'Video 3', 'Video 4', 'Video 5'])

# Add labels and title
plt.xlabel('Months')
plt.ylabel('Cumulative Number of Views (millions)')
plt.title('Viral Video Sensations Over Time')

# Show the legend
plt.legend(loc='upper left')

# Modify the linewidth of the area that contains the center point of the bounding box to 0.93
bbox = plt.gca().get_position().get_points()
bbox[0, 0] = 0.3
bbox[1, 0] = 0.7
bbox[0, 1] = 0.5
bbox[1, 1] = 0.7
plt.gca().set_position(bbox)

# Disable the picker state for that area
plt.gca().picker = False

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")