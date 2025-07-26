from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# data
years = ["2016", "2017", "2018", "2019", "2020", "2021"]
categories = ["Qubits", "Quantum Supremacy", "Quantum Volume", "Quantum Computers Sold"]
data = np.array([[2, 0, 4, 0],
                 [6, 0, 16, 1],
                 [20, 0, 80, 3],
                 [53, 1, 2128, 5],
                 [72, 1, 373248, 7],
                 [100, 1, 1000000, 10]])

# create figure and axes
fig, ax = plt.subplots()

# set light gray background color
ax.set_facecolor("lightgray")

# plot heatmap
im = ax.imshow(data, cmap='viridis', alpha=0.7)

# set ticks and labels
ax.set_xticks(np.arange(len(categories)), labels=categories)
ax.set_yticks(np.arange(len(years)), labels=years)

# rotate x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# add text annotations
for i in range(len(years)):
    for j in range(len(categories)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

# set title
ax.set_title("Quantum Computing Development (2016-2021)")

# add grid
ax.grid(True)

# modify the bounding box
bbox = ax.bbox
bbox = bbox.copy()
bbox.width = 1.5
bbox.color = "#017b1c"
bbox.textcolor = "#cd3955"

# save figure
fig.tight_layout()
plt.savefig("Edit_figure.png")