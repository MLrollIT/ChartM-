from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# The given data
groups = ["Young Adults", "Middle Aged", "Seniors", "Teens"]
recycling_habits = np.array([[10, 12, 14, 20, 22, 25, 6, 30, 32, 35, 18, 20],
                             [12, 13, 11, 9, 8, 7, 20, 10, 7, 6, 5, 50],
                             [20, 18, 15, 13, 10, 9, 12, 30, 35, 32, 28, 25],
                             [10, 15, 20, 25, 30, 12, 14, 50, 45, 40, 35, 30]])

fig, ax = plt.subplots()

# Using the imshow() function to draw the heatmap
im = ax.imshow(recycling_habits, cmap='viridis', alpha=0.7)

# Setting the ticks and labels
ax.set_xticks(np.arange(12))
ax.set_yticks(np.arange(len(groups)), labels=groups)

# Adding a grid and changing the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Rotating the tick labels and setting their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Looping over data dimensions and creating text annotations
for i in range(len(groups)):
    for j in range(12):
        text = ax.text(j, i, recycling_habits[i, j], ha="center", va="center", color="w")

# Setting the title and labels
ax.set_title("Recycling Habits by Demographics")
ax.set_xlabel("Months")
ax.set_ylabel("Demographics")

# Applying a tight layout and saving the figure
fig.tight_layout()
plt.savefig("myplot.png")

# Modify the code to change the border color of the cells that contain the center point of the bounding box in the heatmap to #0693f1, with a border width of 0.8. Also, update the color of the annotation text in those cells to #848e60.
# First, find the center point of the bounding box
bbox = ax.bbox
center_x = bbox.x + bbox.width / 2
center_y = bbox.y + bbox.height / 2

# Then, find the cell that contains the center point of the bounding box
cell = np.unravel_index(np.argmin(np.abs(recycling_habits - center_x)), recycling_habits.shape)

# Finally, modify the border color and annotation text color of the cell
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0
recycling_habits[cell] = 0

# Draw the heatmap again
im = ax.imshow(recycling_habits, cmap='viridis', alpha=0.7)

# Modify the border color and annotation text color of the cell
ax.text(cell[1], cell[0], recycling_habits[cell], ha="center", va="center", color="#848e60")

# Save the modified figure
plt.savefig("Edit_figure.png")