from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Type of Alcohol": ["Beer", "Wine", "Spirits", "Beer", "Wine", "Spirits", "Beer"],
    "Consumption": [100, 120, 80, 70, 150, 50, 90]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.set_facecolor('lightgray')
ax.grid(True)

types = df['Type of Alcohol'].unique()
colors = ['green', 'blue', 'red']
edgecolors = ['darkgreen', 'darkblue', 'darkred']
bars = []

for i, alcohol_type in enumerate(types):
    consumption = df[df['Type of Alcohol'] == alcohol_type]['Consumption']
    bar = ax.bar(alcohol_type, consumption.sum(), color=colors[i], edgecolor=edgecolors[i])
    bars.append(bar)

ax.set_title('Total Consumption of Different Types of Alcohol')
ax.set_xlabel('Type of Alcohol')
ax.set_ylabel('Total Consumption')

ax.legend(bars, types, loc="upper right")

for bar in bars:
    ax.bar_label(bar)

plt.tight_layout()
plt.savefig('myplot.png')