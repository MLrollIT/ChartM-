from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
birds = ["Sparrow", "Hummingbird", "Eagle"]
bird_counts = np.array([[2000, 2100, 2150, 7000, 2200, 2250, 2300, 2350, 2400],
                        [1000, 3500, 3700, 4000, 4100, 8000, 4200, 4300, 4400],
                        [500, 450, 400, 350, 300, 250, 200, 150, 100]])

fig, ax = plt.subplots()
im = ax.imshow(bird_counts, cmap='viridis', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(birds)))

# Assign labels to ticks
ax.set_xticklabels(years)
ax.set_yticklabels(birds)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(birds)):
    for j in range(len(years)):
        text = ax.text(j, i, bird_counts[i, j], ha="center", va="center", color="w")

# Set title and labels
ax.set_title("Bird Population Over The Years")
ax.set_xlabel("Year")
ax.set_ylabel("Bird Species")

# Add grid and change background color
ax.grid(True)
ax.set_facecolor('gray')

# Change the edge color of the cells that contain the center point of the bounding box to #756fdb
for i in range(len(birds)):
    for j in range(len(years)):
        if i == 1 and j == 3:
            im.set_edgecolor('#756fdb')
        elif i == 1 and j == 4:
            im.set_edgecolor('#756fdb')
        elif i == 1 and j == 5:
            im.set_edgecolor('#756fdb')
        elif i == 1 and j == 6:
            im.set_edgecolor('#756fdb')
        elif i == 1 and j == 7:
            im.set_edgecolor('#756fdb')
        elif i == 1 and j == 8:
            im.set_edgecolor('#756fdb')
        elif i == 1 and j == 9:
            im.set_edgecolor('#756fdb')

fig.tight_layout()
plt.savefig("myplot.png")