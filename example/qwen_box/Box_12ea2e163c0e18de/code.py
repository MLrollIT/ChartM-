from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Year': [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016],
    'Organic Farming (in hectares)': [1000, 1250, 1500, 1750, 2500, 2000, 1500, 3000, 3500],
    'Percentage of Organic Farming': [0.5, 0.65, 0.67, 0.7, 1.5, 1.2, 0.9, 1.8, 2.1]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create figure and axis
fig, ax = plt.subplots(figsize =(10, 7))

# Box plot
bp = ax.boxplot([df['Organic Farming (in hectares)'], df['Percentage of Organic Farming']], 
                patch_artist = True, notch = True, vert = 0,
                labels = ['Organic Farming (in hectares)', 'Percentage of Organic Farming'], 
                widths = 0.4)

colors = ['#0000FF', '#00FF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Title and labels
ax.set_title('Organic Farming & Percentage of Organic Farming')
ax.set_xlabel('Variables')
ax.set_ylabel('Values')

# Grid and background color
ax.grid(True)
ax.set_facecolor('lightgrey')

# Modify the linestyle of the boxes that contain the center point of the bounding box to 'dotted'
for patch in bp['boxes']:
    patch.set_linestyle('dotted')

# Save figure
plt.tight_layout()
plt.savefig("myplot.png")