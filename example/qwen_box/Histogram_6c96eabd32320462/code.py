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

# Add glow effect to bars containing the center point of the bounding box
bbox = dict(boxstyle="square", fc="#02fa10", alpha=0.257)
for i in range(1, len(x)):
    if x[i] == 200 or x[i] == 300:
        plt.bar(x[i], w[i], color='skyblue', edgecolor='black', linewidth=2, label='Center Point', alpha=0.5, hatch='//', bottom=w[i-1], align='center', zorder=2, boxstyle=bbox)
    else:
        plt.bar(x[i], w[i], color='skyblue', edgecolor='black', linewidth=2, bottom=w[i-1], align='center', zorder=2)

plt.savefig("Edit_figure.png")