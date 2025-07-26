from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
"Workout Regimes","Year 1","Year 2","Year 3"
"Yoga",100,75,95
"Crossfit",200,120,50
"Zumba",300,310,290
""")

# Read data into pandas DataFrame
df = pd.read_csv(data, quotechar='"')

# Create figure and axes objects
fig, ax = plt.subplots()

# Remove the grid lines
# ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)  # This line was removed

# Set the background color of the chart figure to white
ax.set_facecolor('white')  # Changed 'lightgray' to 'white'

# Plot data
for row in df.itertuples(index=False):
    ax.plot(["Year 1", "Year 2", "Year 3"], [row[1], row[2], row[3]], 
            label=row[0], linestyle='--', linewidth=2, marker='o', markersize=6, alpha=0.7)

# Add title and labels
ax.set_title('Workout Regimes Over Three Years')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Participants')

# Add legend and annotation
for line, name in zip(ax.lines, df["Workout Regimes"]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=10, va="center")

ax.legend(loc='best')

# Ensure layout is tight
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")