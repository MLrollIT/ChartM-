import matplotlib.pyplot as plt
import numpy as np

# Data points for energy consumption levels and frequencies
energy_levels = ['100-500 GWh', '500-1000 GWh', '1000-1500 GWh', '1500-2000 GWh', '2000-2500 GWh']
frequencies = [20, 35, 25, 15, 10]

# Plotting the histogram
plt.bar(energy_levels, frequencies, color='blue')

# Labeling the axes
plt.xlabel('Energy Consumption Levels (GWh)', fontsize=12)
plt.ylabel('Number of Countries', fontsize=12)

# Setting the title
plt.title('Energy Consumption Trends Over 10 Years', fontsize=16)

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to