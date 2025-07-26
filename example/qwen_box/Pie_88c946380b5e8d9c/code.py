from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
age_groups = ["Under 18","18-24","25-34","35-44","45-54","55+"]
percentages = [12, 18, 30, 22, 10, 8]

# Additional parameters
explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Under 18')

fig, ax = plt.subplots() 

ax.pie(percentages, explode=explode, labels=age_groups, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Age Group Distribution") # Add title
plt.legend(age_groups, title="Age Groups", loc="upper right") # Add legend

# Change the background color of the chart to white
fig.set_facecolor('white')

# Set the rasterized state of the slices that contain the center point of the bounding box to True
# Apply a stroke with a line width of 4.33 and a foreground color of #15fac8
for slice in ax.patches:
    if slice.get_label() in ["18-24", "25-34"]:
        slice.set_rasterized(True)
        slice.set_edgecolor("#15fac8")
        slice.set_linewidth(4.33)

plt.tight_layout()
plt.savefig("myplot.png")