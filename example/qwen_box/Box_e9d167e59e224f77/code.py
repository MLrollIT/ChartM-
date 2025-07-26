from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Data
data = StringIO("""
Year,Crime Rate
2000,5000
2001,4500
2002,8000
2003,3000
2004,7000
2005,6000
2006,2000
2007,5000
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['Crime Rate'].values]
labels = ['Crime Rate']
colors = ['#1f77b4']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create an axes instance
ax.set_facecolor('#f0f0f0')

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Crime Rate Over The Years')
ax.set_xlabel('Year')
ax.set_ylabel('Crime Rate')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")