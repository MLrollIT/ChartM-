from io import StringIO
import numpy as np

# Required Libraries
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Year': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Advancements': [100, 120, 450, 150, 200, 250, 1000, 900, 1100]}
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Advancements'], linestyle='--', linewidth=2, color='blue', marker='o', markersize=6, alpha=0.7, label='Advancements')

# Grid
ax.grid(axis='both', color='0.95')

# Labels, Title and Legend
ax.set_xlabel('Year')
ax.set_ylabel('Advancements')
ax.set_title('Yearly Advancements')
ax.legend()

# Annotate
for i, txt in enumerate(df['Advancements']):
    ax.annotate(txt, (df['Year'][i], df['Advancements'][i]))

# Background Color
ax.set_facecolor('lightgray')

# Set animated state of plot that contains center point of bounding box to True
ax.figure.canvas.draw()
bbox = ax.bbox_to_anchor([0.5, 0.5], fig)
bbox = ax.bbox_to_anchor([0.5, 0.5], fig, animated=True)

# Update label of lines
ax.set_xlabel('Year')
ax.set_ylabel('Advancements')
ax.set_title('Yearly Advancements')
ax.legend()

# Annotate
for i, txt in enumerate(df['Advancements']):
    ax.annotate(txt, (df['Year'][i], df['Advancements'][i]))

# Background Color
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig('myplot.png')