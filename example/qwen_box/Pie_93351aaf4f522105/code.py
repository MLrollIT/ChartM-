from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# The given data
regions = ["North America", "South America", "Europe", "Africa", "Asia", "Australia", "Antarctica"]
percentages = [15, 10, 20, 25, 25, 3, 2]

# The given code example
fig, ax = plt.subplots()

# Additional parameters for ax.pie
explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'North America')
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink', 'red']

ax.pie(percentages, explode=explode, labels=regions, colors=colors, autopct='%.1f%%', 
       shadow=True, startangle=140, labeldistance=1.15, pctdistance=0.85)

plt.title("Regional Population Distribution")  # Add title
plt.legend(regions, title="Regions", loc="upper right")  # Add legend

fig.set_facecolor('white')  # Change the face color of the figure to white
plt.tight_layout()  # Adjust the padding between and around the subplots.
plt.savefig("myplot.png")  # Save the final figure

# Modify the code to change the rasterized state of the slices that contain the center point of the bounding box to True
for i, p in enumerate(ax.patches):
    if p.get_bbox().contains((0.5, 0.5)):
        p.set_rasterized(True)