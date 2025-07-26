from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

households = ["Single Person Household", "Two-Person Household", "Three-Person Household", 
              "Four-Person Household", "Five-Person Household", "Six or More Person Household", 
              "Average Household"]
years = ["2019", "2020"]

waste = np.array([[450, 550],
                  [1000, 1100],
                  [700, 800],
                  [800, 600],
                  [500, 700],
                  [1100, 1300],
                  [720, 790]])

fig, ax = plt.subplots()

# Change the color map to 'viridis'
im = ax.imshow(waste, cmap='viridis', alpha=0.7)

ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)

ax.set_yticks(np.arange(len(households)))
ax.set_yticklabels(households)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(households)):
    for j in range(len(years)):
        text = ax.text(j, i, waste[i, j], ha="center", va="center", color="w")

ax.set_title("Household Food Waste (in kg/year)")
ax.set_xlabel("Year")
ax.set_ylabel("Household Type")

# Change the color of the grid lines to 'blue'
ax.grid(True, color='blue')
ax.set_facecolor('lightgray')

# Update the border color of the cells that contain the center point of the bounding box to #861939, and set the border width to 0.7
for i in range(len(households)):
    for j in range(len(years)):
        if waste[i, j] == 600:
            ax.text(j, i, waste[i, j], ha="center", va="center", color="w", bbox=dict(boxstyle="square", fc="#861939", ec="#861939", lw=0.7))

fig.tight_layout()
plt.savefig("myplot.png")