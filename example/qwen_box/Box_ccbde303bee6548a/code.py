from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {
    "Library": ["City Library", "City Library", "City Library", "County Library", "County Library", "County Library", "National Library", "National Library", "National Library"],
    "Year": [2017, 2018, 2019, 2017, 2018, 2019, 2017, 2018, 2019],
    "Visitors": [12000, 9000, 9500, 8000, 6000, 7000, 15000, 12000, 13000],
    "Events": [15, 10, 20, 8, 5, 15, 20, 15, 25]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot
bp = ax.boxplot([df['Visitors'], df['Events']], patch_artist = True, notch = True, vert = 0, widths = 0.5)
 
colors = ['#0000FF', '#00FF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting the background color of the plot
ax.set_facecolor('gray')

# Adding grid
ax.grid(True)

# Adding labels and title
plt.xlabel('Data Categories')
plt.ylabel('Values')
plt.title('Library Visitors and Events')

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1]], ['Visitors', 'Events'], loc='upper right')

# Saving the plot
plt.tight_layout()
plt.savefig('myplot.png')

# Modify the box body that contains the center point of the bounding box to 'dotted' and set the rasterized state to False
for box in bp['boxes']:
    box.set_linestyle('dotted')
    box.set_rasterized(False)

# Save the modified plot
plt.savefig('Edit_figure.png')