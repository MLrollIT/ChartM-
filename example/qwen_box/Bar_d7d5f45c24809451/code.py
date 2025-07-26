from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

countries = ['USA', 'UK', 'Germany', 'France', 'Italy', 'Spain', 'Canada', 'Australia']
consumption = [10000, 9000, 7500, 8000, 8200, 8500, 7000, 9500]

bars = ax.bar(countries, consumption, color='tab:blue', edgecolor='black')

ax.set_ylabel('Food Consumption (in tons)')
ax.set_title('Food Consumption by Country')
ax.set_facecolor('lightgrey')
ax.grid(True)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 100, yval, ha='center', va='bottom')

# Change the linestyle of the bars that contain the center point of the bounding box to '--'
# Additionally, enable rasterization for those bars by setting their rasterized state to True
bbox = dict(boxstyle="square", fc="white", ec="black", lw=1)
for bar in bars:
    if bar.get_x() + bar.get_width()/2 == 7500:
        bar.set_linestyle('--')
        bar.set_rasterized(True)
        bar.set_edgecolor('black')
        bar.set_facecolor('white')
        bar.set_boxstyle(bbox)

plt.tight_layout()
plt.savefig("myplot.png")