from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["1960", "1970", "1980", "1990", "2000", "2005", "2006", "2007", "2008", "2010", "2020"]
data = {
    'Satellites': [100, 500, 1000, 1500, 2000, 1000, 1500, 3000, 2500, 3000, 3500],
    'Rocket Debris': [0, 0, 200, 400, 600, 500, 600, 1200, 900, 1100, 1500],
    'Other Debris': [0, 50, 100, 300, 500, 400, 500, 1000, 800, 900, 1300],
}

x = np.arange(len(years))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots()

for attribute, values in data.items():
    offset = width * multiplier
    bars = ax.bar(x + offset, values, width, label=attribute)
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Objects', fontsize=14)  # Changed font size here
ax.set_title('Space Debris by Year', fontsize=20)  # Changed font size here
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=14)  # Changed font size here
ax.legend()
ax.grid(True)
ax.set_facecolor('gray')

# Update the label of the bars that share the same legend with the bar that contains the center point of the bounding box to 'A new Label'
for attribute, values in data.items():
    offset = width * multiplier
    bars = ax.bar(x + offset, values, width, label=attribute)
    ax.bar_label(bars, padding=3)
    if attribute == 'Rocket Debris':
        for bar in bars:
            bar.set_label('A new Label')
    multiplier += 1

plt.tight_layout()
plt.savefig("myplot.png")