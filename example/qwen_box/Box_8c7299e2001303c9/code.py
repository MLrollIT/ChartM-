from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Data
data = StringIO("""
"Property Type","2018","2019","2020"
"Residential",150000,120000,185000
"Commercial",200000,210000,145000
"Industrial",180000,225000,215000
""")
df = pd.read_csv(data)

# Preprocessing
data = [df['2018'].values, df['2019'].values, df['2020'].values]
labels = ['2018', '2019', '2020']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create a figure instance
fig, ax = plt.subplots(figsize=(10, 7))

# Change the background color here
ax.set_facecolor('white')  # This line was modified

# Create the boxplot with customization
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.5, labels=labels, sym=".")

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Property Prices Over The Years')
ax.set_xlabel('Year')
ax.set_ylabel('Property Price')

# Add grid
ax.grid(True)

# Add legend
ax.legend([bp["boxes"][i] for i in range(len(bp["boxes"]))], ['Residential', 'Commercial', 'Industrial'], loc='upper right')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")