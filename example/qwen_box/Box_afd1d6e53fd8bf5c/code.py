from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
"Architecture Type","Year 2010","Year 2020"
"Modern Architecture",500,250
"Gothic Architecture",300,800
"Victorian Architecture",700,350
"Romanesque Architecture",200,600
"Baroque Architecture",400,550
"Renaissance Architecture",600,700
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Year 2010'].values, df['Year 2020'].values]
labels = ['Year 2010', 'Year 2020']
colors = ['#1f77b4', '#ff7f0e']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Set the background color
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Architecture Popularity Over The Years')
ax.set_xlabel('Years')
ax.set_ylabel('Popularity')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Modify the center point of the bounding box
bbox = bp['boxes'][0].get_bbox()
bbox.set_facecolor('#48064f')
bbox.set_linestyle('dashed')

# Save the figure
plt.tight_layout()
plt.savefig("Edit_figure.png")