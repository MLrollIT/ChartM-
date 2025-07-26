from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Data
labels = ["VR Headsets", "VR Software", "VR Games", "VR Application in Medicine", 
          "VR Application in Education", "VR Application in Military Training", 
          "VR Application in Entertainment", "VR Accessories", "VR Research and Development"]

percentages = [25, 20, 15, 10, 10, 5, 10, 3, 2]

# Figure
fig, ax = plt.subplots()

# Pie chart
ax.pie(percentages, labels=labels, autopct='%.0f%%', 
        textprops={'size': 'smaller'}, radius=0.5, 
        explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1), 
        shadow=True, labeldistance=1.2, pctdistance=0.7)

# Title and Legends
plt.title("Distribution of Virtual Reality Elements")
plt.legend(labels, title="Elements", loc="upper right")

# Background color
fig.patch.set_facecolor('lightgray')

# Save figure
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the line width and style of the slices that contain the center point of the bounding box
for slice in ax.patches:
    if slice.get_bbox().contains((0.5, 0.5)):
        slice.set_linewidth(2.83)
        slice.set_dashdotstyle('dashdot')