from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
sports = ("Football", "Cricket", "Baseball", "Basketball", "Soccer", "Rugby")
popularity = np.array([120, 85, 160, 200, 100, 70])

fig, ax = plt.subplots()

# Plotting the data
bars = ax.barh(sports, popularity, align='center', color='skyblue', edgecolor='black')

# Adding labels to the bars
ax.bar_label(bars, label_type='center')

# Setting labels for x and y axes and the title
ax.set_xlabel('Popularity (in thousands)')
ax.set_ylabel('Sports')
ax.set_title('Popularity of Different Sports')

# Adding a grid and changing the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Change the color of the bars that contain the center point of the bounding box to #e18563
for bar in bars:
    if bar.get_width() == 200:
        bar.set_color('#e18563')

plt.tight_layout()
plt.savefig("myplot.png")