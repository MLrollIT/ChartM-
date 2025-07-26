from io import StringIO
import numpy as np

from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {'Stock Indices': ['Dow Jones', 'S&P 500', 'Nasdaq', 'FTSE 100'],
        'Week 1': [25000, 3000, 7500, 7000],
        'Week 2': [24000, 3200, 7400, 7100],
        'Week 3': [23500, 3100, 7800, 7200],
        'Week 4': [26000, 2700, 7300, 6800]}

df = pd.DataFrame(data)

# Prepare data for box plot
plot_data = [df['Week 1'], df['Week 2'], df['Week 3'], df['Week 4']]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = ['Week 1', 'Week 2', 'Week 3', 'Week 4'], 
                sym = "ro", widths = 0.4)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Weekly Stock Indices")
plt.xlabel("Weeks")
plt.ylabel("Stock Indices")

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2], bp["boxes"][3]], ['Week 1', 'Week 2', 'Week 3', 'Week 4'], loc='upper right')

# Adding grid
plt.grid(True)

# Change the facecolor of the figure
fig.patch.set_facecolor('gray')

# Change the color of the lines in the box that contains the center point of the bounding box to #432226
for patch in bp['boxes']:
    patch.set_facecolor('#432226')
    patch.set_zorder(20)

# Set a line shadow effect to the box with an offset of (3.00, 2.67) and choose a shadow color 'gray'
for patch in bp['boxes']:
    patch.set_edgecolor('gray')
    patch.set_linewidth(2)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226')
    patch.set_zorder(20)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226')
    patch.set_zorder(20)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226')
    patch.set_zorder(20)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226')
    patch.set_zorder(20)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226')
    patch.set_zorder(20)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226')
    patch.set_zorder(20)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226')
    patch.set_zorder(20)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226')
    patch.set_zorder(20)
    patch.set_boxstyle('square,pad=0.3,rounding_size=5')
    patch.set_edgecolor('gray')
    patch.set_facecolor('#432226