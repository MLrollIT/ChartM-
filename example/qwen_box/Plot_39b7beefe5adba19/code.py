from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
from random import choice

# Data
data = StringIO("""
Region,2016,2017,2018
North America,100,80,110
Europe,90,130,120
Asia,85,70,140
Africa,70,75,70
South America,60,90,85
Australia,80,85,80
Middle East,65,60,90
Antarctica,50,51,55
""")
df = pd.read_csv(data)

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple']
markers = ['.', 'o', 'v', '^', 's', 'p', '*', 'h']

# Plot
fig, ax = plt.subplots()
for i in range(len(df)):
    ax.plot(df.columns[1:], df.loc[i, df.columns[1:]], 
            linestyle=choice(linestyles), 
            color=colors[i], 
            marker=markers[i], 
            markersize=10, 
            alpha=0.7, 
            label=df.loc[i, 'Region'])
    
    for j in range(1, len(df.columns)):
        ax.annotate(df.loc[i, df.columns[j]], 
                    (df.columns[j], df.loc[i, df.columns[j]]))

ax.set_title('Region Population Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.legend(title='Region:')
ax.grid(True)
fig.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig('myplot.png')