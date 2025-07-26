from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd

# The given data
data = StringIO("""
Year,Tourist Arrivals (millions),Local Economy Revenue (billion dollars)
2015,50,30
2016,75,45
2017,120,70
2018,35,20
2019,80,50
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

# Set the parameters
linewidth = 2
color = ['blue', 'orange']
marker = ['o', 'v']
markersize = 8
alpha = 0.7
linestyle = ['-', ':']

# Plot the lines
for i, column in enumerate(df.columns[1:]):
    ax.plot(df["Year"], df[column], color=color[i], linewidth=linewidth, linestyle=linestyle[i], 
            marker=marker[i], markersize=markersize, alpha=alpha, label=column)
    for j, value in enumerate(df[column]):
        ax.text(j, value, str(value), ha='center', va='bottom')

# Set the title and labels
ax.set_title("Tourist Arrivals and Local Economy Revenue (2015-2019)")
ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.legend()

# Add grid and set the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(4,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')