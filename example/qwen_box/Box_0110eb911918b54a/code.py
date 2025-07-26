from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {"Disaster Type":["Flood","Drought","Earthquake"],
        "Economic Impact in Year 1":[100,150,120],
        "Economic Impact in Year 2":[50,80,200]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize = (10, 7))

# Creating box plot with customized labels
bp = ax.boxplot([df["Economic Impact in Year 1"], df["Economic Impact in Year 2"]], patch_artist = True,
                notch = True, vert = 0, labels = ["Economic Impact in Year 1", "Economic Impact in Year 2"],
                widths = 0.4, sym='gD')

colors = ['#0000FF', '#00FF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting title and labels with increased font size
ax.set_title('Economic Impact of Disasters', fontsize=18)
ax.set_xlabel('Years', fontsize=14)
ax.set_ylabel('Economic Impact', fontsize=14)

# Adding legend
ax.legend(["Economic Impact in Year 1", "Economic Impact in Year 2"])

# Annotating data
for i, v in enumerate(df["Economic Impact in Year 1"]):
    ax.text(i+1, v + 5, str(v), color='blue', fontweight='bold')

for i, v in enumerate(df["Economic Impact in Year 2"]):
    ax.text(i+2, v + 5, str(v), color='green', fontweight='bold')

# Adding grid
ax.grid(True)

# Change the background color of the chart figure
ax.set_facecolor("lightgray")

# Set the clip box for the boxes that correspond to the center point of the bounding box
bbox = plt.Bbox([[80, 80], [80 + 472, 80 + 372]])
for patch in bp['boxes']:
    patch.set_clip_box(bbox)

# Update the stroke of the boxes containing the center point of the bounding box
for patch in bp['boxes']:
    patch.set_edgecolor('#436d8e')
    patch.set_linewidth(4.405)

plt.tight_layout()
plt.savefig("myplot.png")