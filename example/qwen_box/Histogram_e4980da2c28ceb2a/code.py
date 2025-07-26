# import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# x-axis data, i.e., depth categories
depth_categories = ["50-100", "100-200", "200-300", "300-400", "400-500", "500-600", "600-700", "700-800", "800-900", "900-1000"]

# y-axis data, i.e., frequency of cave depths
frequency = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# Create histogram
plt.figure(figsize=(10, 5))  # handles large labels
plt.bar(depth_categories, frequency)

# add labels and title
plt.xlabel('Depth Categories in Meters')
plt.ylabel('Frequency of Cave Depths')
plt.title('Distribution of Underwater Cave Depths')

plt.xticks(rotation=45)  # makes labels readable

plt.tight_layout()
plt.savefig("figure.png")

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform([0.5, 0.5, 0.5, 0.5])

# Get the bar objects that contain the center point of the bounding box
bars = plt.gca().collections[0].get_paths()[0].vertices

# Set the animated state of the bars to True
bars.set_animated(True)

# Update the linewidth and edge color of the bars
bars.set_edgecolor('black')
bars.set_linewidth(2.65)

plt.tight_layout()
plt.savefig("Edit_figure.png")