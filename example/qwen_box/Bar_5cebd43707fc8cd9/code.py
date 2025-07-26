from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
years = ('2000', '2005', '2010', '2015', '2020', '2025')
co2_emissions = (15, 30, 60, 50, 45, 80)
air_quality_index = (80, 85, 70, 90, 70, 60)
population_density = (150, 200, 400, 500, 600, 700)
y_pos = np.arange(len(years))

# Create subplots
fig, ax = plt.subplots()

# Plotting data with new color scheme
co2_bars = ax.bar(y_pos - 0.2, co2_emissions, 0.2, color='darkred', align='center', edgecolor='black', tick_label=years)
aqi_bars = ax.bar(y_pos, air_quality_index, 0.2, color='deepskyblue', align='center', edgecolor='black')
pd_bars = ax.bar(y_pos + 0.2, population_density, 0.2, color='limegreen', align='center', edgecolor='black')

# Adding labels
ax.bar_label(co2_bars)
ax.bar_label(aqi_bars)
ax.bar_label(pd_bars)

# Setting title, labels and legends
ax.set_title('Yearly Environmental Data')
ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.legend(['CO2 Emissions', 'Air Quality Index', 'Population Density'])

# Inverting y-axis and setting background color
ax.invert_yaxis()
ax.grid(True)
ax.set_facecolor('lightgray')

# Save the plot
plt.tight_layout()
plt.savefig("myplot.png")