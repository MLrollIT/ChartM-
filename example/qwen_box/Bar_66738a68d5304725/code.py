from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io

# Given csv data
csv_data = """
Year, North America, Europe, Asia
2013, 12.7, 15.6, 18.9
2014, 13.5, 16.2, 22.3
2015, 14.2, 17.1, 20.8
2016, 15.0, 18.0, 23.5
2017, 16.1, 20.0, 18.0
2018, 14.8, 19.8, 25.5
2019, 15.5, 22.0, 24.0
"""
df = pd.read_csv(io.StringIO(csv_data), skipinitialspace=True)

# Extract columns
years = df['Year']
regions = df.columns[1:]

x = np.arange(len(years)) # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots()

for region in regions:
    offset = width * multiplier
    bars = ax.bar(x + offset, df[region], width, label=region, edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels
ax.set_ylabel('Population (in billions)')
ax.set_title('Population by Year and Region')
ax.set_xticks(x + width)
ax.set_xticklabels(years)
ax.legend()

ax.grid(True)
ax.set_facecolor('lightgray')
plt.tight_layout()

# Set the clipping state of the bars that share the same legend with the bar that contains the center point of the bounding box to False
# Change the linewidth of those bars to 3.38
for region in regions:
    offset = width * multiplier
    bars = ax.bar(x + offset, df[region], width, label=region, edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1
    if region == 'Europe':
        for bar in bars:
            bar.set_clip_on(False)
            bar.set_linewidth(3.38)

plt.savefig("myplot.png")