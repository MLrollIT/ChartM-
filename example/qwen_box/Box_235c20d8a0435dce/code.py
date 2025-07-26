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

# Define a gradient of blue tones
blue_gradients = ['#1E90FF', '#4169E1', '#0000FF', '#00008B']

for patch, color in zip(bp['boxes'], blue_gradients):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Weekly Stock Indices")
plt.xlabel("Weeks")
plt.ylabel("Stock Indices")

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2], bp["boxes"][3]], ['Week 1', 'Week 2', 'Week 3', 'Week 4'], loc='upper right')

# Removing grid
plt.grid(False)

# Change the facecolor of the figure
fig.patch.set_facecolor('gray')

# Change the clipping state of the boxes that contain the center point of the bounding box to False
for box in bp['boxes']:
    box.set_clip_on(False)

# Set the snap state of these boxes to False
for box in bp['boxes']:
    box.set_snap(False)

plt.tight_layout()
plt.savefig("myplot.png")