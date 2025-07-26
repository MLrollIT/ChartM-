from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# Given data
data = """City, Crime Rate 1, Crime Rate 2, Crime Rate 3, Crime Rate 4, Crime Rate 5
New York, 20, 22, 24, 50, 25
Los Angeles, 18, 17, 16, 35, 15
Chicago, 28, 27, 25, 25, 27
Houston, 15, 20, 35, 20, 15
Phoenix, 10, 15, 10, 15, 5"""
df = pd.read_csv(StringIO(data))

# Prepare data for box plot
plot_data = [df[col] for col in df.columns if col != "City"]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 1, 
                labels = df.columns[1:], 
                sym = "go", widths = 0.4)

colors = ['#0000FF', '#00FF00', '#FF00FF', '#FFFF00', '#00FFFF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("City vs Crime Rate")
plt.xlabel("City")
plt.ylabel("Crime Rate")

# Adding legend
plt.legend([bp["boxes"][i] for i in range(len(df.columns[1:]))], df.columns[1:], loc='upper right')

# Adding grid
plt.grid(True)

# Change the facecolor of the figure
fig.patch.set_facecolor('gray')

# Adjust the clipping box of the boxes that contain the center point of the bounding box
bbox = plt.Bbox([[156, 140], [156 + 195, 140 + 185]])
for box in bp['boxes']:
    box.set_clip_box(bbox)

# Update the color of the boxes related to the Target_object to #303fa2
for i in range(len(df.columns[1:])):
    box = bp['boxes'][i]
    box.set_facecolor('#303fa2')

plt.tight_layout()
plt.savefig("myplot.png")