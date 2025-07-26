from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
data = {
    "Age Groups":["15-24","25-34","35-44","45-54","55-64","65+"],
    "Vegetables":[20,30,40,50,60,70],
    "Meat":[80,70,60,50,40,30],
    "Dairy":[100,90,80,70,60,50]
}

# Convert dictionary to dataframe
df = pd.DataFrame(data)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot
bp = ax.boxplot([df["Vegetables"], df["Meat"], df["Dairy"]], patch_artist = True,
                notch = True, vert = 0, whis = 2, widths = 0.4, sym = 'r+')

colors = ['#0000FF', '#00FF00', '#FFFF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Adding labels 
ax.set_yticklabels(['Vegetables', 'Meat', 'Dairy'])

# Adding title and labels 
plt.title('Box Plot of Food Consumption by Age Groups')
plt.xlabel('Amount')
plt.ylabel('Type of food')

# Adding grid 
ax.grid(True)

# Changing background color 
ax.set_facecolor('lightgray')

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2]], ['Vegetables', 'Meat', 'Dairy'], loc='upper left')

plt.tight_layout()
plt.savefig("myplot.png")