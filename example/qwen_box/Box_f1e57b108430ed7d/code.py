from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Import data
data = {'Year': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Pop': [100, 120, 150, 200, 180, 190, 210, 230, 240],
        'Rock': [80, 70, 60, 50, 90, 80, 70, 150, 160],
        'Classical': [120, 130, 140, 100, 120, 110, 90, 80, 70]}

df = pd.DataFrame(data)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot([df['Pop'], df['Rock'], df['Classical']], patch_artist = True,
                notch = True, vert = 0, widths = 0.5, labels = ['Pop', 'Rock', 'Classical'])
colors = ['#0000FF', '#00FF00', '#FF0000']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Adding title and labels
plt.title('Music Genre Popularity Over Years')
plt.xlabel('Genre')
plt.ylabel('Popularity')

# Adding grid
ax.grid(True)

# Changing the background color of the figure
ax.set_facecolor('lightgray')

# Save the plot
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the object in the chart
for box in bp['boxes']:
    # Change outline color
    box.set(linewidth=2)
    # Change fill color
    box.set(facecolor='white')
    # Change color and linewidth of the whiskers
    for whisker in box['whiskers']:
        whisker.set(color="black", linewidth=2)
    # Change color and linewidth of the caps
    for cap in box['caps']:
        cap.set(color="black", linewidth=2)
    # Change color and linewidth of the median lines
    for median in box['medians']:
        median.set(color="black", linewidth=2)
    # Change the color and linewidth of the box
    for box in box['boxes']:
        box.set(color="black", linewidth=2)

# Change the picker state of the box that contains the center point of the bounding box to True
for box in bp['boxes']:
    box.set_picker(True)

# Set the visibility of the corresponding box body to False for those same points
for box in bp['boxes']:
    box.set_visible(False)

# Save the modified plot
plt.tight_layout()
plt.savefig("Edit_figure.png")