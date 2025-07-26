from io import StringIO
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    "Disaster": ["Earthquake", "Earthquake", "Earthquake", "Earthquake", "Earthquake", "Flood", "Flood", "Flood", "Flood", "Flood", "Hurricane", "Hurricane", "Hurricane", "Hurricane", "Hurricane", "Tornado", "Tornado", "Tornado", "Tornado", "Tornado"],
    "Local Economy Impact": [5000, 8000, 12000, 7000, 13000, 4500, 3000, 7000, 3000, 4500, 4000, 2000, 9000, 2000, 4000, 3500, 1500, 6000, 1500, 3500],
    "Year": [2000, 2001, 2002, 2003, 2004, 2000, 2001, 2002, 2003, 2004, 2000, 2001, 2002, 2003, 2004, 2000, 2001, 2002, 2003, 2004]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10,6))

# Define a color for each disaster type
disaster_colors = {
    "Earthquake": "red",
    "Flood": "blue",
    "Hurricane": "green",
    "Tornado": "purple"
}

disasters = df["Disaster"].unique()

for disaster in disasters:
    subset = df[df["Disaster"] == disaster]
    ax.scatter(subset["Year"], subset["Local Economy Impact"], label=disaster, color=disaster_colors[disaster])

ax.set_xlabel('Year')
ax.set_ylabel('Local Economy Impact')
ax.set_title('Impact of Natural Disasters on Local Economies')
ax.grid(True)
ax.set_facecolor('lightgray')
ax.legend()

# Change the size of the scatter points that share the same legend as those containing the center point of the bounding box to 73.
# Update the edge color of these points to #c402a4 and set the edge width to 1.9.
bbox = ax.bbox
bbox_points = [p for p in bbox if p.contains_point((2002.5, 12000))]
for p in bbox_points:
    subset = df[df["Disaster"] == p.legend_elements()[0][0]]
    ax.scatter(subset["Year"], subset["Local Economy Impact"], s=73, edgecolor="#c402a4", linewidth=1.9)

plt.tight_layout()
plt.savefig("myplot.png")