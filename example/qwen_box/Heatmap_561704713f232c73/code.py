from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Given data 
wildlife = ["Deer", "Bear", "Squirrel", "Bird", "Fox"]
years = ["1970", "2020"]

impact = np.array([[80, 55],
                   [50, 40],
                   [70, 75],
                   [80, 60],
                   [25, 35]])

fig, ax = plt.subplots()
im = ax.imshow(impact, cmap='viridis', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)

ax.set_yticks(np.arange(len(wildlife)))
ax.set_yticklabels(wildlife)

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations
for i in range(len(wildlife)):
    for j in range(len(years)):
        text = ax.text(j, i, impact[i, j], ha="center", va="center", color="w")

# Set the title and labels
ax.set_title("Urbanization Impact on Wildlife")
ax.set_xlabel("Years")
ax.set_ylabel("Wildlife")

# Set the facecolor
ax.set_facecolor('lightgray')

# Add grid
ax.grid(True)

# Adjust the font size of the annotations in the cells that contain the center point of the bounding box to 13
for i in range(len(wildlife)):
    for j in range(len(years)):
        text = ax.text(j, i, impact[i, j], ha="center", va="center", color="w", fontsize=13)

plt.tight_layout()
plt.savefig("myplot.png")