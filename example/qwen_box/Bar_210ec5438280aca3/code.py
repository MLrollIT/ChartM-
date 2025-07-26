from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Create data
appliances = ["Refrigerator", "Air Conditioner", "Washing Machine", "Dishwasher", "Microwave"]
usage = np.array([[10,12,10,8,9], [3,5,10,2,3], [5,7,7,6,10], [1,1,5,1,1], [2,3,3,5,6]])
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']

fig, ax = plt.subplots()

bars = ax.bar(appliances, usage.mean(axis=1), color=colors, edgecolor='black')

# Title and labels
ax.set_title('Average Usage of Home Appliances')
ax.set_xlabel('Appliance')
ax.set_ylabel('Usage')

# Grid and background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Bar labels
ax.bar_label(bars)

# Change the rasterized state of the bars that contain the center point of the bounding box to False, and set their snap state to True as well.
for bar in bars:
    if bar.get_bbox().contains((0.5, 0.5)):
        bar.set_rasterized(False)
        bar.set_snap(True)

plt.tight_layout()
plt.savefig("myplot.png")