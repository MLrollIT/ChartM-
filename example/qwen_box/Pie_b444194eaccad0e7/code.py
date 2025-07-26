from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data preparation
platforms = ["PlayStation", "Xbox", "PC", "Nintendo Switch", "Mobile", "Others"]
percentages = [20, 15, 30, 15, 15, 5]

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Function to format the percentage and absolute value
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

# Plotting the pie chart
wedges, texts, autotexts = ax.pie(percentages, 
                                  autopct=lambda pct: func(pct, percentages),
                                  textprops=dict(color="w"),
                                  explode=(0.1, 0, 0, 0, 0, 0),
                                  shadow=True,
                                  colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])

# Adding legend and title
ax.legend(wedges, platforms,
          title="Platforms",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Percentage of Gaming Platforms Usage")

# Setting the background color
fig.set_facecolor('lightgray')

# Modify the slices that contain the center point of the bounding box
for wedge in wedges:
    if wedge.contains_point((0.5, 0.5)):
        wedge.set_facecolor("#e2461f")
        wedge.set_edgecolor("#e2461f")
        wedge.set_linewidth(1.68)

plt.tight_layout()
plt.savefig("myplot.png")