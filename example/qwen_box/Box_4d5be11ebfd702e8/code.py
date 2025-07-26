from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Region,2010,2020
Asia,80,65
Europe,70,40
America,90,50
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['2010'].values, df['2020'].values]
labels = ['2010', '2020']
colors = ['#1f77b4', '#ff7f0e']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Population Change from 2010 to 2020')
ax.set_xlabel('Year')
ax.set_ylabel('Population')

# Change the face color of the chart
ax.set_facecolor('#f0f0f0')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], labels, loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")