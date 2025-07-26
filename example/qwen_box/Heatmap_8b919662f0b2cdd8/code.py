from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

regions = ["North America", "South America", "Europe", "Asia", "Africa"]
years = ["Year2017", "Year2018", "Year2019"]

data = np.array([[4000, 5000, 4500],
                 [4000, 7000, 5000],
                 [5000, 5500, 7000],
                 [4000, 4500, 5000],
                 [2000, 3000, 4000]])

fig, ax = plt.subplots()

# Setting the background color of the chart figure
ax.set_facecolor('gray')

im = ax.imshow(data, cmap='viridis', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(regions)))

# Set the labels to the names
ax.set_xticklabels(years)
ax.set_yticklabels(regions)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(regions)):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

ax.set_title("Region's Yearly Income")
ax.set_xlabel('Year')
ax.set_ylabel('Region')

# Add grid
ax.grid(True)

# Change the edge color of the cells that contain the center point of the bounding box to #9a9943
bbox = dict(boxstyle="square", fc="#9a9943")
for i in range(len(regions)):
    for j in range(len(years)):
        if data[i, j] == 7000:
            ax.text(j, i, data[i, j], ha="center", va="center", color="w", bbox=bbox)

fig.tight_layout()
plt.savefig("myplot.png")