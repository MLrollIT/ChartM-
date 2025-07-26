from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Age Groups': ['15-24', '25-34', '35-44', '45-54', '55-64', '65+'],
        'Vegetables': [20, 30, 40, 50, 60, 70],
        'Meat': [80, 70, 60, 50, 40, 30],
        'Dairy': [100, 90, 80, 70, 60, 50]}
df = pd.DataFrame(data)

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot data
ax.scatter(df['Age Groups'], df['Vegetables'], marker='o', cmap='viridis', label='Vegetables')
ax.scatter(df['Age Groups'], df['Meat'], marker='s', cmap='plasma', label='Meat')
ax.scatter(df['Age Groups'], df['Dairy'], marker='^', cmap='inferno', label='Dairy')

# Set the title and labels
ax.set_title('Food consumption by Age Groups', fontsize=14)
ax.set_xlabel('Age Groups', fontsize=12)
ax.set_ylabel('Consumption', fontsize=12)

# Set the background color
ax.set_facecolor('gray')

# Add legend and grid
ax.legend()
ax.grid(True)

# Annotate data values above the point on the chart figure
for i in range(len(df)):
    ax.text(df['Age Groups'][i], df['Vegetables'][i], df['Vegetables'][i], ha='center', va='bottom')
    ax.text(df['Age Groups'][i], df['Meat'][i], df['Meat'][i], ha='center', va='bottom')
    ax.text(df['Age Groups'][i], df['Dairy'][i], df['Dairy'][i], ha='center', va='bottom')

# Change the color of the scatter points that share the same legend as those containing the center point of the bounding box to #821746
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox_points = [bbox.get_x(), bbox.get_y(), bbox.get_width(), bbox.get_height()]
bbox_points[0] += 5.4
bbox_points[1] += 5.4
bbox_points[2] -= 10.8
bbox_points[3] -= 10.8
bbox = bbox_points
ax.scatter(df['Age Groups'][bbox[0]:bbox[0]+bbox[2]], df['Vegetables'][bbox[1]:bbox[1]+bbox[3]], marker='o', cmap='viridis', label='Vegetables', color='#821746', alpha=0.5, edgecolors='none', zorder=10)
ax.scatter(df['Age Groups'][bbox[0]:bbox[0]+bbox[2]], df['Meat'][bbox[1]:bbox[1]+bbox[3]], marker='s', cmap='plasma', label='Meat', color='#821746', alpha=0.5, edgecolors='none', zorder=10)
ax.scatter(df['Age Groups'][bbox[0]:bbox[0]+bbox[2]], df['Dairy'][bbox[1]:bbox[1]+bbox[3]], marker='^', cmap='inferno', label='Dairy', color='#821746', alpha=0.5, edgecolors='none', zorder=10)

# Apply a shadow effect to these points with an offset of 5.4 pixels and a foreground color of silver
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox_points = [bbox.get_x(), bbox.get_y(), bbox.get_width(), bbox.get_height()]
bbox_points[0] += 5.4
bbox_points[1] += 5.4
bbox_points[2] -= 10.8
bbox_points[3] -= 10.8
bbox = bbox_points
ax.scatter(df['Age Groups'][bbox[0]:bbox[0]+bbox[2]], df['Vegetables'][bbox[1]:bbox[1]+bbox[3]], marker='o', cmap='viridis', label='Vegetables', color='#821746', alpha=0.5, edgecolors='none', zorder=10, shadow=True, offset=5.4, facecolor='silver