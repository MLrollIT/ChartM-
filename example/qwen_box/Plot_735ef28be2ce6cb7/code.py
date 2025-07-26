from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {"Region": ["North America", "Latin America", "Europe", "Africa", "Asia", "Australia", "Antarctica", "East Asia", "Middle East"],
        "Home schooling rate": [5, 8, 10, 3, 7, 11, 1, 6, 4]}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

x = np.arange(len(df["Region"]))

# Changed line color to green and marker color to red
line, = ax.plot(x, df["Home schooling rate"], marker='o', linestyle='-', linewidth=2, markersize=6, color='green', markerfacecolor='red', alpha=0.8, label="Home schooling rate")
for i in range(len(x)):
    ax.text(i, df["Home schooling rate"][i], df["Home schooling rate"][i], ha='center')

ax.set_xlabel('Region')
ax.set_ylabel('Home Schooling Rate (%)')
ax.set_title('Home Schooling Rates by Region')
ax.legend(loc='upper right', shadow=True)
ax.set_xticks(x)
ax.set_xticklabels(df["Region"], rotation=45)
ax.grid(True)
ax.set_facecolor('lightgray')

# Change the marker style of the lines that contain the center point of the bounding box to 'D'
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.