from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# The given data
data = [
    ("2000", 2000, 1550),
    ("2001", 2100, 1600),
    ("2002", 2200, 1650),
    ("2003", 2300, 1700),
    ("2004", 2100, 1750),
    ("2005", 2600, 1800),
    ("2006", 2400, 1850),
    ("2007", 2500, 2100),
    ("2008", 2200, 2500),
]

years, industrial_emissions, transportation_emissions = zip(*data)

y = np.arange(len(years))  # the label locations
height = 0.3  # the height of the bars

fig, ax = plt.subplots()

rects1 = ax.barh(y + height/2, industrial_emissions, height, label='Industrial Emissions', color='skyblue', edgecolor='blue')
rects2 = ax.barh(y - height/2, transportation_emissions, height, label='Transportation Emissions', color='lightgreen', edgecolor='green')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Emissions (kt)')
ax.set_title('Industrial and Transportation Emissions (2000-2008)')
ax.set_yticks(y)
ax.set_yticklabels(years)
ax.legend(loc='upper right', ncol=1)
ax.grid(visible=True)
ax.set_facecolor('lightgray')

# Annotate the bar chart with data values.
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Invert the y-axis so the years read top-to-bottom
ax.invert_yaxis()

# Add a shadow effect to the bars that share the same legend with the bar that contains the center point of the bounding box
bbox = ax.bbox
bbox_points = bbox.get_points()
bbox_points[0, 0] -= 3.77
bbox_points[0, 1] -= 3.97
bbox_points[1, 0] -= 3.77
bbox_points[1, 1] -= 3.97
bbox.set_points(bbox_points)
bbox.set_clip_on(True)
bbox.set_clip_box(ax.bbox)
bbox.set_rasterized(True)

plt.tight_layout()
plt.savefig("myplot.png")