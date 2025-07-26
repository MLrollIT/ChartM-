from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Wildlife,Urbanization_Impact_1970,Urbanization_Impact_2020
Deer,80,55
Bear,50,40
Squirrel,70,75
Bird,80,60
Fox,25,35
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Urbanization_Impact_1970'].values, df['Urbanization_Impact_2020'].values]
labels = ['1970', '2020']
colors = ['#6baed6', '#fd8d3c']  # Changed colors here

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)  # This uses the new colors

# Set title and labels
ax.set_title('Urbanization Impact on Wildlife Over The Years')
ax.set_xlabel('Years')
ax.set_ylabel('Impact')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Modify the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = bbox.transformed(ax.transAxes.inverted())
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes.inverted())
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox = bbox.transformed(ax.transAxes)
bbox