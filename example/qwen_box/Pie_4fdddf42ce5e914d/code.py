from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
labels = ['Satellite Launches', 'Space Probes', 'Telescope Technology', 'International Space Station', 
          'Manned Space Missions', 'Space Research & Development']
sizes = [25, 20, 15, 20, 15, 5]

fig, ax = plt.subplots()

ax.pie(sizes, labels=labels, autopct='%.0f%%', explode=(0, 0, 0, 0.1, 0, 0), 
       shadow=True, startangle=90, colors=('blue', 'orange', 'green', 'red', 'purple', 'brown'))

plt.title("Distribution of Space Technology/Exploration") 
plt.legend(labels, title="Space Technology/Exploration", loc="upper right")

fig.patch.set_facecolor('lightgray')

# Set the linestyle of the slices containing the center point of the bounding box to 'dashdot'
# and add a stroke with a linewidth of 2.36 and a foreground color of #f18178
for slice in ax.patches:
    if slice.get_label() == 'International Space Station':
        slice.set_linestyle('dashdot')
        slice.set_edgecolor('#f18178')
        slice.set_linewidth(2.36)

plt.tight_layout()
plt.savefig("myplot.png")