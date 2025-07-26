import matplotlib.pyplot as plt
import numpy as np

# Data points for continents, energy consumption intervals, and frequencies
continents = ['Asia', 'Europe', 'North America', 'South America']
energy_consumption_intervals = ['10-20 GW', '20-30 GW', '30-40 GW', '40-50 GW', '50-60 GW']
frequencies = np.array([[8, 12, 10, 5, 3],
                        [5, 7, 8, 9, 6],
                        [6, 7, 4, 3, 2],
                        [2, 3, 5, 4, 1]])

# Plotting the histogram
fig, ax = plt.subplots()
width = 0.15
x = np.arange(len(energy_consumption_intervals))

for i, continent in enumerate(continents):
    ax.bar(x + width * i, frequencies[i], width=width, label=continent)

# Labeling the axes
plt.xlabel('Energy Consumption Intervals (GW)')
plt.ylabel('Number of Cities')

# Setting the title
plt.title('Energy Consumption in Major Cities')

# Adding a legend
ax.legend(loc='upper right')

# Adjusting the x-axis tick labels
ax.set_xticks(x + width * (len(continents) - 1) / 2)
ax.set_xticklabels(energy_consumption_intervals)

# Displaying the plot
plt.tight_layout()
plt.savefig("figure.png")

# Adjusting the opacity of the bars that share the same legend as the bar containing the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0.5), pad=10)
bbox = ax.bbox_to_anchor((0.5, 0