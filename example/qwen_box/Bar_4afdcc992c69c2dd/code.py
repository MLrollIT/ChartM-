from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

platforms = ("Facebook", "Instagram", "Snapchat", "Twitter", "LinkedIn", "YouTube")
scores = np.array([85, 120, 80, 70, 90, 110])
width = 0.5

fig, ax = plt.subplots()

# Set background color
ax.set_facecolor('gray')

bars = ax.bar(platforms, scores, width, color='blue', edgecolor='black')

ax.set_title('Impact Score of Different Social Media Platforms')
ax.set_xlabel('Social Media Platform')
ax.set_ylabel('Impact Score')

# Add grid
ax.grid(True)

# Add labels to each bar
ax.bar_label(bars, label_type="center")

# Change the transparency of the bars that contain the center point of the bounding box to 0.535
for bar in bars:
    if bar.get_bbox().contains((120, 70)):
        bar.set_alpha(0.535)

plt.tight_layout()
plt.savefig("myplot.png")