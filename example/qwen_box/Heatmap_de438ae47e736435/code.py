from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

technologies = ["Battery Life (in hours)", "Range (in Km)", "Load Capacity (in Kg)", "Flight Speed (in Km/hr)"]
years = ["Year 2014", "Year 2018", "Year 2022"]

data = np.array([[5, 7, 4],
                 [20, 35, 60],
                 [1, 2, 5],
                 [40, 80, 55]])

fig, ax = plt.subplots()
# Change the colormap to 'plasma'
im = ax.imshow(data, cmap='plasma', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(technologies)))
ax.set_yticklabels(technologies)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Annotate each cell with the data value
for i in range(len(technologies)):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="w")

# Remove the annotations from the cells that contain the center point of the bounding box in the heatmap
for i in range(len(technologies)):
    for j in range(len(years)):
        if i == 1 and j == 1:
            ax.text(j, i, data[i, j],
                    ha="center", va="center", color="w", alpha=0.0)

# Change the color of the annotation text for those cells to #3c4098
for i in range(len(technologies)):
    for j in range(len(years)):
        if i == 1 and j == 1:
            ax.text(j, i, data[i, j],
                    ha="center", va="center", color="#3c4098", alpha=0.7)

ax.set_title("Technology Performance Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("Performance Metric")
ax.grid(visible=True)
fig.tight_layout()
plt.savefig("Edit_figure.png")