from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

disaster_types = ["Flood", "Drought", "Earthquake"]
years = ["Year 1", "Year 2"]

economic_impact = np.array([[100, 50],
                            [150, 80],
                            [120, 200]])

fig, ax = plt.subplots()
im = ax.imshow(economic_impact, cmap="YlOrRd", alpha=0.7)

ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(disaster_types)))
ax.set_xticklabels(years)
ax.set_yticklabels(disaster_types)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(disaster_types)):
    for j in range(len(years)):
        text = ax.text(j, i, economic_impact[i, j], ha="center", va="center", color="w")

ax.set_title("Economic Impact of Disasters")
ax.set_xlabel("Year")
ax.set_ylabel("Disaster Type")
ax.grid(True)
ax.set_facecolor('gray')

# Change the border color of the cells that contain the center point of the bounding box in the heatmap to #f11cb9, and set the border width to 1.3.
for i in range(len(disaster_types)):
    for j in range(len(years)):
        if i == 1 and j == 1:
            im.set_edgecolor('#f11cb9')
            im.set_linewidth(1.3)

plt.tight_layout()
plt.savefig("myplot.png")