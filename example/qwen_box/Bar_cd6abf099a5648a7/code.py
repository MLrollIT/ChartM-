from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
households = ["Johnson Family", "Smith Family", "Brown Family", "Taylor Family", "Miller Family", "Davis Family", "Wilson Family"]
january = [120, 150, 180, 100, 160, 200, 90]
february = [135, 220, 190, 130, 170, 240, 110]
march = [110, 120, 150, 70, 200, 210, 80]

fig, ax = plt.subplots()

# Create a bar chart
y_pos = np.arange(len(households))
width = 0.2

# Define gradients for each month
gradient_blue = ['#08306b', '#08519c', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef']
gradient_orange = ['#a63603', '#e6550d', '#fd8d3c', '#fdae6b', '#fdd0a2', '#feedde', '#fff5eb']
gradient_green = ['#00441b', '#006d2c', '#238b45', '#41ab5d', '#74c476', '#a1d99b', '#c7e9c0']

bars1 = ax.barh(y_pos - width, january, width, color=gradient_blue, edgecolor='black', label='January')
bars2 = ax.barh(y_pos, february, width, color=gradient_orange, edgecolor='black', label='February')
bars3 = ax.barh(y_pos + width, march, width, color=gradient_green, edgecolor='black', label='March')

ax.set_yticks(y_pos)
ax.set_yticklabels(households)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Expenses')
ax.set_title('Household Expenses Over Time')
ax.legend()

# Annotate the data value on the chart figure
ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)
ax.bar_label(bars3, padding=3)

# Add grids and set background color
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot_modified.png")