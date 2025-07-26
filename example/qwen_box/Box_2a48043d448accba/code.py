from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame from the provided data
data = {'Year': [2013, 2014, 2015, 2016, 2017, 2018, 2019],
        'North America': [12.7, 13.5, 14.2, 15.0, 16.1, 14.8, 15.5],
        'Europe': [15.6, 16.2, 17.1, 18.0, 20.0, 19.8, 22.0],
        'Asia': [18.9, 22.3, 20.8, 23.5, 18.0, 25.5, 24.0]}
df = pd.DataFrame(data)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 7))

# Creating box plot
colors = ['#0000FF', '#00FF00', '#FFFF00']
bp = ax.boxplot([df['North America'], df['Europe'], df['Asia']], patch_artist=True,
                notch=True, vert=0, widths=0.6)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting labels
ax.set_yticklabels(['North America', 'Europe', 'Asia'])

# Setting title and labels
plt.title('Box Plot of Data')
plt.xlabel('Values')
plt.ylabel('Regions')

# Setting grid
ax.grid(True)

# Setting face color
ax.set_facecolor('gray')

# Save the figure
plt.tight_layout()
plt.savefig('myplot.png')

# Update the label of the box that contains the center point of the bounding box to 'A new Label', and ensure that the rasterized state of this box is set to False.
for box in bp['boxes']:
    box.set_label('A new Label')
    box.set_rasterized(False)

# Save the figure
plt.tight_layout()
plt.savefig('Edit_figure.png')