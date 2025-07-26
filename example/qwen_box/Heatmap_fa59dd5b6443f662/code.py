from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016]
organic_farming = [1000, 1250, 1500, 1750, 2500, 2000, 1500, 3000, 3500]
percentage_of_organic_farming = [0.5, 0.65, 0.67, 0.7, 1.5, 1.2, 0.9, 1.8, 2.1]

# Convert the data to a 2D array
data = np.array([organic_farming, percentage_of_organic_farming])

# Create a figure and axes
fig, ax = plt.subplots()

# Show the 2D array data as an image, with the alpha parameter set over 0.6, and using a colormap
im = ax.imshow(data, cmap='viridis', alpha=0.7)

# We want to show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)), labels=years)

# Set the labels for the y axis
ax.set_yticks(np.arange(len(['Organic Farming', 'Percentage of Organic Farming'])), labels=['Organic Farming', 'Percentage of Organic Farming'])

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(['Organic Farming', 'Percentage of Organic Farming'])):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

# Set the title
ax.set_title("Organic Farming (in hectares) and Percentage of Organic Farming Over the Years")

# Add a grid and set a light gray background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Make sure the layout is tight (no unnecessary padding)
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")