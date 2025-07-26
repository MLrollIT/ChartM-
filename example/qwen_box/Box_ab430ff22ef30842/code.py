from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {"Year": ["2014", "2015", "2016", "2017", "2018", "2019", "2020"],
        "Number of Visits": [5000, 4600, 4700, 4400, 7000, 6900, 4500],
        "Number of Books Borrowed": [7000, 6000, 9000, 6500, 8000, 12000, 7000]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a figure and axis
fig, ax = plt.subplots(figsize =(10, 7))

# Create box plot
bp = ax.boxplot([df["Number of Visits"], df["Number of Books Borrowed"]], patch_artist=True, vert=0, widths=0.5, sym='',
                labels = ['Number of Visits', 'Number of Books Borrowed'])

# Change color for each box
colors = ['#0000FF', '#00FF00']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Library Visits and Books Borrowed Over the Years')
ax.set_xlabel('Counts')
ax.set_ylabel('Categories')

# Show grid
ax.grid(True)

# Change the figure background color
fig.set_facecolor('gray')

# Annotate data value on the chart figure
for i, line in enumerate(bp['medians']):
    x, y = line.get_xydata()[1]
    ax.annotate(f'Median: {x}', (x, y), textcoords="offset points", xytext=(10,0), ha='center', fontsize=8)

# Add a shadow effect to the box body that contains the center point of the bounding box
for box in bp['boxes']:
    x, y = box.get_xydata()[1]
    box.set_facecolor('#53aa08')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#53aa08')
    box.set_zorder(3)
    box.set_boxstyle('square', pad=0.3, rounding_size=3, fc='white', ec='black', lw=2)
    box.set_edgecolor('black')
    box.set_edgecolor('#5