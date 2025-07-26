from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
subjects = ("Mathematics", "Physics", "Chemistry", "Biology", "English", "History", "Geography")
popularity = (100, 200, 50, 300, 150, 50, 80)

x = np.arange(len(subjects))  # the label locations

fig, ax = plt.subplots()

# Plotting the bar chart
bars = ax.bar(x, popularity, tick_label=subjects, color="steelblue", edgecolor="black")

# Annotating the data value on the chart
ax.bar_label(bars)

# Adding labels and title
ax.set_ylabel('Popularity')
ax.set_xlabel('Subjects')
ax.set_title('Popularity of Different Subjects')

# Adding a legend
ax.legend(["Popularity"], loc='upper right')

# Setting the face color
ax.set_facecolor("lightgray")

# Adding grids
ax.grid(True)

# Updating the linewidth of the bars that contain the center point of the bounding box to 1.93
for bar in bars:
    if bar.get_x() + bar.get_width() / 2 == 1.93:
        bar.set_edgecolor("black")
        bar.set_rasterized(False)

plt.tight_layout()
plt.savefig("myplot.png")