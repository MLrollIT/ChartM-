from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = pd.DataFrame({
    "Year": [2015, 2016, 2017, 2018, 2019, 2020],
    "Drone Production": [1000, 950, 870, 1050, 800, 1200],
    "Drone Sales": [500, 600, 400, 650, 450, 700]
})

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot([data['Drone Production'], data['Drone Sales']], patch_artist = True,
                notch = True, vert = 0, labels = ['Drone Production', 'Drone Sales'], widths=0.5)

# Gradient colors for the boxes
colors_production = ['#1E90FF', '#4169E1', '#6495ED', '#4682B4', '#5F9EA0', '#00BFFF']
colors_sales = ['#32CD32', '#98FB98', '#00FF00', '#008000', '#3CB371', '#90EE90']

# Apply gradient colors across the boxes for 'Drone Production'
for patch, color in zip(bp['boxes'], colors_production):
    patch.set_facecolor(color)

# Apply a different set of gradient colors across the boxes for 'Drone Sales'
for patch, color in zip(bp['boxes'], colors_sales):
    patch.set_facecolor(color)

# Setting title and labels
ax.set_title('Drone Production and Sales over Years')
ax.set_xlabel('Quantity')
ax.set_ylabel('Categories')

# Annotating data
for i in range(len(data['Year'])):
    ax.annotate(str(data['Year'][i]), (data['Drone Production'][i], 1),
                textcoords="offset points", xytext=(10,10), ha='center')
    ax.annotate(str(data['Year'][i]), (data['Drone Sales'][i], 0),
                textcoords="offset points", xytext=(10,-20), ha='center')

# Adding grid and setting background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Saving the figure
plt.tight_layout()
plt.savefig("myplot.png")