from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = '''\
Year,Crime Rate
2000,5000
2001,4500
2002,8000
2003,3000
2004,7000
2005,6000
2006,2000
2007,5000
'''
df = pd.read_csv(StringIO(data))

# Plotting the data
fig, ax = plt.subplots()

ax.plot(df['Year'], df['Crime Rate'], marker='o', color='b', linestyle='-', linewidth=2, markersize=6, alpha=0.7, label='Crime Rate')

# Annotating the lines
for i, txt in enumerate(df['Crime Rate']):
    ax.annotate(txt, (df['Year'][i], df['Crime Rate'][i]))

ax.set_xlabel('Year')
ax.set_ylabel('Crime Rate')
ax.set_title('Crime Rate Over the Years')
ax.legend(loc='best')
ax.grid(True)
ax.set_facecolor('lightgray')

# Adjust the linewidth of the plot that contains the center point of the bounding box to 1.58
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox_points = bbox.get_points()
bbox_points[0] = (bbox_points[0][0], bbox_points[0][1] - 0.05)
bbox_points[1] = (bbox_points[1][0], bbox_points[1][1] - 0.05)
bbox.set_points(bbox_points)

# Enable the rasterized state for that plot by setting it to True
bbox.set_rasterized(True)

plt.tight_layout()
plt.savefig('myplot.png')