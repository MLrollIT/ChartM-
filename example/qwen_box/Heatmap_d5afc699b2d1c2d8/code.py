from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Given data
disorders = ["Depression", "Anxiety", "Bipolar Disorder"]
years = ["2018", "2019", "2020"]

data = np.array([[100, 150, 130],
                 [80, 90, 200],
                 [60, 70, 65]])

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='hot', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)), labels=years)
ax.set_yticks(np.arange(len(disorders)), labels=disorders)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(disorders)):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="w")

# Set title, labels and legend
ax.set_title("Prevalence of Mental Health Disorders (in thousands)")
ax.set_xlabel("Year")
ax.set_ylabel("Disorder")
ax.legend()

# Set background color and grid
ax.set_facecolor("lightgray")
ax.grid(True)

# Change the border color of the cells that contain the center point of the bounding box to #457a1c, with a border width of 1.3. Additionally, update the background color of these cells to #b88f24.
for i in range(len(disorders)):
    for j in range(len(years)):
        if i == 1 and j == 1:
            im.set_edgecolor('#457a1c')
            im.set_linewidth(1.3)
            im.set_facecolor('#b88f24')

fig.tight_layout()
plt.savefig("myplot.png")