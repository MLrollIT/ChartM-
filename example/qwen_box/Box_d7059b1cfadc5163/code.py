from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {'State': ['Texas', 'California', 'New York', 'Florida', 'Illinois', 'Ohio', 'Pennsylvania'],
        'Unemployment Rate': [[5.9, 6.2, 6.5, 6.1, 5.7, 5.3, 5.5], 
                              [7.4, 7.6, 7.8, 7.5, 7.2, 7.0, 6.9],
                              [6.4, 6.6, 6.9, 6.7, 6.4, 6.6, 7.0],
                              [4.9, 5.1, 5.4, 5.2, 5.0, 5.1, 5.3],
                              [7.7, 7.6, 7.5, 6.9, 7.4, 7.9, 8.2],
                              [6.1, 6.3, 6.6, 6.4, 6.2, 6.5, 6.8],
                              [6.3, 6.2, 5.9, 6.4, 6.9, 7.3, 7.6]]}

df = pd.DataFrame(data)

# Prepare data for box plot
plot_data = [df['Unemployment Rate'][i] for i in range(len(df))]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = df['State'].tolist(), 
                sym = "ro", widths = 0.4)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF', '#FF0000', '#800080']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("State vs Unemployment Rate")
plt.xlabel("State")
plt.ylabel("Unemployment Rate")

# Adding legend
plt.legend([bp["boxes"][i] for i in range(len(df))], df['State'].tolist(), loc='upper right')

# Adding grid
plt.grid(True)

# Change the facecolor of the figure
fig.patch.set_facecolor('gray')

# Update all of the lines' linewidth of the boxes that contain the center point of the bounding box to 0.92 and color to #cbafcc, and adjust their transform to the data coordinate system.
for box in bp['boxes']:
    x = box.get_x()
    y = box.get_y()
    width = box.get_width()
    height = box.get_height()
    center = (x + width / 2, y + height / 2)
    box.set_linewidth(0.92)
    box.set_facecolor('#cbafcc')
    box.set_transform(ax.transData)

plt.tight_layout()
plt.savefig("myplot.png")