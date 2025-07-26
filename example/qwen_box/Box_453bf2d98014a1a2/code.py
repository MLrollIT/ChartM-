from io import StringIO
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {'Age_Group': ['20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100'],
        'Running': [140, 160, 180, 210, 200, 180, 220, 180],
        'Yoga': [180, 220, 210, 205, 180, 160, 140, 120],
        'Weightlifting': [200, 210, 190, 205, 215, 210, 190, 160]}

df = pd.DataFrame(data)

# Prepare data for box plot
plot_data = [df['Running'], df['Yoga'], df['Weightlifting']]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = ['Running', 'Yoga', 'Weightlifting'], 
                sym = "ro", widths = 0.4)

colors = ['#0000FF', '#00FF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Age Group vs Fitness Activity")
plt.xlabel("Fitness Activity")
plt.ylabel("Frequency")

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2]], ['Running', 'Yoga', 'Weightlifting'], loc='upper right')

# Adding grid
ax.grid(True)

# Change the facecolor of the figure to white
fig.patch.set_facecolor('white')

# Apply a stroke to box's whiskers and caps that contains the center point of the bounding box with a linewidth of 2.04 and a foreground color of #fa62a8.
for whisker in bp['whiskers']:
    whisker.set_color('#fa62a8')
    whisker.set_linewidth(2.04)
for cap in bp['caps']:
    cap.set_color('#fa62a8')
    cap.set_linewidth(2.04)

plt.tight_layout()
plt.savefig("myplot.png")