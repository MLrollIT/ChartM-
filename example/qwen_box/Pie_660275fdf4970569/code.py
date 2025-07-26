from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Given csv data
data = [
    ["Wind Energy", "35%"],
    ["Solar Energy", "45%"],
    ["Hydropower", "20%"]
]

# Converting percentage strings to float numbers
data = [[source, float(percent.strip('%'))] for source, percent in data]

# Splitting data into labels and sizes
labels = [source for source, _ in data]
sizes = [percent for _, percent in data]

# Creating a new figure
fig, ax = plt.subplots()

# Creating the pie chart without shadow
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size': 'smaller'}, pctdistance=1.1, colors=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Adding a title
plt.title("Distribution of Renewable Energy Sources")

# Adding a legend
plt.legend(labels, title="Energy Sources", loc="upper right")

# Setting the background color of the chart figure to white
fig.set_facecolor('white')

# Adjusting layout
plt.tight_layout()

# Saving the figure
plt.savefig("myplot.png")

# Animating the slices that contain the center point of the bounding box
for slice in ax.patches:
    if slice.get_bbox().contains((0.5, 0.5)):
        slice.set_animated(True)
        slice.set_clip_on(True)