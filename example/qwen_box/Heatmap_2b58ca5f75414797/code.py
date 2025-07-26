from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Create a list of species and years
species = ["Amazon Rainforest", "Siberian Taiga", "Australian Bush"]
years = ["Year 2000", "Year 2020"]

# Create a 2D array of the data
data = np.array([[5000, 3700],
                 [4200, 4000],
                 [3200, 1800]])

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a heatmap of the data using the 'plasma' colormap
im = ax.imshow(data, cmap='plasma', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(species)))
ax.set_yticklabels(species)

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations
for i in range(len(species)):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="w")

# Set the title of the chart
ax.set_title("Population of Species in Different Years")

# Add grids on the background
ax.grid(True)

# Set the background color of the chart figure
ax.set_facecolor('gray')

# Adjust layout to make sure the labels fit
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")