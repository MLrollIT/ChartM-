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

# Change the color of the scatter points that share the same legend as those containing the center point of the bounding box to #622a8e
scatter_points = ax.collections
bbox = ax.bbox
bbox_points = [point for point in scatter_points if bbox.contains_point(point.get_xy())]
bbox_points[0].set_color('#622a8e')

plt.tight_layout()
plt.savefig("myplot.png")