from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from random import choice

# Data
data = {
    "Social Media Platform": ["Facebook", "Twitter", "Instagram", "LinkedIn", "Snapchat", "Reddit", "WhatsApp"],
    "2016": [2000, 1000, 500, 800, 700, 300, 1500],
    "2017": [1800, 1200, 750, 850, 900, 400, 1600],
    "2018": [1500, 1300, 1000, 900, 1200, 350, 1700],
    "2019": [2000, 1100, 1500, 1200, 1000, 500, 2000],
    "2020": [1900, 1400, 3000, 1100, 1200, 1000, 1800],
    "2021": [1600, 800, 2500, 1000, 1500, 600, 2000]
}
df = pd.DataFrame(data)

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
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
            label=df.loc[i, 'Social Media Platform'])
    
    for j in range(1, len(df.columns)):
        ax.annotate(df.loc[i, df.columns[j]], 
                    (df.columns[j], df.loc[i, df.columns[j]]))

ax.set_title('Social Media Usage Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Users (in millions)')
ax.legend(title='Platform:')
ax.grid(True)
fig.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig('myplot.png')