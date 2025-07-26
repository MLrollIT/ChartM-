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

# Adjust the transparency of the scatter points that share the same legend as those containing the center point of the bounding box to 0.42
bbox = ax.bbox
bbox_points = bbox.get_points()
bbox_points[10] = (bbox_points[10][0], bbox_points[10][1])
bbox_points[11] = (bbox_points[11][0], bbox_points[11][1])
bbox_points[12] = (bbox_points[12][0], bbox_points[12][1])
bbox_points[13] = (bbox_points[13][0], bbox_points[13][1])
bbox_points[14] = (bbox_points[14][0], bbox_points[14][1])
bbox_points[15] = (bbox_points[15][0], bbox_points[15][1])
bbox_points[16] = (bbox_points[16][0], bbox_points[16][1])
bbox_points[17] = (bbox_points[17][0], bbox_points[17][1])
bbox_points[18] = (bbox_points[18][0], bbox_points[18][1])
bbox_points[19] = (bbox_points[19][0], bbox_points[19][1])
bbox_points[20] = (bbox_points[20][0], bbox_points[20][1])
bbox_points[21] = (bbox_points[21][0], bbox_points[21][1])
bbox_points[22] = (bbox_points[22][0], bbox_points[22][1])
bbox_points[23] = (bbox_points[23][0], bbox_points[23][1])
bbox_points[24] = (bbox_points[24][0], bbox_points[24][1])
bbox_points[25] = (bbox_points[25][0], bbox_points[25][1])
bbox_points[26] = (bbox_points[26][0], bbox_points[26][1])
bbox_points[27] = (bbox_points[27][0], bbox_points[27][1])
bbox_points[28] = (bbox_points[28][0],