from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Provided data
disasters = ("Hurricane", "Earthquake", "Tsunami", "Flood", "Drought")
economic_impact = np.array([10000, 7000, 5000, 4000, 2000])

fig, ax = plt.subplots()

bars = ax.barh(disasters, economic_impact, align='center', color='skyblue', edgecolor='black')

# Adding the labels
ax.bar_label(bars)

ax.set_yticks(np.arange(len(disasters)))
ax.set_yticklabels(disasters)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Economic Impact (in $)')
ax.set_title('Economic Impact of Different Disasters')
ax.grid(True)
ax.set_facecolor('white')  # Change the background color to white

# Update the linewidth of the bars that contain the center point of the bounding box to 1.60
# Set the snap state of these bars to False
for bar in bars:
    if bar.get_width() > 1000:
        bar.set_edgecolor('black')
        bar.set_linewidth(1.60)
        bar.set_snap(False)

plt.tight_layout()
plt.savefig("myplot.png")