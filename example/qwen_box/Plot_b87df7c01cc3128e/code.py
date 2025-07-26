from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = StringIO("""
Natural Disasters,2000,2001,2002,2003,2004
Earthquakes,200,300,250,150,100
Floods,100,200,350,300,200
Volcanic Eruptions,50,70,30,120,90
Wildfires,100,150,200,100,50
Hurricanes,150,250,200,400,350
""")
df = pd.read_csv(data, index_col=0)

# Plot
fig, ax = plt.subplots()

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['red', 'green', 'blue', 'purple', 'orange']
markers = ['.', ',', 'o', 'v', '^']
linewidths = [1.0, 1.5, 2.0, 2.5, 3.0]
alphas = [0.7, 0.8, 0.9, 1.0, 0.6]

for idx, disaster in enumerate(df.index):
    ax.plot(df.columns, df.loc[disaster], 
            linestyle=linestyles[idx % len(linestyles)], 
            color=colors[idx % len(colors)], 
            marker=markers[idx % len(markers)], 
            linewidth=linewidths[idx % len(linewidths)], 
            alpha=alphas[idx % len(alphas)], 
            label=disaster)
    for x, y in zip(df.columns, df.loc[disaster]):
        ax.text(int(x), y, str(y))

# Annotations
for line, name in zip(ax.lines, df.index):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

ax.set_xlabel('Year')
ax.set_ylabel('Frequency')
ax.set_title('Frequency of Natural Disasters Over the Years')
ax.legend()
ax.grid(True)
ax.set_facecolor('gray')
plt.tight_layout()
plt.savefig('myplot.png')