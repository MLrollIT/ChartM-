from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the data
data = {'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007],
        'Climate Change Effects': [0.4, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 2.0],
        'Greenhouse Gas Emissions': [1.2, 1.1, 0.9, 0.5, 0.4, 0.3, 0.2, 1.5],
        'Global Average Temperature': [0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 1.0]}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Plot the data with markers and different line styles, and change the color as per the instructions
ax.scatter(df['Year'], df['Climate Change Effects'], marker='o', label='Climate Change Effects', linestyle='-', color='yellow')
ax.scatter(df['Year'], df['Greenhouse Gas Emissions'], marker='*', label='Greenhouse Gas Emissions', linestyle='--', color='purple')
ax.scatter(df['Year'], df['Global Average Temperature'], marker='^', label='Global Average Temperature', linestyle='-.', color='cyan')

# Set the title and labels
ax.set_title('Yearly Climate Data')
ax.set_xlabel('Year')
ax.set_ylabel('Values')

# Set the background color to gray
ax.set_facecolor('gray')

# Add a grid
ax.grid(True)

# Add a legend
ax.legend()

# Annotate data values above the points
for i, txt in enumerate(df['Climate Change Effects']):
    ax.annotate(txt, (df['Year'][i], df['Climate Change Effects'][i]))
for i, txt in enumerate(df['Greenhouse Gas Emissions']):
    ax.annotate(txt, (df['Year'][i], df['Greenhouse Gas Emissions'][i]))
for i, txt in enumerate(df['Global Average Temperature']):
    ax.annotate(txt, (df['Year'][i], df['Global Average Temperature'][i]))

# Change the transparency of the points that shares the same legend with the point containing the center point of the bounding box to 0.58 and set their shape to '>'
ax.scatter(df['Year'][4], df['Climate Change Effects'][4], marker='>', label='Climate Change Effects', linestyle='-', color='yellow', alpha=0.58)
ax.scatter(df['Year'][4], df['Greenhouse Gas Emissions'][4], marker='*', label='Greenhouse Gas Emissions', linestyle='--', color='purple', alpha=0.58)

plt.tight_layout()
plt.savefig("myplot.png")