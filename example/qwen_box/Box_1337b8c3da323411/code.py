from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Prepare data
decades = ['1960', '1970', '1980', '1990', '2000', '2010', '2020', '2030']
trend_scores = [20, 25, 40, 35, 60, 65, 90, 30]

# Create figure and axis
fig, ax = plt.subplots(figsize =(10, 7))

# Create box plot
bp = ax.boxplot(trend_scores, patch_artist = True, notch = True, vert = 0, widths=0.5, sym='gD')

# Create a gradient color list from blue to red
n_boxes = len(bp['boxes'])
colors = [(i / n_boxes, 0, 1 - i / n_boxes) for i in range(n_boxes)]

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Change the outlier marker color to magenta
for flier in bp['fliers']:
    flier.set(marker='o', color='magenta', alpha=0.5)

# Add a grid
ax.grid(True)

# Set the background color of the figure
ax.set_facecolor('lightgray')

# Set labels and title
ax.set_xlabel('Fashion Trend Score')
ax.set_ylabel('Decade')
plt.title('Fashion Trend Score by Decade')

# Show values on the plot
for i, v in enumerate(trend_scores):
    ax.text(v + 3, i + .25, str(v), color='blue', fontweight='bold')

# Add legend
ax.legend([bp["boxes"][0]], ['Fashion Trend Score'], loc='upper left')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')