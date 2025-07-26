from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Stock Indices and corresponding data
indices = ["Dow Jones", "S&P 500", "Nasdaq", "FTSE 100"]
weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]

data = np.array([[25000, 24000, 23500, 26000],
                 [3000, 3200, 3100, 2700],
                 [7500, 7400, 7800, 7300],
                 [7000, 7100, 7200, 6800]])

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='cool', alpha=0.7)  # Changed color map to 'cool'

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(weeks)))
ax.set_xticklabels(weeks)
ax.set_yticks(np.arange(len(indices)))
ax.set_yticklabels(indices)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(indices)):
    for j in range(len(weeks)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Stock Indices Over Four Weeks")
ax.figure.set_facecolor('grey')
ax.grid(color='black', linestyle='-', linewidth=0.2)  # Changed grid color to 'black'

# Change the border color of the cells that contain the center point of the bounding box to #6832f7 and set the border thickness to 2.3 pixels, overriding the previous settings of #b5e713 for the color and 1.9 pixels for the thickness.
for i in range(len(indices)):
    for j in range(len(weeks)):
        if i == 2 and j == 2:
            im.set_edgecolor('#6832f7')
            im.set_edgewidth(2.3)

fig.tight_layout()
plt.savefig("modified_myplot.png")