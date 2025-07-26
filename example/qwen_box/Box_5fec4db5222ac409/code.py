from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = StringIO("""
Year,Software Sales,Software Use
2016,10000,20000
2017,12000,18000
2018,14000,15000
2019,10000,10000
2020,12000,20000
2021,16000,25000
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Software Sales'].values, df['Software Use'].values]
labels = ['Software Sales', 'Software Use']
colors = ['#1f77b4', '#ff7f0e']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Set the background color of the figure
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Software Sales and Use Over The Years')
ax.set_xlabel('Year')
ax.set_ylabel('Value')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Set a shadow effect to the boxes that contain the center point of the bounding box
for box in bp['boxes']:
    x, y = box.get_x(), box.get_y()
    width, height = box.get_width(), box.get_height()
    center_x = x + width / 2
    center_y = y + height / 2
    box.set_facecolor('#f1d4f8')
    box.set_alpha(0.515)
    box.set_edgecolor('black')
    box.set_boxstyle('square', pad=0.1, rounding_size=5, fc='white', ec='black')
    box.set_zorder(3)

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")