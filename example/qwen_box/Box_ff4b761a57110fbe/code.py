from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Input data
data = {
    'Profession': ['Teacher', 'Doctor', 'Software Developer', 'Construction Worker', 'Nurse', 'Chef', 'Lawyer', 'Police Officer', 'Retail Worker'],
    'Hours in Week 1': [40, 50, 45, 60, 48, 50, 55, 60, 35],
    'Hours in Week 2': [44, 75, 47, 42, 50, 50, 30, 60, 35]
}

df = pd.DataFrame(data)

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot([df['Hours in Week 1'], df['Hours in Week 2']], patch_artist=True,
                notch=True, vert=0, widths=0.5, labels=['Week 1', 'Week 2'])

colors = ['#0000FF', '#00FF00']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Adding grid
ax.grid(True)
ax.set_facecolor('gray')

# Adding title and labels
plt.title('Hours worked per week')
plt.xlabel('Week')
plt.ylabel('Hours')

# Set the median line's linestyle of the section that contains the center point of the bounding box to 'dotted' and change its transform to the figure's coordinate system
for median in bp['medians']:
    median.set_linestyle('dotted')
    median.set_transform(ax.transAxes)

# Saving the figure
plt.tight_layout()
plt.savefig("myplot.png")