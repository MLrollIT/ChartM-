import matplotlib.pyplot as plt
import numpy as np

# specify the data points
depth_ranges = ['0-5', '6-10', '11-15', '16-20', '21-25']
frequency = [12, 8, 15, 10, 5]

# plot the histogram
plt.figure(figsize=[10,8])
plt.bar(depth_ranges, frequency, color='skyblue')

# set plot title and labels
plt.title('Distribution of Coral Species Within Different Depth Zones')
plt.xlabel('Depth Ranges (in Meters)')
plt.ylabel('Frequency of Coral Species')

# modify the height of the bars that include the center point of the bounding box
bbox = plt.gca().get_position().bounds
bbox = [bbox[0], bbox[1], bbox[2], 1.4 * bbox[3]]
plt.gca().set_position(bbox)

# display the plot
plt.tight_layout()
plt.savefig("figure.png")