# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the ranges and their frequencies
ranges = ['0-50', '51-100', '101-150', '151-200', '201-250', '251-300']
frequencies = [12, 9, 17, 6, 3, 1]

# Set the figure size for better visibility
plt.figure(figsize=[10,8])

# Create the histogram
plt.hist(ranges, bins=6, weights=frequencies, alpha=0.6, color='skyblue', edgecolor='black')

# Label the axes and title
plt.xlabel('Depth Ranges in Meters', fontsize=14)
plt.ylabel('Frequency of Caves Found', fontsize=14)
plt.title('Histogram of Underwater Cave Depths Explored by Sonar', fontsize=16)

# Add a shadow effect to the bars that contain the center point of the bounding box
bbox = (101, 150, 150, 200)
plt.bar([bbox[0]], [bbox[1]], color='gold', edgecolor='black', alpha=0.6, bottom=bbox[2], width=bbox[3], label='Shadowed Bar')

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")