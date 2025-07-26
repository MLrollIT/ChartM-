from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dataframe from the provided data
data = {
    "Platform": ["Facebook", "Instagram", "Twitter", "Snapchat", "LinkedIn", "Pinterest", "Reddit", "WeChat", "WhatsApp"],
    "2016": [100, 80, 90, 70, 60, 50, 30, 20, 10],
    "2017": [120, 110, 70, 100, 80, 75, 60, 40, 5],
    "2018": [85, 130, 95, 70, 85, 55, 65, 45, 30],
}
df = pd.DataFrame(data)
platforms = df["Platform"].values
years = df.columns[1:]

# Convert the dataframe to a 2D array
values = df[years].values

fig, ax = plt.subplots()

# Set the color of the figure to white
fig.patch.set_facecolor('white')

# Show the heatmap
im = ax.imshow(values, cmap="YlGnBu", alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)), labels=years)
ax.set_yticks(np.arange(len(platforms)), labels=platforms)

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations
for i in range(len(platforms)):
    for j in range(len(years)):
        text = ax.text(j, i, values[i, j], ha="center", va="center", color="w")

# Set labels and title
ax.set_title("Social Media Usage Over Years")
ax.set_xlabel("Years")
ax.set_ylabel("Platforms")

# Remove the grid
ax.grid(False)

# Adjust the font size of the annotations in the cells that contain the center point of the bounding box to 16, and change the edge color of those same cells to #b6fceb
for i in range(len(platforms)):
    for j in range(len(years)):
        if i == j:
            text = ax.text(j, i, values[i, j], ha="center", va="center", color="w", fontsize=16, edgecolor="#b6fceb")

fig.tight_layout()
plt.savefig("myplot.png")