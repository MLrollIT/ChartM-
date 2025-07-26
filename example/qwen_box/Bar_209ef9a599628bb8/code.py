from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006])
wealth = np.array([1000, 1500, 2000, 2500, 3000, 1500, 4000])

# Create the figure and the axes
fig, ax = plt.subplots()

# Create the bar chart
bars = ax.bar(years, wealth, color='skyblue', edgecolor='black', tick_label=years)

# Add labels to the bars
ax.bar_label(bars, label_type='center')

# Set the labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Wealth')
ax.set_title('Wealth by Year')

# Add a grid and set the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Set the animated state of the bars that contain the center point of the bounding box to False
center_point = 2003
animated_bars = [bar for bar in bars if bar.get_x() <= center_point and bar.get_width() >= 200]
for bar in animated_bars:
    bar.set_animated(False)
    bar.set_visible(False)

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")