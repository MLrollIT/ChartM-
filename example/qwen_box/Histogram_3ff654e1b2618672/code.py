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

# add shadow below the bars that contain the center point of the bounding box
for i in range(6, 10):
    plt.bar(depth_categories[i], frequency[i], bottom=frequency[i-6], color='blue', edgecolor='black', hatch='/', linewidth=1.16, linestyle='dashed', label='Shadow')

plt.tight_layout()
plt.savefig("figure.png")