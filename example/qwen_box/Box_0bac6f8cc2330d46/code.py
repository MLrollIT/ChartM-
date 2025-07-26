from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = '''Year,Childhood Obesity,Adult Obesity,Senior Obesity
2010,20,35,30
2011,22,37,34
2012,30,45,40
2013,35,55,50
2014,30,45,40
2015,32,47,42
2016,35,52,47
2017,40,57,52
2018,35,52,47
2019,45,62,57
2020,40,57,52
2021,50,67,62'''

# Read data into DataFrame
df = pd.read_csv(StringIO(data))

# Prepare data for box plot
plot_data = [df['Childhood Obesity'], df['Adult Obesity'], df['Senior Obesity']]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = ['Childhood Obesity', 'Adult Obesity', 'Senior Obesity'], 
                sym = "ro", widths = 0.4)

colors = ['#0000FF', '#00FF00', '#FFFF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
ax.set_title("Obesity Trends Over the Years")
ax.set_xlabel("Age Group")
ax.set_ylabel("Obesity Percentage (%)")

# Adding legend
ax.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2]], ['Childhood Obesity', 'Adult Obesity', 'Senior Obesity'], loc='upper right')

# Adding grid
ax.grid(True)

# Change the facecolor of the figure
fig.patch.set_facecolor('gray')

# Set the clipping state of the box that contains the center point of the bounding box to True
bp['boxes'][1].set_clip_on(True)

# Adjust the transformation of the same box to align with the data coordinate system
bp['boxes'][1].set_transform(ax.transData)

plt.tight_layout()
plt.savefig("myplot.png")