from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# The given data
meat_type = ["Beef", "Poultry", "Pork", "Fish", "Lamb"]
meat_data = {
    '2000': [50, 30, 70, 40, 10],
    '2005': [55, 35, 75, 50, 12],
    '2010': [52, 37, 80, 60, 14],
    '2015': [54, 40, 78, 45, 16],
    '2020': [60, 80, 79, 48, 30]
}

y = np.arange(len(meat_type))  # the label locations
height = 0.15  # the height of the bars
multiplier = 0

fig, ax = plt.subplots()

for year, consumption in meat_data.items():
    offset = height * multiplier
    bars = ax.barh(y + offset, consumption, height, label=year, edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Consumption (in tons)')
ax.set_title('Meat consumption by type in different years')
ax.set_yticks(y + height * 2)
ax.set_yticklabels(meat_type)
ax.legend(loc='upper right', ncol=1)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlim(0, 100)

# Add grid and change background color
ax.grid(True)
# Set the facecolor to light blue
ax.set_facecolor('#add8e6')  # light blue

# Adjust the transparency of the bars that share the same legend as those containing the center point of the bounding box to 0.521
center_point = 70
for year, consumption in meat_data.items():
    if year == '2015':
        for i in range(len(consumption)):
            if consumption[i] == center_point:
                bars = ax.barh(y + height * 2 + i * height, consumption, height, label=year, edgecolor='black')
                bars.set_alpha(0.521)
                bars.set_facecolor('#089CEB')
                bars.set_edgecolor('#089CEB')
                bars.set_hatch('/')
                bars.set_linewidth(0.15)

plt.tight_layout()

# Save the final figure as "myplot.png"
plt.savefig("myplot.png")