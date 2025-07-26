from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# given data
demographic = ['Teenagers', 'Adults', 'Elderly', 'Infants']
hours_of_sleep = [6.5, 7.3, 5.2, 14.8]

# create figure and axis
fig, ax = plt.subplots()

# scatter plot
scatter = ax.scatter(demographic, hours_of_sleep, marker='o', cmap='viridis')

# labels
ax.set_xlabel('Demographic')
ax.set_ylabel('Hours of Sleep')
ax.set_title('Hours of Sleep by Demographic')

# grid and background color
ax.grid(False)  # Remove grid lines
ax.set_facecolor('white')  # Change background color to white

# annotate each point
for i, txt in enumerate(hours_of_sleep):
    ax.annotate(txt, (demographic[i], hours_of_sleep[i]))

# modify scatter points
scatter.set_facecolor('#d3bf37')
scatter.set_edgecolor('#d3bf37')
scatter.set_alpha(0.5)

plt.tight_layout()

plt.savefig("myplot.png")