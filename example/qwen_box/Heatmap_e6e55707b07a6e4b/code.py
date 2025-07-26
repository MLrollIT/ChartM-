from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np


age_groups = ["20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90", "90-100"]
activities = ["Running", "Yoga", "Weightlifting"]

data = np.array([[140, 180, 200],
                 [160, 220, 210],
                 [180, 210, 190],
                 [210, 205, 205],
                 [200, 180, 215],
                 [180, 160, 210],
                 [220, 140, 190],
                 [180, 120, 160]])

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='viridis', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(activities)), labels=activities)
ax.set_yticks(np.arange(len(age_groups)), labels=age_groups)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(age_groups)):
    for j in range(len(activities)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

ax.set_title("Activity participation by age group")
ax.set_xlabel("Activities")
ax.set_ylabel("Age groups")
ax.grid(True)
ax.set_facecolor('lightgray')
fig.tight_layout()

# Update the edge color of the cells that contain the center point of the bounding box to #569081.
# Increase the border thickness to 2.8 pixels and change the border color to #0225c2.
bbox = ax.bbox
bbox_points = bbox.get_points()
bbox_points[1, 0] = 0.5
bbox_points[1, 1] = 0.5
bbox_points[2, 0] = 0.5
bbox_points[2, 1] = 0.5
bbox.set_points(bbox_points)
bbox.set_edgecolor("#569081")
bbox.set_linewidth(2.8)
bbox.set_edgecolor("#0225c2")

plt.savefig("myplot.png")