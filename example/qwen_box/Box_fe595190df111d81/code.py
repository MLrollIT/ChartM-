from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# Data
data = StringIO("""
AR Devices,AR Applications,AR Investments
150,200,1000
120,190,700
180,220,1100
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['AR Devices'].values, df['AR Applications'].values, df['AR Investments'].values]
labels = ['AR Devices', 'AR Applications', 'AR Investments']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Change the background color of the chart figure
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

# Change the color of the box body that contain the center point of the bounding box to #f4f6ef
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_edgecolor('#f4f6ef')

# Set title and labels
ax.set_title('AR Devices, Applications and Investments')
ax.set_xlabel('AR Categories')
ax.set_ylabel('Values')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")