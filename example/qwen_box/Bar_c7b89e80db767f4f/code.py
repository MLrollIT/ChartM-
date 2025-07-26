from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Community Service': [15, 14, 16, 15, 14, 15, 16, 17, 18, 20, 22],
    'Disaster Relief': [18, 20, 24, 22, 18, 20, 22, 21, 25, 24, 30],
    'Environmental Protection': [22, 21, 19, 18, 17, 18, 19, 20, 22, 20, 18]
}

x = np.arange(len(data['Year']))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in dict(list(data.items())[1:]).items():
    offset = width * multiplier
    bars = ax.bar(x + offset, measurement, width, label=attribute, color=['silver', 'gray', 'lightgray'][multiplier], edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year')
ax.set_ylabel('Number of activities')
ax.set_title('Activities by year')
ax.set_xticks(x + width, data['Year'])
ax.legend(loc='upper left')
ax.set_ylim(0, 35)
ax.grid(True)
ax.set_facecolor('white')

# Set the clipping box for the bars that share the same legend with the bar that contains the center point of the bounding box
bbox = plt.Bbox([[57, 270], [57 + 219, 270 + 427]])
for attribute, measurement in dict(list(data.items())[1:]).items():
    offset = width * multiplier
    bars = ax.bar(x + offset, measurement, width, label=attribute, color=['silver', 'gray', 'lightgray'][multiplier], edgecolor='black')
    ax.bar_label(bars, padding=3)
    multiplier += 1
    if attribute == 'Disaster Relief':
        bars.set_clip_box(bbox)
        bars.set_rasterized(False)

plt.tight_layout()
plt.savefig("myplot.png")