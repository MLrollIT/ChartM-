from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Creating a figure
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Setting data
drone_types = ["Consumer Drones", "Military Drones", "Commercial Drones"]
data = [40, 40, 20]

# Changing the background color of the figure
fig.set_facecolor('lightgray')

# Define a monochromatic color scheme in shades of blue
colors = ['#1f77b4', '#aec7e8', '#c6dbef']

# Creating pie chart with new color scheme
wedges, texts, autotexts = ax.pie(data, labels=drone_types, colors=colors, wedgeprops=dict(width=0.5), startangle=-40, autopct='%1.1f%%', pctdistance=0.8, explode = (0.1, 0.1, 0.1), shadow=True)

# Setting title
ax.set_title("Distribution of Drone Technologies")

# Setting properties for labels box
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

# Adding labels to each wedge
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(drone_types[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

# Tight layout
plt.tight_layout()

# Saving figure
plt.savefig("myplot.png")