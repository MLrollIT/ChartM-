from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = """
Age Group,Relaxation Habits Percentage
"Under 18","15%"
"18-24","20%"
"25-34","25%"
"35-44","15%"
"45-54","10%"
"55-64","10%"
"65+","5%"
"""
# Read the data into a pandas DataFrame
df = pd.read_csv(StringIO(data), quotechar='"')

# Extract labels and sizes for the pie chart
labels = df['Age Group']
sizes = df['Relaxation Habits Percentage'].str.rstrip('%').astype('float')

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%', pctdistance=1.1, labeldistance=1.2, 
       textprops={'size': 'large'}, radius=0.5, explode=[0.05]*len(sizes), shadow=True,
       colors=plt.get_cmap("tab20").colors)

# Set the title and legend
plt.title('Distribution of Relaxation Habits by Age Group')
plt.legend(labels, title="Age Group", loc="upper right")

# Set background color
ax.set_facecolor('gray')

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the transparency of the slices that contain the center point of the bounding box to 0.43
# Also, ensure that the picker state for these slices is disabled by setting it to False
# This can be done by accessing the patches of the pie chart and modifying their properties
patches, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%.0f%%', pctdistance=1.1, labeldistance=1.2, 
       textprops={'size': 'large'}, radius=0.5, explode=[0.05]*len(sizes), shadow=True,
       colors=plt.get_cmap("tab20").colors)

# Get the center point of the bounding box
bbox = ax.bbox

# Get the patches that contain the center point of the bounding box
center_patches = [patch for patch in patches if patch.get_bbox() == bbox]

# Set the transparency of the center patches to 0.43
for patch in center_patches:
    patch.set_alpha(0.43)

# Set the picker state of the center patches to False
for patch in center_patches:
    patch.set_picker(False)

# Save the modified figure
plt.savefig("Edit_figure.png")