from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {'Age Group': ['15-24', '25-34', '35-44', '45-54', '55-64', '65+'],
        'Fast Food Consumption': [50, 45, 60, 35, 70, 55]}

df = pd.DataFrame(data)

# Prepare data for box plot
plot_data = [df['Fast Food Consumption']]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = ['Fast Food Consumption'], 
                sym = "go", widths = 0.4)

colors = ['#00FF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Fast Food Consumption by Age Group")
plt.xlabel("Consumption")
plt.ylabel("Age Group")

# Adding legend
plt.legend([bp["boxes"][0]], ['Fast Food Consumption'], loc='upper right')

# Adding grid
plt.grid(True)

# Change the facecolor of the figure
fig.patch.set_facecolor('gray')

# Modify the transparency of the boxes that contain the center point of the bounding box to 0.30
for box in bp['boxes']:
    # get the index of the current box
    box_index = bp['boxes'].index(box)
    # get the center point of the box
    center_point = box.get_center()
    # get the width and height of the box
    width, height = box.get_width(), box.get_height()
    # get the coordinates of the center point of the box
    x, y = center_point
    # get the coordinates of the top left corner of the box
    left, bottom = x - width/2, y - height/2
    # get the coordinates of the bottom right corner of the box
    right, top = x + width/2, y + height/2
    # create a rectangle with the center point of the box as the top left corner
    rect = plt.Rectangle((left, bottom), width, height, facecolor=color, alpha=0.30, animated=False)
    # add the rectangle to the plot
    ax.add_patch(rect)

plt.tight_layout()
plt.savefig("myplot.png")