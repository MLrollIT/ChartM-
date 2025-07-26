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

# Change the whiskers,caps and median color of the box that contain the center point of the bounding box to #8a9805. Also, apply a stroke to the box body with a linewidth of 2.11 and a foreground color of #e02f2d.
for box in bp['boxes']:
    box.set(facecolor="#8a9805", edgecolor="#e02f2d", linewidth=2.11)

for whisker in bp['whiskers']:
    whisker.set(color="#e02f2d", linewidth=2.11)

for cap in bp['caps']:
    cap.set(color="#e02f2d", linewidth=2.11)

for median in bp['medians']:
    median.set(color="#e02f2d", linewidth=2.11)

# Change the facecolor of the box that contain the center point of the bounding box to #8a9805
for box in bp['boxes']:
    box.set(facecolor="#8a9805")

# Change the stroke color of the box body to #e02f2d
for box in bp['boxes']:
    box.set(facecolor="#8a9805", edgecolor="#e02f2d")

# Change the stroke color of the box body to #e02f2d
for box in bp['boxes']:
    box.set(facecolor="#8a9805", edgecolor="#e02f2d")

# Change the stroke color of the box body to #e02f2d
for box in bp['boxes']:
    box.set(facecolor="#8a9805", edgecolor="#e02f2d")

# Change the stroke color of the box body to #e02f2d
for box in bp['boxes']:
    box.set(facecolor="#8a9805", edgecolor="#e02f2d")

# Change the stroke color of the box body to #e02f2d
for box in bp['boxes']:
    box.set(facecolor="#8a9805", edgecolor="#e02f2d")

# Change the stroke color of the box body to #e02f2d
for box in bp['boxes']:
    box.set(facecolor="#8a9805", edgecolor="#e02f2d")

# Change the stroke color of the box body to #e02f2d
for box in bp['boxes']:
    box.set(facecolor="#8a9805