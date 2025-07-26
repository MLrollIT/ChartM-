from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
segments = np.array(["Residential", "Commercial", "Industrial", "Agricultural", "Luxury", "Suburban"])
prices = np.array([500000, 700000, 300000, 200000, 800000, 400000])

fig, ax = plt.subplots()

# Draw the bar chart
bars = ax.bar(segments, prices, color='skyblue', edgecolor='black')

# Set larger font sizes for the labels and title
ax.set_xlabel('Real Estate Segment', fontsize=14)
ax.set_ylabel('Price', fontsize=14)
ax.set_title('Prices of Different Real Estate Segments', fontsize=16)

ax.set_facecolor('lightgray')
ax.grid(True)

# Add data labels
ax.bar_label(bars)

# Change the border thickness of the bars that contain the center point of the bounding box to 1.604, and update their color to black
for bar in bars:
    if bar.get_x() + bar.get_width() / 2 == 300000:
        bar.set_edgecolor('black')
        bar.set_linewidth(1.604)

plt.tight_layout()
plt.savefig("myplot.png")