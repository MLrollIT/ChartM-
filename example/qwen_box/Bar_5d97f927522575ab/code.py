from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
data = {
    'Year': [2016, 2017, 2018, 2019, 2020, 2021],
    'PC Game Market': [101.63, 99.69, 95.18, 93.12, 98.44, 93.23],
    'Mobile Game Market': [40.58, 56.07, 70.31, 86.22, 77.24, 92.12],
    'Console Game Market': [35.51, 33.46, 34.27, 40.28, 51.53, 55.67]
}

x = np.arange(len(data['Year']))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

# Loop over the data dict, skipping the 'Year' key
for market, values in {k: v for k, v in data.items() if k != 'Year'}.items():
    offset = width * multiplier
    bars = ax.bar(x + offset, values, width, label=market, edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year')
ax.set_ylabel('Market Size (in billion $)')
ax.set_title('Game Market Size by Platform and Year')
ax.set_xticks(x + width)
ax.set_xticklabels(data['Year'])
ax.legend(loc='upper left', ncol=3)
ax.set_ylim(0, max(max(data['PC Game Market']), max(data['Mobile Game Market']), max(data['Console Game Market'])) + 10)
ax.grid(True)
ax.set_facecolor('lightgray')

# Adjust the transparency of the bars that share the same legend with the bar that contains the center point of the bounding box to 0.29
bbox = ax.bbox
bbox_points = bbox.get_points()
bbox_points[1, 0] = 0.29
bbox.set_points(bbox_points)
bbox.set_boxstyle('square,pad=0.1')
bbox.set_clip_on(True)

plt.tight_layout()
plt.savefig("myplot.png")