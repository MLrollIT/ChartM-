from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {'Vacation Type': ['Cruise Vacations', 'Road Trips', 'Staycations'],
        '2018': [5000, 6300, 4000],
        '2019': [6000, 4500, 4200],
        '2020': [2500, 9000, 8400]}

df = pd.DataFrame(data)

# Prepare data for box plot
plot_data = [df['2018'], df['2019'], df['2020']]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = ['2018', '2019', '2020'], 
                sym = "ro", widths = 0.4)

colors = ['#0000FF', '#00FF00', '#FFFF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Vacation Type vs Years")
plt.xlabel("Years")
plt.ylabel("Vacation Type")

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2]], ['2018', '2019', '2020'], loc='upper right')

# Removing grid lines
plt.grid(False)  # Modified line

# Change the facecolor of the figure to white
fig.patch.set_facecolor('white')  # Modified line

plt.tight_layout()
plt.savefig("myplot.png")