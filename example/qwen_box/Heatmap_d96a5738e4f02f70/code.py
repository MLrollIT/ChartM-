from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
genres = ["Pop", "Rock", "Classical"]
sales = np.array([
    [100, 80, 120],
    [120, 70, 130],
    [150, 60, 140],
    [200, 50, 100],
    [180, 90, 120],
    [190, 80, 110],
    [210, 70, 90],
    [230, 150, 80],
    [240, 160, 70]
])

fig, ax = plt.subplots()
im = ax.imshow(sales, cmap="viridis")  # Changed colormap to "viridis" and removed alpha

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(genres)))
ax.set_yticks(np.arange(len(years)))
ax.set_xticklabels(genres)
ax.set_yticklabels(years)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(years)):
    for j in range(len(genres)):
        text = ax.text(j, i, sales[i, j],
                       ha="center", va="center", color="w")

# Adding grid, title and labels
ax.grid(True)
ax.set_facecolor('lightgray')
ax.set_title("Music Genre Sales Over the Years")
ax.set_xlabel("Genre")
ax.set_ylabel("Year")

# Change the background color of the cells that contain the center point of the bounding box to #e051f1
bbox = dict(boxstyle="square", fc="#e051f1")
for i in range(len(years)):
    for j in range(len(genres)):
        if i == 4 and j == 1:
            text = ax.text(j, i, sales[i, j],
                           ha="center", va="center", color="w", bbox=bbox)

fig.tight_layout()
plt.savefig("myplot.png")