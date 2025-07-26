from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Creating DataFrame from given data
data = {'Year': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Sparrow': [2000, 2100, 2150, 7000, 2200, 2250, 2300, 2350, 2400],
        'Hummingbird': [1000, 3500, 3700, 4000, 4100, 8000, 4200, 4300, 4400],
        'Eagle': [500, 450, 400, 350, 300, 250, 200, 150, 100]}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot([df['Sparrow'], df['Hummingbird'], df['Eagle']], 
                patch_artist=True, 
                notch=True, 
                vert=0, 
                labels=['Sparrow', 'Hummingbird', 'Eagle'],
                sym='r+',
                widths=0.5)

colors = ['#0000FF', '#00FF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Remove grid
ax.grid(False)

# Set background color to white
ax.set_facecolor('white')

# Set title and labels
ax.set_title('Birds Population Over Years')
ax.set_xlabel('Population')
ax.set_ylabel('Bird Species')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the median line's linestyle of the boxes that contain the center point of the bounding box to 'dashed'
for box in bp['boxes']:
    x = box.get_x()
    y = box.get_y()
    width = box.get_width()
    height = box.get_height()
    center = (x + width / 2, y + height / 2)
    median_line = ax.plot(center, [y + height / 2, y + height / 2], linestyle='dashed', color='black', picker=True)

# Save the modified figure
plt.savefig("Edit_figure.png")