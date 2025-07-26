import matplotlib.pyplot as plt
import numpy as np

# Data
vortex_strength_intervals_midpoints = [0.15, 0.25, 0.35, 0.45]
frequency = [12, 18, 15, 9]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a bar plot
ax.bar(vortex_strength_intervals_midpoints, frequency, width=0.1)

# Set the x-axis labels as intervals
ax.set_xticks([0.15, 0.25, 0.35, 0.45])
ax.set_xticklabels(['0.1-0.2', '0.2-0.3', '0.3-0.4', '0.4-0.5'])

# Set the title and labels
ax.set_title('Magnitude Distribution of Vortex Strengths within Ocean Vortex Dynamics')
ax.set_xlabel('Vortex Strength Intervals')
ax.set_ylabel('Frequency of Occurrence')

# Set the clip box for the bars that contain the center point of the bounding box
bbox = plt.Bbox([[383, 477], [383 + 755, 477 + 504]])
ax.bbox_to_clip_path(bbox)

# Make the bars with the center point of the bounding box invisible
ax.set_visible(False)

# Render the plot
plt.tight_layout()
plt.savefig("figure.png")