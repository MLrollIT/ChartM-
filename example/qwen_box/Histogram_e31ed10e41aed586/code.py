import matplotlib.pyplot as plt
import numpy as np

# Data
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # Representative points for each bin (range)
y = [15, 22, 30, 18, 12, 7, 5, 3, 2, 1] # Frequency of each range

# Create bins for histogram
bins = np.arange(11) - 0.5 # shifts the bins to left for correct alignment 

# Create histogram
plt.hist(x, weights=y, bins=bins, edgecolor='black')

# Add labels
plt.xlabel('Growth Rate in cm/day')
plt.ylabel('Frequency')
plt.title('Distribution of Psychedelic Mushroom Growth Rates')

# Make x-axis labels more readable
plt.xticks(range(0, 10))

# Add shadow effect to bars containing the center point of the bounding box
bbox = (2.59, 2.78) # shadow offset
shadow_color = 'gold' # shadow color
facecolor = '#fc4dec' # facecolor of the bars

# Get the bounding box of the center point of the bounding box
bbox_patch = plt.gca().patch
bbox_center = bbox_patch.get_window_extent().transformed(plt.gcf().transFigure.inverted())
bbox_center = bbox_center.get_points()

# Get the indices of the bars that contain the center point of the bounding box
indices = np.where((bbox_center[:,0] >= x[0]) & (bbox_center[:,0] <= x[-1]))[0]

# Update the facecolor of the bars
for i in indices:
    plt.bar(x[i], y[i], color=facecolor, edgecolor='black')

# Show plot
plt.tight_layout()
plt.savefig("figure.png")