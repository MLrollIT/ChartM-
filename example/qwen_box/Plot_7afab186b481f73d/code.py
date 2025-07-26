from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Let's define our data
data = {
    "Decade": [1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040],
    "Fashion Trend 1": [20, 30, 100, 40, 60, 50, 30, 70, 90],
    "Fashion Trend 2": [50, 60, 40, 70, 100, 80, 60, 50, 40],
    "Fashion Trend 3": [80, 70, 60, 90, 50, 100, 40, 80, 100],
}

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Create a figure and an axis
fig, ax = plt.subplots()

# Set the face color of the figure
fig.patch.set_facecolor('gray')

# Draw each line with different settings
ax.plot(df['Decade'], df['Fashion Trend 1'], color='red', linestyle='-', marker='o', markersize=5, linewidth=2, alpha=0.7, label='Fashion Trend 1')
ax.plot(df['Decade'], df['Fashion Trend 2'], color='blue', linestyle='--', marker='v', markersize=5, linewidth=2, alpha=0.7, label='Fashion Trend 2')
ax.plot(df['Decade'], df['Fashion Trend 3'], color='green', linestyle='-.', marker='^', markersize=5, linewidth=2, alpha=0.7, label='Fashion Trend 3')

# Set the title and labels for the chart
ax.set_title('Fashion Trends Over the Decades')
ax.set_xlabel('Decade')
ax.set_ylabel('Popularity')

# Add a legend
ax.legend()

# Add grid
ax.grid(True)

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, ['Fashion Trend 1', 'Fashion Trend 2', 'Fashion Trend 3']):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=10, va="center")

# Save the final figure
plt.tight_layout()
plt.savefig('myplot.png')