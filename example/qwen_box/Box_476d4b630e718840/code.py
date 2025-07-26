from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Year,"Satellite Launches","Space Missions","Investment in Space Technology"
1990,100,5,1
1995,50,10,1.5
2000,150,15,2
2005,120,20,3
2010,75,25,2.5
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Satellite Launches'].values, df['Space Missions'].values, df['Investment in Space Technology'].values]
labels = ['Satellite Launches', 'Space Missions', 'Investment in Space Technology']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Investment, Satellite Launches and Space Missions Over The Years')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Modify the label of the box that contains the center point of the bounding box to 'A new Label'
# Adjust its transform to use the figure's coordinate system, focusing only on the portion at the center point
bbox = ax.bbox_to_transform(ax.bbox.get_points()[:, 0])
bbox = bbox.transformed(fig.transFigure.inverted())
bbox = bbox.get_points()[:, 0]
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.05, bbox[1] + 0.05
bbox = bbox[0] + 0.0