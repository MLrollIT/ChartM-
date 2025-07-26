import matplotlib.pyplot as plt
import numpy as np

# Center points of ranges for the X-axis (Tree Density per sq. km)
x = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475]

# Data points for the Y-axis (Frequency of Occurrences)
w = [10, 15, 20, 25, 30, 25, 20, 15, 10, 5]

# Plot histogram
plt.hist(x, bins=10, weights=w, color='skyblue')

# set labels for better readability
plt.xlabel('Tree Density per sq. km')
plt.ylabel('Frequency of Occurrences')
plt.title('Jungle Canopy Density Distribution Pattern')
plt.tight_layout()

# Set the facecolor of the bars that contain the center point of the bounding box to #f08903 and change the linestyle to 'dashed'
for i in range(1, len(x)):
    if x[i] == 200:
        plt.bar(x[i-1], w[i-1], color='#f08903', linestyle='dashed')
    elif x[i] == 150:
        plt.bar(x[i-1], w[i-1], color='#f08903', linestyle='dashed')
    elif x[i] == 100:
        plt.bar(x[i-1], w[i-1], color='#f08903', linestyle='dashed')

plt.savefig("Edit_figure.png")