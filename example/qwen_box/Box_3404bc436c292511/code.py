from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given data
data = {'Country': ['USA', 'China', 'India', 'Brazil', 'Australia'],
        'Year 1': [100, 150, 120, 200, 80],
        'Year 2': [200, 160, 140, 210, 70],
        'Year 3': [170, 320, 120, 160, 150]
       }

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot([df['Year 1'], df['Year 2'], df['Year 3']], patch_artist=True,
                notch=True, vert=0, widths=0.5, labels=['Year 1', 'Year 2', 'Year 3'],
                flierprops={'marker':'o', 'markerfacecolor':'red', 'markersize':12,
                            'linestyle':'none', 'markeredgecolor':'black'}
               )

colors = ['#0000FF', '#00FF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Annotate data values
for i, line in enumerate(bp['medians']):
    x, y = line.get_xydata()[1]
    ax.annotate(f'{y:.1f}', (i+1.1, y), ha='center', va='center')

ax.set_title('Box plot of Yearly Data')
ax.set_xlabel('Years')
ax.set_ylabel('Data Value')
ax.legend([bp["boxes"][0]], ['Data'], loc='upper right')
ax.grid(True)
ax.set_facecolor('#f5f5f5')

# Set the rasterized state of the box body that contains the center point of the bounding box to True
# Set the snap state to False
for box in bp['boxes']:
    box.set_rasterized(True)
    box.set_snap(False)

plt.tight_layout()
plt.savefig("myplot.png")