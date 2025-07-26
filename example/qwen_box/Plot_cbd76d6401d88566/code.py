from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = StringIO("""
Year,Africa,Asia,Europe
2000,90,75,25
2001,85,72,24
2002,80,65,22
2003,150,60,21
2004,82,68,20
2005,78,110,19
2006,76,105,18
2007,74,100,17
2008,70,95,80
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

x = df["Year"]

linestyles = ['-', '--', '-.', ':']
colors = ['red', 'green', 'blue']

for i in range(1, df.shape[1]):
    line, = ax.plot(x, df.iloc[:, i], marker='o', linestyle=linestyles[i % len(linestyles)], linewidth=2, markersize=6, label=df.columns[i], color=colors[i % len(colors)], alpha=0.7)
    ax.text(x.iloc[-1], df.iloc[-1, i], df.columns[i], ha='center', color=colors[i % len(colors)])

ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title('Population by Continent and Year')
ax.legend(loc='upper left', shadow=True)
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")