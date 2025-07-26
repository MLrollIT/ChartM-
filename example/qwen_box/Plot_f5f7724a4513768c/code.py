from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Data
data = """Sport,2008,2012,2016
Baseball,10000,11000,3000
Basketball,5000,3000,5000
Football,15000,10000,20000
Golf,8000,7000,9000
Tennis,6000,12000,8000"""
df = pd.read_csv(StringIO(data), index_col=0)

# Plot
fig, ax = plt.subplots()

# Define a color map
colors = plt.cm.viridis(np.linspace(0, 1, len(df)))

for (sport, values), color in zip(df.iterrows(), colors):
    ax.plot(values.index, values, marker='o', linestyle='--', label=sport, linewidth=2.0, alpha=0.7, color=color)
    for x, y in zip(values.index, values):
        ax.text(x, y, str(y), color=color)

# Annotations
for line, name in zip(ax.lines, df.index):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1, y), xytext=(6, 0), color=line.get_color(), 
                xycoords=ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

ax.set_xlabel('Year')
ax.set_ylabel('Number of Players')
ax.set_title('Number of Players in Different Sports Over the Years')
ax.legend()
ax.grid(True)
ax.set_facecolor('gray')
plt.tight_layout()
plt.savefig('myplot.png')