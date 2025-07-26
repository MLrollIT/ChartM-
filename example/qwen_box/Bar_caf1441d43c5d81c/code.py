from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

data = {
    "Blue Whale": (3000, 3500, 2000),
    "Tuna": (80000, 60000, 30000),
    "Cod": (120000, 50000, 75000),
    "Sea Turtles": (500, 300, 150),
    "Salmon": (100000, 120000, 90000),
    "Sharks": (15000, 7500, 10000)
}

years = ["2000", "2010", "2020"]
species = list(data.keys())
values = np.array(list(data.values()))

num_species = len(species)
num_years = len(years)

bar_width = 0.2
index = np.arange(num_years)

fig, ax = plt.subplots()

for i in range(num_species):
    bars = ax.bar(index + i * bar_width, values[i], bar_width, label=species[i], edgecolor='black')
    ax.bar_label(bars)

ax.set_xlabel('Year')
ax.set_ylabel('Number of Marine Species')
ax.set_title('Number of Marine Species per Year')
ax.set_xticks(index + bar_width * (num_species - 1) / 2)
ax.set_xticklabels(years)
ax.legend(loc='upper right', ncol=1)
ax.grid(True)
ax.set_facecolor('lightgray')

# Change the fill pattern of the bars that share the same legend as those containing the center point of the bounding box to '.', and update their edge color to '#79aaa0'.
for i in range(num_species):
    if i == 2:
        bars = ax.bar(index + i * bar_width, values[i], bar_width, label=species[i], edgecolor='black')
        ax.bar_label(bars)
        bars.set_facecolor('.')
        bars.set_edgecolor('#79aaa0')

plt.tight_layout()
plt.savefig("myplot.png")