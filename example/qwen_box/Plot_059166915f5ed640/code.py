from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import io

# Data for plotting
data = """
"Year","Arctic Sea Levels (in meters)","Antarctic Sea Levels (in meters)","Global Average Sea Levels (in meters)"
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
2020,0.65,0.57,0.60
"""
df = pd.read_csv(io.StringIO(data), quotechar='"')

fig, ax = plt.subplots()
ax.plot(df["Year"], df["Arctic Sea Levels (in meters)"], label='Arctic', linestyle='-', color='red', marker='o', markersize=5, linewidth=2, alpha=1)
ax.plot(df["Year"], df["Antarctic Sea Levels (in meters)"], label='Antarctic', linestyle='--', color='blue', marker='v', markersize=5, linewidth=2, alpha=1)
ax.plot(df["Year"], df["Global Average Sea Levels (in meters)"], label='Global Average', linestyle='-.', color='green', marker='s', markersize=5, linewidth=2, alpha=1)

# Change font sizes here
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Sea Level (in meters)', fontsize=14)
ax.set_title('Sea Level Changes from 2000 to 2020', fontsize=18)
ax.legend(loc='upper left', fontsize=12)
ax.grid(True)
ax.set_facecolor('lightgray')

for line, name in zip(ax.lines, ['Arctic', 'Antarctic', 'Global Average']):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Set the visibility of the plot that contains the center point of the bounding box to False
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox.set_visible(False)

plt.tight_layout()
fig.savefig("myplot.png")