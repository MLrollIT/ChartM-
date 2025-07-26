from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

cities = ["San Francisco", "Boston", "New York", "Austin", "Seattle"]
years = ["2018", "2019", "2020"]

data = np.array([[500, 450, 300],
                 [200, 400, 600],
                 [300, 250, 500],
                 [400, 350, 200],
                 [250, 300, 250]])

fig, ax = plt.subplots()

# Set facecolor to a soft blue color
ax.set_facecolor("#DCE3F3")  # Soft blue background

heatmap = ax.imshow(data, cmap="YlGn", alpha=0.8)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(cities)))

ax.set_xticklabels(years)
ax.set_yticklabels(cities)

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations
for i in range(len(cities)):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

# Set title and labels
ax.set_title("City Population Over Years")
ax.set_xlabel("Years")
ax.set_ylabel("Cities")

# Add grid
ax.grid(True)

# Add legend
cbar = plt.colorbar(heatmap)
cbar.set_label('Population')

# Modify the font size of the annotations in the cells that contain the center point of the bounding box to 9, and set the background color of those cells to #e17ea8.
for i in range(len(cities)):
    for j in range(len(years)):
        if i == 1 and j == 1:
            text = ax.text(j, i, data[i, j], ha="center", va="center", color="w", fontsize=9, backgroundcolor="#e17ea8")
        else:
            text = ax.text(j, i, data[i, j], ha="center", va="center", color="w", fontsize=9)

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")