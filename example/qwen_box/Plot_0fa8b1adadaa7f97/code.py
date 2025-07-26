from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
from random import choice

# Data
data = StringIO("""
Year,Africa,Asia,South America
1990,150,120,80
2000,140,115,75
2010,130,110,70
2020,90,105,65
2025,70,200,60
2030,65,195,55
2035,60,110,50
2040,70,120,45
2045,80,130,40
2050,90,140,35
""")
df = pd.read_csv(data)

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['blue', 'green', 'red', 'cyan', 'magenta']
markers = ['.', 'o', 'v', '^', 's']

# Plot
fig, ax = plt.subplots()
for i in range(df.shape[1]-1):
    ax.plot(df['Year'], df.iloc[:, i+1], 
            linestyle=choice(linestyles), 
            color=colors[i], 
            marker=markers[i], 
            markersize=10, 
            alpha=0.7, 
            label=df.columns[i+1])
    
    ax.annotate(df.columns[i+1], 
                (df['Year'].iat[-1], df.iloc[-1, i+1]))

ax.set_title('Population Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.legend(title='Continent:')
ax.grid(True)
fig.set_facecolor('lightgrey')

# Adjust the transparency of the lines that contain the center point of the bounding box to 0.08.
# For the same lines, set the marker edge width to 1.59.
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox_points = bbox.get_points()
bbox_points[0] = (bbox_points[0][0], bbox_points[0][1] - 0.08)
bbox_points[1] = (bbox_points[1][0], bbox_points[1][1] - 0.08)
bbox.set_points(bbox_points)

bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox_points = bbox.get_points()
bbox_points[0] = (bbox_points[0][0], bbox_points[0][1] + 1.59)
bbox_points[1] = (bbox_points[1][0], bbox_points[1][1] + 1.59)
bbox.set_points(bbox_points)

plt.tight_layout()
plt.savefig('myplot.png')