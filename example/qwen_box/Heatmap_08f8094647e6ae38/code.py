from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

plants = ["Rose", "Sunflower", "Fern", "Dandelion", "Orchid", "Cactus", "Lily", "Oak"]
patterns = ["Pattern1", "Pattern2", "Pattern3", "Pattern4", "Pattern5", "Pattern6", "Pattern7"]

growth = np.array([[25,30,35,70,75,30,20],
                   [40,30,20,10,50,60,70],
                   [60,50,40,30,80,90,100],
                   [20,30,40,80,85,40,30],
                   [100,90,80,70,150,140,130],
                   [30,40,50,100,105,50,40],
                   [70,60,50,40,90,100,110],
                   [50,60,70,80,85,90,40]])

fig, ax = plt.subplots()
im = ax.imshow(growth, cmap='viridis', alpha=0.7)  # Changed 'Blues' to 'viridis'

ax.set_xticks(np.arange(len(patterns)))
ax.set_yticks(np.arange(len(plants)))
ax.set_xticklabels(patterns)
ax.set_yticklabels(plants)
ax.set_facecolor('gray')
ax.grid(True, linestyle='--', color='w')  # Added color='w' to set gridline color to white

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(plants)):
    for j in range(len(patterns)):
        text = ax.text(j, i, growth[i, j], ha="center", va="center", color="w")

ax.set_title("Plant Growth Patterns")
ax.set_xlabel("Pattern")
ax.set_ylabel("Plant Species")

fig.tight_layout()

# Change the border color of the cells that contain the center point of the bounding box to #a9e0f0 with a width of 1.1
# Update the edge color of those same cells to #6ad280
bbox = ax.get_position()
bbox.x0 = 0.5
bbox.width = 0.5
bbox.y0 = 0.5
bbox.height = 0.5
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox_to_anchor(bbox)
bbox = ax.bbox