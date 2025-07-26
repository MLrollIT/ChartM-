from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import io

data = '''Year,Arctic Sea Levels (in meters),Antarctic Sea Levels (in meters),Global Average Sea Levels (in meters)
2000,0.10,0.08,0.09
2001,0.12,0.09,0.10
2002,0.15,0.10,0.12
2003,0.18,0.12,0.14
2004,0.20,0.13,0.15
2005,0.25,0.16,0.18
2006,0.28,0.19,0.21
2007,0.30,0.20,0.23
2008,0.33,0.25,0.27
2009,0.35,0.26,0.29
2010,0.30,0.30,0.31
2011,0.35,0.33,0.34
2012,0.40,0.35,0.36
2013,0.38,0.38,0.39
2014,0.42,0.40,0.41
2015,0.45,0.45,0.45
2016,0.50,0.42,0.46
2017,0.52,0.50,0.51
2018,0.55,0.52,0.53
2019,0.60,0.55,0.57
2020,0.65,0.57,0.60'''

df = pd.read_csv(io.StringIO(data))

fig, ax = plt.subplots(figsize =(10, 7))

data = [df["Arctic Sea Levels (in meters)"], df["Antarctic Sea Levels (in meters)"], df["Global Average Sea Levels (in meters)"]]

bp = ax.boxplot(data, patch_artist = True, notch = True, vert = 0, widths = 0.7)

colors = ['#0000FF', '#00FF00', '#FFFF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_yticklabels(['Arctic', 'Antarctic', 'Global Average'])

ax.set_title('Sea Levels in Meters')
ax.set_xlabel('Sea Levels (in meters)')
ax.set_ylabel('Regions')

# Removed the grid and changed the background color to white
ax.grid(False)
ax.set_facecolor('white')  # Changed from 'lightgray' to 'white'

plt.tight_layout()
plt.savefig('myplot.png')