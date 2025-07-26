from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Load the data
data = StringIO("""Exercise Type,Popularity
Yoga,15
Weightlifting,35
Running,20
Cycling,40
Swimming,25""")
df = pd.read_csv(data)

fig, ax = plt.subplots()

# Plot the data with different line styles, markers and colors
l1, = ax.plot(df['Exercise Type'], df['Popularity'], linestyle='-', marker='o', color='blue', markersize=8, alpha=0.7, linewidth=2, label='Popularity')

ax.legend(loc='upper left', shadow=True)

# Annotate the data points
for x, y in zip(df['Exercise Type'], df['Popularity']):
    ax.text(x, y, str(y), color='blue', fontweight='bold')

# Set labels, title, and grid
ax.set_xlabel('Exercise Type')
ax.set_ylabel('Popularity')
ax.set_title('Popularity of Different Exercise Types')
ax.grid(True)

# Set the background color
ax.set_facecolor('lightgray')

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Set the snap state of the element that contains the center point of the bounding box to True
ax.figure.canvas.manager.set_snap(True)