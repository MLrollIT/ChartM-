from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
decades = ('1920', '1930', '1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010')
trends = {
    'Flapper Dresses': np.array([10, 5, 3, 4, 3, 6, 8, 4, 12, 16]),
    'Platform Shoes': np.array([1, 2, 8, 18, 15, 22, 12, 7, 10, 5]),
    'Leather Jackets': np.array([3, 4, 12, 9, 14, 18, 20, 22, 19, 15]),
}
width = 0.3  # Width of the bars

# Create the figure and the axes
fig, ax = plt.subplots()

# Variables to store the bar positions and the bars
bar_positions = np.arange(len(decades))
bars = []

# Loop through the trends and create the bars
for i, (trend, counts) in enumerate(trends.items()):
    # Positions of the bars
    positions = bar_positions + i * width

    # Create the bars
    p = ax.bar(positions, counts, width, label=trend, color=['gray', 'blue', 'green'][i])

    # Store the bars
    bars.append(p)

# Set the title, labels, and legend
ax.set_title('Trends by Decade')
ax.set_xlabel('Decade')
ax.set_ylabel('Count')
ax.legend()

# Add labels to each bar
for bar in bars:
    ax.bar_label(bar, label_type='center')

# Add a grid and change the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Change the x-axis ticks
ax.set_xticks(bar_positions + width)
ax.set_xticklabels(decades)

# Add a tight layout and save the figure
plt.tight_layout()
plt.savefig('myplot.png')