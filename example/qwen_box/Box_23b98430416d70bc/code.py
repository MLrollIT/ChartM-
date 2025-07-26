import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
data = {'Smartphone Feature': ['Web Browsing', 'Social Media', 'Gaming', 'Music and Video', 'Email and Messaging', 'Other'],
        'Week 1': [50, 80, 60, 70, 40, 30],
        'Week 2': [70, 70, 50, 60, 60, 34],
        'Week 3': [90, 75, 40, 50, 70, 38],
        'Week 4': [30, 140, 120, 51, 50, 140],
        'Week 5': [35, 100, 115, 70, 52, 130]}

df = pd.DataFrame(data)

# Prepare data for box plot
plot_data = [df['Week 1'], df['Week 2'], df['Week 3'], df['Week 4'], df['Week 5']]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'], 
                sym = "ro", widths = 0.4)

# Define blue gradient colors
colors = ['#003366', '#336699', '#6699CC', '#99CCFF', '#CCCCFF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Weekly Smartphone Feature Usage")
plt.xlabel("Weeks")
plt.ylabel("Usage")

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2], bp["boxes"][3], bp["boxes"][4]], 
           ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'], loc='upper right')

# Adding grid
plt.grid(True)

# Change the facecolor of the figure
fig.patch.set_facecolor('gray')

# Adjust the transparency of the boxes that contain the center point of the bounding box to 0.32
for box in bp['boxes']:
    box.set_alpha(0.32)

# Enable the picker state for these same boxes by setting it to True
for box in bp['boxes']:
    box.set_picker(True)

plt.tight_layout()
plt.savefig("Edit_figure.png")