from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
data = {
    "Year": [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
    "Brent Crude": [72.44, 96.94, 61.74, 79.61, 111.26, 111.63, 108.56, 98.97, 52.32],
    "West Texas Intermediate": [72.34, 99.67, 59.65, 79.48, 94.88, 94.05, 97.98, 93.17, 48.66]
}

# Create the figure and the axes
fig, ax = plt.subplots()

# Set the bar width
bar_width = 0.35

# Set the positions of the bars on the x axis
r1 = np.arange(len(data["Year"]))  # the label locations
r2 = [x + bar_width for x in r1]

# Create the bars
bars1 = ax.bar(r1, data["Brent Crude"], width=bar_width, color='b', edgecolor='grey', label='Brent Crude')
bars2 = ax.bar(r2, data["West Texas Intermediate"], width=bar_width, color='r', edgecolor='grey', label='West Texas Intermediate')

# Add the data value on the top of each bar
ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)

# Custom the subplot layout
ax.set_xlabel('Year')
ax.set_ylabel('Average Oil Price ($)')
ax.set_title('Average Oil Price of Brent Crude and WTI from 2007 to 2015')
ax.set_xticks([r + bar_width / 2 for r in range(len(data["Year"]))])
ax.set_xticklabels(data["Year"])
ax.legend()

# Set the background color
ax.set_facecolor('lightgray')
ax.grid(True)

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")