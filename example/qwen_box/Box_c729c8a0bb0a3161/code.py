from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {"Species": ["Amazon Rainforest", "Siberian Taiga", "Australian Bush"],
        "Year 2000": [5000, 4200, 3200],
        "Year 2020": [3700, 4000, 1800]}
df = pd.DataFrame(data)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 7))

# Change the boxplot parameters
bp = ax.boxplot([df['Year 2000'], df['Year 2020']], patch_artist=True, vert=0, widths=0.5, sym='r+')

colors = ['#0000FF', '#00FF00']

# Change the color of each boxplot
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Annotate the data
for i in range(len(df['Year 2000'])):
    ax.text(df['Year 2000'][i], i+1, str(df['Year 2000'][i]), ha='center')
    ax.text(df['Year 2020'][i], i+1.4, str(df['Year 2020'][i]), ha='center')

# Add title and labels
ax.set_title('Comparison of Forest Area in Year 2000 and 2020')
ax.set_xlabel('Year')
ax.set_ylabel('Forest Area (thousand square kilometers)')

# Add legend
ax.legend(['Year 2000', 'Year 2020'], loc='upper right')

# Add grid and change background color
ax.grid(True)
# Modified background color to light blue
ax.set_facecolor('#add8e6')

# Change the fill color of the box that contain the center point of the bounding box to #6ac12b
for patch in bp['boxes']:
    patch.set_facecolor('#6ac12b')

# Add an outline to this box body with a linewidth of 1.81 and a color of '#ff8379'
for patch in bp['boxes']:
    patch.set_edgecolor('#ff8379')
    patch.set_linewidth(1.81)

plt.tight_layout()
plt.savefig("myplot.png")