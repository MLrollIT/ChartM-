from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    'Earthquakes': [98, 90, 85, 78, 100, 75, 70, 68, 65, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42],
    'Hurricanes': [15, 20, 25, 30, 35, 40, 100, 95, 90, 80, 70, 60, 55, 50, 45, 40, 35, 30, 25, 20],
    'Floods': [50, 52, 55, 57, 60, 45, 42, 40, 38, 35, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55],
    'Wildfires': [20, 25, 30, 35, 40, 100, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],
    'Tornados': [80, 70, 60, 50, 45, 35, 30, 28, 26, 25, 24, 23, 22, 21, 20, 19, 18, 100, 95, 90]
}

fig, ax = plt.subplots()

x = np.arange(len(data['Year']))  # the label locations
height = 0.15  # the height of the bars
multiplier = 0
colors = ['red', 'blue', 'green', 'purple', 'orange']
disasters = ['Earthquakes', 'Hurricanes', 'Floods', 'Wildfires', 'Tornados']

for i, disaster in enumerate(disasters):
    offset = height * multiplier
    bars = ax.bar(x + offset, data[disaster], height, color=colors[i], edgecolor='black', label=disaster)
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year')
ax.set_ylabel('Number of Disasters')
ax.set_title('Number of Disasters per Year')
ax.set_xticks(x + height * 2)
ax.set_xticklabels(data['Year'], rotation=90)
ax.legend(loc='upper left', ncol=1)

# Remove grid and change background color to white
ax.grid(False)
ax.set_facecolor('white')

plt.tight_layout()
plt.savefig("myplot.png")