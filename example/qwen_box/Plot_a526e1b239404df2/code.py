from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# The given data
data = StringIO("""
Year,Arctic Ice Cap,Antarctic Ice Cap,Greenland Ice Cap
2000,13.2,13.6,2.9
2001,13.5,13.9,3.2
2002,13.7,13.5,3.0
2003,10.2,13.0,2.7
2004,10.5,13.5,3.0
2005,10.9,14.0,3.3
2006,10.7,13.6,3.1
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

# Set the parameters
linewidth = 2.0
color = ['skyblue', 'teal', 'navy']
marker = ['o', 'v', '^']
markersize = 7
alpha = 0.8
linestyle = ['-', '--', '-.']

# Plot the lines
for i, column in enumerate(df.columns[1:]):
    ax.plot(df["Year"], df[column], color=color[i], linewidth=linewidth, linestyle=linestyle[i], 
            marker=marker[i], markersize=markersize, alpha=alpha, label=column)
    y = df[column].values[-1]
    ax.annotate(column, xy=(1,y), xytext=(6,0), color=color[i], 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Set the title and labels
ax.set_title("Changes in Ice Cap Sizes from 2000 to 2006")
ax.set_xlabel("Year")
ax.set_ylabel("Size (in million square kilometers)")
ax.legend()

# Add grid and set the background color
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')