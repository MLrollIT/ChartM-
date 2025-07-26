from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# The given data
data = {
    "Species": ["Tuna", "Shark", "Cod", "Salmon", "Herring"],
    "2000": [500000, 400000, 350000, 500000, 400000],
    "2005": [400000, 300000, 300000, 550000, 350000],
    "2010": [350000, 350000, 250000, 500000, 325000],
    "2015": [250000, 200000, 150000, 450000, 300000]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Plot each species over the years
for species in df["Species"].unique():
    ax.plot(df.columns[1:], df[df["Species"] == species].values[0][1:], label=species)

# Set the chart title and labels
ax.set_title('Species Population Over the Years', fontsize=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population', fontsize=12)

# Add legends
ax.legend()

# Set background to white and remove grid
ax.set_facecolor('white')  # Change face color to white
ax.grid(False)             # Disable gridlines

# Add annotations
for i, txt in enumerate(df["Species"]):
    ax.annotate(txt, (df.columns[-1], df.iloc[i][-1]))

# Set the snap state of the line that contains the center point of the bounding box to True.
# Set the z-order of the same line to 17.
# Set the shadow effect of the same lines to the Target_object with a offset of (2.84,3.29).
ax.plot(df.columns[1:], df[df["Species"] == "Tuna"].values[0][1:], label="Tuna", snap=True, zorder=17, shadow=True, offset=(2.84,3.29))

plt.tight_layout()
plt.savefig("myplot.png")