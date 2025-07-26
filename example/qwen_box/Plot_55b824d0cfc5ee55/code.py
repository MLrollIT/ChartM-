from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from random import choice

# Data
data = {
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    "Pop": [100, 85, 90, 70, 90, 80, 70, 85, 100, 95, 70],
    "Rock": [150, 130, 120, 140, 110, 150, 130, 120, 150, 130, 110],
    "Country": [50, 55, 60, 70, 60, 55, 65, 70, 75, 80, 85],
    "Hip Hop": [70, 80, 75, 85, 95, 90, 110, 100, 95, 105, 120]
}
df = pd.DataFrame(data)

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['blue', 'green', 'red', 'cyan', 'magenta']
markers = ['.', 'o', 'v', '^', 's']

# Plot
fig, ax = plt.subplots()
for i in range(1, len(df.columns)):
    ax.plot(df['Year'], df[df.columns[i]], 
            linestyle=choice(linestyles), 
            color=colors[i-1], 
            marker=markers[i-1], 
            markersize=10, 
            alpha=0.7, 
            label=df.columns[i])
    
    ax.annotate(df.columns[i], 
                (df['Year'].iloc[-1], df[df.columns[i]].iloc[-1]))
    
# Set custom font sizes here
title_fontsize = 16
label_fontsize = 16
legend_fontsize = 12

ax.set_title('Music Genre Popularity Over Years', fontsize=title_fontsize)
ax.set_xlabel('Year', fontsize=label_fontsize)
ax.set_ylabel('Popularity', fontsize=label_fontsize)
legend = ax.legend(title='Genre:', fontsize=legend_fontsize)  # Set the legend title font size
ax.grid(True)
fig.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig('myplot.png')