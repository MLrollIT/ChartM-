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

# Change the line color of the box body that contain the center point of the bounding box to #ee04cf, and also set the box whiskers to be invisible by adjusting their visibility to False.
for box in bp['boxes']:
    # change outline color
    box.set(linewidth=2, color='#ee04cf')
    # change facecolor
    box.set(facecolor='none')
    # change whisker properties
    for whisker in bp['whiskers']:
        whisker.set(linewidth=2, color='#ee04cf')
    # change cap properties
    for cap in bp['caps']:
        cap.set(linewidth=2, color='#ee04cf')
    # change median properties
    for median in bp['medians']:
        median.set(linewidth=2, color='#ee04cf')
    # change box properties
    for box in bp['boxes']:
        box.set(linewidth=2, color='#ee04cf')

plt.tight_layout()
plt.savefig("myplot.png")