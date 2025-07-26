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

im = ax.imshow(waste, cmap='hot', alpha=0.7)

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

ax.grid(True)
ax.set_facecolor('lightgray')

fig.tight_layout()
plt.savefig("myplot.png")

# Change the background color of the cells that contain the center point of the bounding box to #a18901
# and update the annotation text color in those cells to #9537db
for i in range(len(households)):
    for j in range(len(years)):
        if i == 3 and j == 1:
            im.set_array(waste[i, j])
            im.set_clim(0, 1000)
            im.set_cmap('hot')
            im.set_facecolor('#a18901')
            im.set_edgecolor('#9537db')
            im.set_text(waste[i, j])
            im.set_text_color('#9537db')