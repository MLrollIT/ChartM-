from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a pandas DataFrame from the given csv data.
data = pd.DataFrame({
    "Meat Type": ["Beef", "Poultry", "Pork", "Fish", "Lamb"],
    "2000": [50, 30, 70, 40, 10],
    "2005": [55, 35, 75, 50, 12],
    "2010": [52, 37, 80, 60, 14],
    "2015": [54, 40, 78, 45, 16],
    "2020": [60, 80, 79, 48, 30]
})

# Transpose the DataFrame and convert meat types to columns
data.set_index('Meat Type', inplace=True)
data = data.T

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot
bp = ax.boxplot(data, patch_artist = True,
                notch = True, vert = 0,
                sym='r+', widths=0.7)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Annotate data value on the chart figure
for i, line in enumerate(bp['medians']):
    x, y = line.get_xydata()[1]
    ax.annotate(f'{y}', (x, y))

# Set labels
ax.set_xlabel('Meat Types')
ax.set_ylabel('Amount')

# Set title
ax.set_title('Meat Consumption Over Years')

# Add grids on the background
ax.grid(True)

# Change the background the chart figure
ax.set_facecolor('#f0f0f0')

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], data.columns, loc='upper right')

# Add dashed outline to the boxes bodies that contain the center point of the bounding box
for box in bp['boxes']:
    x, y = box.get_xydata()[1]
    ax.plot([x, x], [y, y], color='#02b08b', linestyle='--', linewidth=1.62)

# Set transparency (alpha) of the boxes to 0.7958
for box in bp['boxes']:
    box.set_alpha(0.7958)

# Fill the boxes with a horizontal hatch pattern
for box in bp['boxes']:
    box.set_hatch('/')

plt.tight_layout()
plt.savefig('myplot.png')