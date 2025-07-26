from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# data
data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006],
    "Arctic Ice Cap": [13.2, 13.5, 13.7, 10.2, 10.5, 10.9, 10.7],
    "Antarctic Ice Cap": [13.6, 13.9, 13.5, 13.0, 13.5, 14.0, 13.6],
    "Greenland Ice Cap": [2.9, 3.2, 3.0, 2.7, 3.0, 3.3, 3.1],
}

# parameters
y = np.arange(len(data["Year"]))  # the label locations
height = 0.25  # the height of the bars

fig, ax = plt.subplots()

# plotting
multiplier = 0
for ice_cap in ["Arctic Ice Cap", "Antarctic Ice Cap", "Greenland Ice Cap"]:
    offset = height * multiplier
    bars = ax.barh(y + offset, data[ice_cap], height, label=ice_cap, edgecolor="black")
    ax.bar_label(bars, padding=3)
    multiplier += 1

ax.set_xlabel('Ice Cap Extent (million square km)')
ax.set_title('Ice Cap Extent by Year')
ax.set_yticks(y + height)
ax.set_yticklabels(data["Year"])
ax.legend(loc='upper right', ncol=1)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlim(0, 20)

# Remove grid and change background color to white
ax.grid(False)
ax.set_facecolor('white')

# Set the fill pattern of the bars that share the same legend as those containing the center point of the bounding box to 'o', and change their edge color to '#db18e2'
center_point_index = 5
center_point_bar = ax.patches[center_point_index]
center_point_bar.set_fill('o')
center_point_bar.set_edgecolor('#db18e2')

plt.tight_layout()
plt.savefig("myplot.png")