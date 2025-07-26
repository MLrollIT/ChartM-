from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Year,Compact Cars,SUVs,Trucks
2010,1000,1200,1400
2011,1200,1100,1300
2012,1400,1000,1200
2013,1600,1400,1100
2014,1800,1600,1000
2015,2000,1800,1300
2016,1600,2000,1500
2017,1700,1500,1600
2018,1900,1300,1400
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Compact Cars'].values, df['SUVs'].values, df['Trucks'].values]
labels = ['Compact Cars', 'SUVs', 'Trucks']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Vehicle Sales Over The Years')
ax.set_xlabel('Vehicle Type')
ax.set_ylabel('Sales')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Modify the boxes that contain the center point of the bounding box
for box in bp['boxes']:
    # Get the center point of the box
    center = box.get_center()
    # Set the transparency of the box
    box.set_alpha(0.88)
    # Set the stroke of the box
    box.set_edgecolor('#c6171d')
    box.set_linewidth(4.84)

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")