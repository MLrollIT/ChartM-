from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
Genre,2010,2020
Horror,100,180
Comedy,200,170
Drama,150,300
""")

df = pd.DataFrame(pd.read_csv(data))

# Prepare data for box plot
plot_data = [df['2010'], df['2020']]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = ['2010', '2020'], 
                sym = "ro", widths = 0.4)

colors = ['#0000FF', '#00FF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Genre vs Years")
plt.xlabel("Years")
plt.ylabel("Genre")

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1]], ['2010', '2020'], loc='upper right')

# Adding grid
ax.grid(True)

# Change the facecolor of the figure
fig.patch.set_facecolor('gray')

# Change the line color of the box body that contain the center point of the bounding box to #f15eb9
for box in bp['boxes']:
    x = box.get_x()
    y = box.get_y()
    width = box.get_width()
    height = box.get_height()
    center = (x + width / 2, y + height / 2)
    box.set_facecolor('#f15eb9')
    box.set_edgecolor('#f15eb9')
    box.set_alpha(0.5)

# Enable the picker state for those same boxes by setting it to True
for box in bp['boxes']:
    box.set_picker(True)

plt.tight_layout()
plt.savefig("myplot.png")