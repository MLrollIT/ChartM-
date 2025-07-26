from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
from random import choice

# Data
data = StringIO("""
Plant Species,Spring,Summer,Autumn,Winter
Rose,50,75,30,15
Sunflower,80,100,20,5
Maple,30,50,70,40
Cactus,10,30,10,20
""")
df = pd.read_csv(data)

# Variables for variety
linestyles = ['-', '--', '-.', ':']
colors = ['b', 'g', 'r', 'c', 'm']
markers = ['.', 'o', 'v', '^', 's']

# Plot
fig, ax = plt.subplots()
for i in range(len(df)):
    ax.plot(df.columns[1:], df.loc[i, df.columns[1:]], 
            linestyle=choice(linestyles), 
            color=colors[i % len(colors)], 
            marker=markers[i % len(markers)], 
            markersize=10, 
            alpha=0.7, 
            label=df.loc[i, 'Plant Species'])

    for j in range(1, len(df.columns)):
        ax.annotate(df.loc[i, df.columns[j]], 
                    (df.columns[j], df.loc[i, df.columns[j]]))

ax.set_title('Plant Growth Over Seasons')
ax.set_xlabel('Season')
ax.set_ylabel('Growth')
ax.legend(title='Plant Species:')
ax.grid(True)
fig.set_facecolor('lightgrey')

# Set the clip box for the portion at the center point of the bounding box
bbox = plt.Bbox([[20, 240], [20 + 787, 240 + 159]])
ax.set_clip_box(bbox)
ax.set_snap(True)

plt.tight_layout()
plt.savefig('myplot.png')