from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data in csv format
csv_data = "Travel Type,Popularity Score\nCar Travel,5\nTrain Travel,15\nBus Travel,7\nAir Travel,30\nBike Travel,9\nBoat Travel,20\nFoot Travel,3\nCamel Travel,8\nHorse Travel,12"

# Convert the csv data into a pandas dataframe
data = pd.read_csv(StringIO(csv_data))

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 7))

# Creating box plot
bp = ax.boxplot(data["Popularity Score"], patch_artist=True, notch=True, vert=0, widths=0.7, sym="r+")

# Set color for the box plot
bp['boxes'][0].set_facecolor('#0000FF')

# Add title and labels
plt.title("Popularity of Different Travel Types")
plt.xlabel("Popularity Score")
plt.ylabel("Travel Type")

# Add grid
ax.grid(True)

# Set background color
ax.set_facecolor('#D3D3D3')

# Add legend
plt.legend([bp["boxes"][0]], ['Travel Types'], loc='upper right')

# Annotate the data value on the chart figure
for i, v in enumerate(data["Popularity Score"]):
    ax.text(v+1, i+1, str(v), color='black', fontweight='bold')

# Set the layout tight
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")