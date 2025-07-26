import matplotlib.pyplot as plt
import numpy as np

# Data points for energy consumption levels and frequencies
energy_levels = ['100-500 GWh', '500-1000 GWh', '1000-1500 GWh', '1500-2000 GWh', '2000-2500 GWh']
frequencies = [20, 35, 25, 15, 10]

# Plotting the histogram
plt.bar(energy_levels, frequencies, color='blue')

# Labeling the axes
plt.xlabel('Energy Consumption Levels (GWh)', fontsize=12)
plt.ylabel('Number of Countries', fontsize=12)

# Setting the title
plt.title('Energy Consumption Trends Over 10 Years', fontsize=16)

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Adding a shadow effect to the bars that contain the center point of the bounding box
bbox = (2.50, 2.46)
shadow_color = 'gold'
line_color = '#b11a94'
for i in range(len(energy_levels)):
    if i in [1, 3]:
        plt.bar(energy_levels[i], frequencies[i], color=line_color, edgecolor=line_color, linewidth=2, shadow=True, shadowoffsetx=2.5, shadowcolor=shadow_color, bottom=frequencies[:i].sum())

# Displaying the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")