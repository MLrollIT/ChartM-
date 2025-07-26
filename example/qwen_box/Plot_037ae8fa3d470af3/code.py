from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020])
remote_workers = np.array([200, 250, 220, 180, 210, 190, 1000])

# Plot
fig, ax = plt.subplots()
ax.plot(years, remote_workers, color='tab:blue', linestyle='-', linewidth=2, marker='o', markersize=6, alpha=0.7)

ax.annotate('Remote Workers', xy=(2020, 1000), xytext=(2020, 1000), ha='right')

# Title and labels
ax.set_title('Number of Remote Workers Over the Years')
ax.set_xlabel('Year')
ax.set_ylabel('Remote Workers (in thousands)')
ax.grid(True)
ax.set_facecolor('lightgray')

# Modify the transparency of the lines that contain the center point of the bounding box to 0.14
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox_points = bbox.get_points()
bbox_points[0] = (bbox_points[0][0], 0.14)
bbox_points[1] = (bbox_points[1][0], 0.14)
bbox.set_points(bbox_points)

# Ensure that the snap state for these lines is set to False
bbox.set_snap(False)

plt.tight_layout()
plt.savefig("myplot.png")