from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a DataFrame from the given data
data = pd.DataFrame({
    "Mental Health Disorder": ["Depression", "Anxiety", "Bipolar Disorder"],
    "2018": [100, 80, 60],
    "2019": [150, 90, 70],
    "2020": [130, 200, 65]
})

# Set the index to 'Mental Health Disorder'
data.set_index('Mental Health Disorder', inplace=True)

# Create boxplot
fig, ax = plt.subplots(figsize =(10, 7))
bp = ax.boxplot(data.values, patch_artist = True, notch = True, vert = 0, widths=0.6,
                labels=data.index, sym='r+')

# Set colors for each box using a monochromatic palette
colors = ['#1E90FF', '#4169E1', '#0000CD']  # Shades of blue
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Mental Health Disorders over the Years')
ax.set_xlabel('Mental Health Disorder')
ax.set_ylabel('Number of Cases')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2]], ['Depression', 'Anxiety', 'Bipolar Disorder'], loc='upper right')

# Annotate data values on the chart
for line, value in zip(bp['medians'], data.median(axis=1)):
    x, y = line.get_xydata()[1] # Top of the median line
    ax.text(x, y, f'{value}', horizontalalignment='center') # Draw text in the middle

# Set the background color of the chart figure
ax.set_facecolor('lightgray')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")