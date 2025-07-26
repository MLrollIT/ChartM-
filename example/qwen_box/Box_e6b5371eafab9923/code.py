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

# New colors for the box plot
colors = ['#800080', '#FFA500']  # Purple for 2010, Orange for 2020

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

# Change the color of the boxes that contain the center point of the bounding box to #3f1ce7
for box in bp['boxes']:
    box.set(facecolor='#3f1ce7', edgecolor='black', linewidth=4.18, linestyle='solid')

# Apply a stroke to these all of the boxes' lines with a linewidth of 4.18 and a foreground color of #c51b6c
for whisker in bp['whiskers']:
    whisker.set(color='#c51b6c', linewidth=4.18)

for cap in bp['caps']:
    cap.set(color='#c51b6c', linewidth=4.18)

for median in bp['medians']:
    median.set(color='#c51b6c', linewidth=4.18)

for flier in bp['fliers']:
    flier.set(marker='o', color='#c51b6c', alpha=0.5)

plt.tight_layout()
plt.savefig("myplot.png")