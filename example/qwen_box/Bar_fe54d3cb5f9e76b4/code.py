from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    "Year": [2015, 2016, 2017, 2018, 2019, 2020],
    "Solar Power (GWh)": [206, 215, 550, 565, 540, 480],
    "Wind Power (GWh)": [450, 470, 480, 440, 750, 760],
}

fig, ax = plt.subplots()

# Bar width
width = 0.35

# The x locations for the groups
ind = np.arange(len(data["Year"]))

# Plot bars
bars1 = ax.bar(ind - width/2, data["Solar Power (GWh)"], width,
               label="Solar Power (GWh)", color='b', edgecolor='black')
bars2 = ax.bar(ind + width/2, data["Wind Power (GWh)"], width,
               label="Wind Power (GWh)", color='r', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year')
ax.set_ylabel('Power (GWh)')
ax.set_title('Yearly Solar and Wind Power Production')
ax.set_xticks(ind)
ax.set_xticklabels(data["Year"])
ax.legend(loc='upper left', ncol=1)

# Change background color to white and remove gridlines
ax.set_facecolor('white') # Changed from 'gray' to 'white'
ax.grid(False) # Changed from True to False

# Annotate bars
ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)

# Adjust the line width of the bars that share the same legend with the bar that contains the center point of the bounding box to 0.65.
for bar in bars1:
    if bar.get_label() == "Solar Power (GWh)":
        bar.set_linewidth(0.65)
for bar in bars2:
    if bar.get_label() == "Wind Power (GWh)":
        bar.set_linewidth(0.65)

plt.tight_layout()
plt.savefig("myplot.png")