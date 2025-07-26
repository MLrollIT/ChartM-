from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

countries = ["USA", "China", "India", "Brazil", "Australia"]
years = ["Year 1", "Year 2", "Year 3"]

data = np.array([[100, 200, 170],
                 [150, 160, 320],
                 [120, 140, 120],
                 [200, 210, 160],
                 [80, 70, 150]])

fig, ax = plt.subplots()
im = ax.imshow(data, alpha=0.7, cmap='viridis')

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(countries)))
ax.set_yticklabels(countries)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(countries)):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

# Increase border thickness and change color of cells containing center point of bounding box
for i in range(len(countries)):
    for j in range(len(years)):
        if data[i, j] == 150:
            ax.text(j, i, data[i, j], ha="center", va="center", color="w", fontsize=10, fontweight='bold', bbox=dict(boxstyle="square", facecolor="#071003", edgecolor="#071003", lw=2.8))

ax.set_title("Data of Countries Over Years")
ax.set_xlabel("Years")
ax.set_ylabel("Countries")

# Set grid and background color
ax.grid(True)
ax.set_facecolor('lightgray')

fig.tight_layout()
plt.savefig("myplot.png")