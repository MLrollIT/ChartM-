from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# The given data
data = StringIO("""Genetic Engineering Development,Year 2016,Year 2018,Year 2020
CRISPR,100,150,130
Gene Therapy,80,70,100
Genetic Modification,120,140,90
Genome Mapping,90,85,75
Cloning,50,45,65
Synthetic Biology,70,65,85
Bioinformatics,60,55,80
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

# Set the parameters
linewidth = 2.0
color = ['red', 'blue', 'green']
marker = ['o', 'v', '^']
markersize = 8
alpha = 0.9
linestyle = ['-', '--', '-.']

# Plot the lines
for i, column in enumerate(df.columns[1:]):
    ax.plot(df["Genetic Engineering Development"], df[column], color=color[i], linewidth=linewidth, linestyle=linestyle[i], 
            marker=marker[i], markersize=markersize, alpha=alpha, label=column)
    for j, value in enumerate(df[column]):
        ax.text(j, value, str(value), ha='center', va='bottom')

# Set the title and labels
ax.set_title("Genetic Engineering Development over Years")
ax.set_xlabel("Technologies")
ax.set_ylabel("Development Level")
ax.legend()

# Add grid and set the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')