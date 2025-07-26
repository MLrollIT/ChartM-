from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Create DataFrame from the given data
data = {'Age Group': ['18-25', '25-35', '35-45', '45-55'],
        'Vegan': [200, 450, 500, 600],
        'Gluten-Free': [400, 550, 300, 700],
        'Keto': [600, 350, 200, 1000]}
df = pd.DataFrame(data)

# Prepare data for box plot
data_to_plot = [df['Vegan'].values, df['Gluten-Free'].values, df['Keto'].values]

# Create figure and axes
fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot
bp = ax.boxplot(data_to_plot, patch_artist = True, notch = True, vert = 0, widths=0.3)

colors = ['#0000FF', '#00FF00', '#FFFF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Adding background grid
ax.grid(True)

# Setting background color
ax.set_facecolor('#f0f0f0') 

# Setting title and labels
ax.set_title('Diet Preference by Age Group')
ax.set_xlabel('Diet Type')
ax.set_ylabel('Number of People')

# Adding legend
ax.legend(['Vegan', 'Gluten-Free', 'Keto'], loc='upper right')

# Updating the linewidth of the median, whiskers and caps line of the box that contain the center point of the bounding box
for median in bp['medians']:
    median.set_linewidth(1.48)
    median.set_dashes('dashed')

# Updating the linewidth of the median, whiskers and caps line of the box that contain the center point of the bounding box
for whisker in bp['whiskers']:
    whisker.set_linewidth(1.48)
    whisker.set_dashes('dashed')

# Updating the linewidth of the median, whiskers and caps line of the box that contain the center point of the bounding box
for cap in bp['caps']:
    cap.set_linewidth(1.48)
    cap.set_dashes('dashed')

# Saving the figure
plt.tight_layout()
plt.savefig('myplot.png')