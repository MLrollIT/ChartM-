import matplotlib.pyplot as plt
import numpy as np

# Age groups
age_18_24 = [1000, 1200, 800, 1500, 1100]
age_25_34 = [1500, 1800, 900, 2000, 1300]
age_35_44 = [900, 1000, 700, 1200, 800]
age_45_54 = [500, 600, 300, 700, 400]

# The labels for the viral videos
labels = ['Video 1', 'Video 2', 'Video 3', 'Video 4', 'Video 5']

# Plot the data using a stack plot
fig, ax = plt.subplots()

ax.stackplot(labels, age_18_24, age_25_34, age_35_44, age_45_54, labels=['18-24','25-34','35-44','45-54'], colors=['blue', 'orange', 'green', 'purple'])

# Set the x and y labels
ax.set_xlabel('Viral Videos')
ax.set_ylabel('Number of Views')

# Add a title
ax.set_title('Distribution of Viral Video Views by Demographics')

# Add legend
ax.legend(loc='upper left')

# Modify the area containing the center point of the bounding box
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((0.35, 0.35))
bbox = ax.bbox_to_anchor((