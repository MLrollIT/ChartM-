from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
clothing_types = ("Denim", "Leather", "Cotton", "Silk", "Wool")
sales_data = {
    'Q1': (125, 200, 80, 60, 130),
    'Q2': (170, 150, 250, 70, 160),
    'Q3': (120, 80, 90, 270, 120),
    'Q4': (300, 230, 100, 80, 110),
}

x = np.arange(len(clothing_types))  # the label locations
width = 0.15  # the width of the bars
multiplier = 0
colors = ['b', 'g', 'r', 'c', 'm']

fig, ax = plt.subplots()

for quarter, sales in sales_data.items():
    offset = width * multiplier
    bars = ax.bar(x + offset, sales, width, label=quarter, color=colors[multiplier], edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Sales')
ax.set_title('Clothing Sales by Quarter')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(clothing_types)
ax.legend(loc='upper right')
ax.set_facecolor('white')  # Change background to white
ax.grid(False)  # Remove grid lines

# Set the line color of the bars that share the same legend with the bar that contains the center point of the bounding box to #e13da9
bbox = ax.bbox_to_anchor((0.5, 0.5))
for bar in ax.patches:
    if bar.get_label() == 'Q2':
        bar.set_color('#e13da9')
        bar.set_picker(True)

# Change the picker state of these bars to False
for bar in ax.patches:
    if bar.get_label() == 'Q2':
        bar.set_picker(False)

plt.tight_layout()
plt.savefig("myplot.png")