from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

travel_types = ["Car Travel", "Train Travel", "Flight Travel", "Bus Travel"]
popularity = np.array([70, 90, 50, 30])

fig, ax = plt.subplots()
im = ax.imshow(popularity.reshape((-1, 1)), cmap='viridis', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(travel_types)), labels=travel_types)
ax.set_yticks([])

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(travel_types)):
    text = ax.text(0, i, popularity[i],
                   ha="center", va="center", color="w")

ax.set_title("Popularity of Different Types of Travel")
ax.set_xlabel("Type of Travel")
ax.set_ylabel("Popularity")

# Set grid and background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Change the border color of the cells that contain the center point of the bounding box to #4e7fc2 and update the border width to 1.0
for i in range(len(travel_types)):
    for j in range(len(popularity)):
        if i == 1 and j == 0:
            im.set_edgecolor('#4e7fc2')
            im.set_edgewidth(1.0)

fig.tight_layout()
plt.savefig("myplot.png")