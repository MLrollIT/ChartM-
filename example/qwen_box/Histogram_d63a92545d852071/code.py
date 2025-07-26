import matplotlib.pyplot as plt
import numpy as np

# Defining the dataset
elevation_values = [150, 300, 450, 600, 900, 1200, 1550, 1800, 2150, 2450, 2700, 2950]

# Create bins for the range of elevation values
bins = np.arange(0,3001,300) 

# Setting plot size
plt.figure(figsize=(10,7))

# Making the histogram
plt.hist(elevation_values, bins=bins, edgecolor='black', alpha=0.7)

# Setting plot labels and title
plt.xlabel('Elevation (in meters)', fontsize=13)
plt.ylabel('Frequency', fontsize=13)
plt.title('Distribution of Elevations in Geological Layers', fontsize=15)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform(np.array([[750, 0], [750, 1000]]))

# Get the bar objects that contain the center point of the bounding box
bars = plt.gca().collections[0].get_paths()[bbox.transformed(plt.gca().transData).get_points()]

# Set the line color of the bars to #fa7b54
bars.set_edgecolor('#fa7b54')

# Set the visibility of the bars to False
bars.set_visible(False)

plt.tight_layout()
plt.savefig("Edit_figure.png")