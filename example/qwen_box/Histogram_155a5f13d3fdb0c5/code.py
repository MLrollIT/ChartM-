# necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# data points
cell_size = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
frequency = np.array([15, 20, 30, 35, 45, 50, 40, 25, 20, 10])

# creating histogram using hist() function
plt.hist(cell_size, weights=frequency, bins=10, edgecolor='black')

# label for x and y axis
plt.xlabel('Cell Size (in micrometers)')
plt.ylabel('Frequency')

# Plot title
plt.title('Histogram for Microscopic Cell Size Distribution')

# show the histogram
plt.tight_layout()
plt.savefig("figure.png")

# modify the object in the chart
# apply a shadow effect to the bars that contain the center point of the bounding box
# with a shadow offset of (2.28, 3.96) and a shadow color of gray
# make these bars invisible by setting their visibility to False
bbox = plt.gca().get_position().bounds
bbox = [bbox[0] + 2.28, bbox[1] + 3.96, bbox[2], bbox[3]]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], facecolor='none', edgecolor='gray', linewidth=2, alpha=0.5, zorder=10))
plt.gca().set_visible(False)