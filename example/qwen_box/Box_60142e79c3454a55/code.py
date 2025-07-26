from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# data
data = {'Year': [1990, 2000, 2010, 2020],
        'Liberalism': [200, 210, 220, 250],
        'Conservatism': [250, 230, 220, 300],
        'Socialism': [300, 280, 260, 240],
        'Libertarianism': [350, 370, 400, 360]}
df = pd.DataFrame(data)

# Creating box plot
fig, ax = plt.subplots(figsize =(10, 7))
bp = ax.boxplot(df.iloc[:,1:].T, patch_artist = True,
                notch = True, vert = 0, whis = 2,
                widths = 0.4, sym='r+')

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Adding title and labels
plt.title('Ideologies over Years')
plt.xlabel('Ideologies') 
plt.ylabel('Popularity') 
plt.xticks([1, 2, 3, 4], ['Liberalism', 'Conservatism', 'Socialism', 'Libertarianism'])

# Adding legend
plt.legend([bp["boxes"][0]], ['Ideologies'], loc='upper left')

# Annotating data value
for line, year in zip(bp['medians'], df['Year']):
    # get position data for median line
    x, y = line.get_xydata()[1] 
    plt.text(x, y, 'Year {}'.format(year))

# Adding grid
plt.grid(True)

# Changing the background color
fig.set_facecolor('gray')

# Set the clipping box for the boxes that contain the center point of the bounding box
bbox = matplotlib.transforms.Bbox([[98, 55], [98 + 498, 55 + 431]])
for box in bp['boxes']:
    box.set_clip_box(bbox)

# Enable the rasterized state for the boxes linked to the same points
for box in bp['boxes']:
    box.set_rasterized(True)

plt.tight_layout()
plt.savefig('myplot.png')