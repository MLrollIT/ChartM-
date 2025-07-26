from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
Natural Disasters,Local Economy 1,Local Economy 2,Local Economy 3
Earthquake,120,90,80
Flood,140,65,100
Hurricane,200,75,130
Tsunami,160,60,90
Wildfire,130,80,85
Volcano,180,95,115
Drought,110,70,80
Tornado,150,90,120
""")

df = pd.read_csv(data, sep=",")

natural_disasters = df["Natural Disasters"].values
local_economy = {
    "Local Economy 1": df["Local Economy 1"].values,
    "Local Economy 2": df["Local Economy 2"].values,
    "Local Economy 3": df["Local Economy 3"].values
}

width = 0.2

fig, ax = plt.subplots()

# Create an array with the position of each bar along the x-axis
x = np.arange(len(natural_disasters))

for i, (economy, values) in enumerate(local_economy.items()):
    ax.bar(x - width/2 + i*width, values, width, label=economy, edgecolor='black')

# Add title, labels and legend
ax.set_title("Impact of Natural Disasters on Local Economy")
ax.set_xlabel("Natural Disasters")
ax.set_ylabel("Economic Impact")
ax.set_xticks(x)
ax.set_xticklabels(natural_disasters)
ax.legend(loc="upper right")

# Add grids on the background
ax.grid(True)

# Set the face color to a light color
ax.set_facecolor('lightgray')

# Save chart as a png file
plt.tight_layout()
plt.savefig("myplot.png")