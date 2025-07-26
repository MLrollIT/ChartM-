from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Define the data
data = {
    "Refrigerator": [10, 12, 10, 8, 9],
    "Air Conditioner": [3, 5, 10, 2, 3],
    "Washing Machine": [5, 7, 7, 6, 10],
    "Dishwasher": [1, 1, 5, 1, 1],
    "Microwave": [2, 3, 3, 5, 6]
}

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(data.values(), patch_artist = True, notch = True, vert = 0, 
                labels = data.keys(), widths=0.5, sym='b+')

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels for axes
ax.set_xlabel("Appliance")
ax.set_ylabel("Usage")
plt.title("Box Plot of Appliance Usage")

# Add a grid
ax.grid(True)

# Change the background color
ax.set_facecolor('lightgray')

# Annotate the data value on the chart figure
for line, value in zip(bp['medians'], data.values()):
    x, y = line.get_xydata()[1]
    ax.annotate(f'{np.median(value)}', xy=(x, y))

# Modify the box body that contain the center point of the bounding box
for box in bp['boxes']:
    # get the median of the box
    median = np.median(box.get_ydata())
    # set the alpha transparency of the box body to 0.6602
    box.set_alpha(0.6602)
    # set the fill color to #2602c8
    box.set_facecolor('#2602c8')
    # set the border of the box to be solid with a width of 2.3 and a color of #58f761
    box.set_edgecolor('#58f761')
    box.set_linewidth(2.3)

plt.tight_layout()
plt.savefig("myplot.png")