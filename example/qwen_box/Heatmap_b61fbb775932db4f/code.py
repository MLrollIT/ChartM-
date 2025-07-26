from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# data
regions = ["North America", "Latin America", "Europe", "Africa","Asia", "Australia", "Antarctica", "East Asia", "Middle East"]
home_schooling_rate = np.array([[5, 8, 10, 3, 7, 11, 1, 6, 4]])

fig, ax = plt.subplots()

# using heatmap
im = ax.imshow(home_schooling_rate, cmap='YlOrRd', alpha=0.7)

# setting ticks
ax.set_xticks(np.arange(len(regions)))
ax.set_yticks(np.arange(1))
ax.set_xticklabels(regions)
ax.set_yticklabels(['Home schooling rate'])

# rotating the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# loop over data dimensions and create text annotations
for i in range(len(home_schooling_rate[0])):
    text = ax.text(i, 0, home_schooling_rate[0][i], ha="center", va="center", color="black")

# setting title and labels
ax.set_title("Home schooling rate by region")
ax.set_xlabel("Region")
ax.set_ylabel("Home schooling rate")

# adding grid and changing the background color
ax.grid(True)
ax.set_facecolor("lightgray")

# legend
cbar = plt.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Home schooling rate', rotation=-90, va="bottom")

fig.tight_layout()
plt.savefig("myplot.png")