from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# data
regions = ["North America", "Latin America", "Europe", "Africa", "Asia", "Australia", "Antarctica", "East Asia", "Middle East"]
home_schooling_rate = np.array([[5, 8, 10, 3, 7, 11, 1, 6, 4]])

fig, ax = plt.subplots()

# using heatmap
im = ax.imshow(home_schooling_rate, cmap='YlOrRd', alpha=0.7)

# setting ticks
ax.set_xticks(np.arange(len(regions)))
ax.set_yticks(np.arange(1))
ax.set_xticklabels(regions, fontsize=12)  # Changed font size for x-axis tick labels
ax.set_yticklabels(['Home schooling rate'], fontsize=12)  # Changed font size for y-axis tick labels

# rotating the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# loop over data dimensions and create text annotations
for i in range(len(home_schooling_rate[0])):
    text = ax.text(i, 0, home_schooling_rate[0][i], ha="center", va="center", color="black")

# setting title and labels
ax.set_title("Home schooling rate by region", fontsize=16)  # Changed font size for title
ax.set_xlabel("Region")
ax.set_ylabel("Home schooling rate")

# adding grid and changing the background color
ax.grid(True)
ax.set_facecolor("lightgray")

# legend
cbar = plt.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Home schooling rate', rotation=-90, va="bottom")

# Increase the border thickness of the cells that contain the center point of the bounding box to 2.7 pixels and change their color to #332e9c. Also, set the annotation text color in those cells to #c09ae7.
for i in range(len(home_schooling_rate[0])):
    for j in range(len(home_schooling_rate[0])):
        if i == 0 and j == 0:
            text = ax.text(i, j, home_schooling_rate[0][0], ha="center", va="center", color="#332e9c", fontsize=12)
            text.set_bbox(dict(boxstyle="square", ec=(1, 1, 1), fc=(1, 1, 1), pad=0.1, lw=2.7))
        elif i == 0 and j == 1:
            text = ax.text(i, j, home_schooling_rate[0][1], ha="center", va="center", color="#332e9c", fontsize=12)
            text.set_bbox(dict(boxstyle="square", ec=(1, 1, 1), fc=(1, 1, 1), pad=0.1, lw=2.7))
        elif i == 0 and j == 2:
            text = ax.text(i, j, home_schooling_rate[0][2], ha="center", va="center", color="#332e9c", fontsize=12)
            text.set_bbox(dict(boxstyle="square", ec=(1, 1, 1), fc=(1, 1, 1), pad=0.1, lw=2.7))
        elif i == 0 and j == 3:
            text = ax.text(i, j, home_schooling_rate[0][3], ha="center", va="center", color="#332e9c", fontsize=12)
            text.set_bbox(dict(boxstyle="square", ec=(1, 1, 1), fc=(1, 1, 1), pad=0.1, lw=2.7))
        elif i == 0 and j == 4:
            text = ax.text(i, j, home_schooling_rate[0][4], ha="center", va="center", color="#332e9c", fontsize=12)
            text.set_bbox(dict(boxstyle="square", ec=(1, 1, 1), fc=(1, 1, 1), pad=0.1, lw=2.7))
        elif i == 0 and j == 5:
            text = ax.text(i, j, home_schooling_rate[0][5], ha="center", va="center", color="#332e9c", fontsize=12)
            text.set_bbox(dict(boxstyle="square", ec=(1, 1, 1), fc=(1, 1, 1), pad=0.1,