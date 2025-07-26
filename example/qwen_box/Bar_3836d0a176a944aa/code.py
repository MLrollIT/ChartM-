from io import StringIO

import matplotlib.pyplot as plt
import numpy as np

# Given data
diets = ("Keto", "Paleo", "Vegan")
months = np.array(range(1, 13))  # 12 months in a year
data = np.array([[15, 30, 50, 25, 60, 70, 40, 30, 20, 10, 30, 60],
                 [70, 60, 40, 20, 10, 5, 7, 75, 80, 85, 70, 60],
                 [30, 40, 45, 50, 55, 45, 35, 25, 15, 45, 70, 30]])

fig, ax = plt.subplots()

# Draw the bar chart
for i, diet in enumerate(diets):
    bars = ax.bar(months + i*0.25, data[i], width=0.25, align='center', label=diet, edgecolor='black')
    ax.bar_label(bars)

ax.set_xticks(months + 0.25)
ax.set_xticklabels(months)

ax.set_xlabel('Month')
ax.set_ylabel('Popularity Score')
ax.set_title('Popularity of Diets Over Months')
ax.legend()

ax.grid(True)
ax.set_facecolor('lightgray')

# Set the clipping state of the bars that share the same legend with the bar that contains the center point of the bounding box to True
center_point = 6
target_object = ax.bar(months + 0.25, data[0][center_point], width=0.25, align='center', label='Keto', edgecolor='black')
for i, diet in enumerate(diets):
    bars = ax.bar(months + i*0.25, data[i], width=0.25, align='center', label=diet, edgecolor='black')
    ax.bar_label(bars)
    if i == 0:
        continue
    for bar in bars:
        if bar.get_label() == diet:
            bar.set_clipping(True)

# Enable the picker state for the bars related to the Target_object at those same points
for bar in target_object:
    bar.set_picker(True)

plt.tight_layout()
plt.savefig("myplot.png")