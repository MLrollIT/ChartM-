from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given data as a csv string
data = '''"Vacation Type","2018","2019","2020"
"Cruise Vacations",5000,6000,2500
"Road Trips",6300,4500,9000
"Staycations",4000,4200,8400'''

# Read the csv data
df = pd.read_csv(StringIO(data), quotechar='"')

# Prepare the data for plotting
x = df.columns[1:].astype(int)
y_values = df.values[:, 1:].astype(int)
labels = df.values[:, 0]

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot each line
for y, label in zip(y_values, labels):
    ax.plot(x, y, marker='o', label=label)
    for i, v in enumerate(y):
        ax.text(x[i], v+100, str(v), ha='center')  # Annotate data values

# Set title and labels
ax.set_title('Vacation Trends over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Number of People')

# Add legend, grid and set facecolor
ax.legend()
ax.grid(True)
ax.set_facecolor('lightgray')

# Change the shape of the points in the line that contain the center point of the bounding box to a triangle
bbox = ax.bbox_to_anchor((0.5, 0.5), which='center')
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.get_points()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
ax.plot(x, y, marker='^', label=label, bbox=dict(boxstyle="square", facecolor='none', edgecolor='black'), markersize=10, markeredgewidth=2, markeredgecolor='black', markerfacecolor='none', bbox_to_anchor=bbox)

plt.tight_layout()
plt.savefig('myplot.png')