from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
data = {
    'Year': [2016, 2017, 2018, 2019, 2020],
    'Mobile Gaming': [35.6, 46.1, 56.7, 68.5, 77.2],
    'Console Gaming': [29.4, 30.1, 34.7, 35.7, 47.9],
    'PC Gaming': [36.9, 32.3, 28.1, 25.3, 33.6],
}

df = pd.DataFrame(data)

years = df['Year']

# Define width of the bars
width = 0.25

fig, ax = plt.subplots()

# Plot bars for each gaming type
rects1 = ax.bar(years - width, df['Mobile Gaming'], width, label='Mobile Gaming',
                edgecolor='black', color='cyan', tick_label=years)
rects2 = ax.bar(years, df['Console Gaming'], width, label='Console Gaming',
                edgecolor='black', color='magenta', tick_label=years)
rects3 = ax.bar(years + width, df['PC Gaming'], width, label='PC Gaming',
                edgecolor='black', color='yellow', tick_label=years)

# Adding labels to the bars
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

# Add some text for labels, title
ax.set_xlabel('Year')
ax.set_ylabel('Gaming Type Percentage')
ax.set_title('Gaming Type Percentage by Year')

# Adding legends and grid
ax.legend()
ax.grid(True)

# Set background color to light blue
ax.set_facecolor('#ADD8E6')  # Light blue color

# Adjust the transparency of the bars that share the same legend with the bar that contains the center point of the bounding box to 0.22, and ensure that the snap state for these bars is set to True.
for bar in rects1:
    bar.set_alpha(0.22)
    bar.set_snap(True)
for bar in rects2:
    bar.set_alpha(0.22)
    bar.set_snap(True)
for bar in rects3:
    bar.set_alpha(0.22)
    bar.set_snap(True)

plt.tight_layout()
plt.savefig("myplot.png")