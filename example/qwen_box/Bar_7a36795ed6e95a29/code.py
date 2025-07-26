from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Here is the given csv data
csv_data = """
Year,City A,City B,City C
2013,120,200,180
2014,130,220,170
2015,140,240,160
2016,150,260,150
2017,160,250,140
2018,170,240,130
2019,180,230,120
2020,190,210,110
"""

# We will use pandas to read the csv data
df = pd.read_csv(StringIO(csv_data))

# Prepare data for plotting
years = df['Year'].values
cities = df.columns[1:]
data = df[cities].values.T

fig, ax = plt.subplots()

# Define bar width
bar_width = 0.2
bar_positions = np.arange(len(years))

# Plot each city's data
for i, city in enumerate(cities):
    offset = bar_width * i
    bars = ax.bar(bar_positions + offset, data[i], bar_width, label=city, color=f"C{i}", edgecolor='black')
    ax.bar_label(bars, padding=3)

ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.set_title('Yearly data for each city')
ax.set_xticks(bar_positions + bar_width / 2)
ax.set_xticklabels(years)
ax.legend()

# Remove grid lines and change background color
ax.grid(False) # This line removes the grid lines
ax.set_facecolor('white') # This line changes the background color to white

# Set the clip box of the bars that share the same legend with the bar that contains the center point of the bounding box
bbox = plt.Bbox([[488, 143], [488 + 836, 143 + 119]])
for i, city in enumerate(cities):
    offset = bar_width * i
    bars = ax.bar(bar_positions + offset, data[i], bar_width, label=city, color=f"C{i}", edgecolor='black')
    ax.bar_label(bars, padding=3)
    ax.bar_label(bars, bbox=bbox, label_type='center', color='black', fontweight='bold')

plt.tight_layout()
plt.savefig("myplot.png")