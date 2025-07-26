from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Year": [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    "Sparrow": [2000, 2100, 2150, 7000, 2200, 2250, 2300, 2350, 2400],
    "Hummingbird": [1000, 3500, 3700, 4000, 4100, 8000, 4200, 4300, 4400],
    "Eagle": [500, 450, 400, 350, 300, 250, 200, 150, 100]
}
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots()

for column in df.columns[1:]:
    ax.plot(df['Year'], df[column], marker='o', linestyle=':', linewidth=2.0, label=column, alpha=0.7)
    for x, y in zip(df['Year'], df[column]):
        ax.text(x, y, str(y))

# Annotations
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

ax.set_xlabel('Year')
ax.set_ylabel('Bird Population')
ax.set_title('Bird Population Over the Years')
ax.legend()
ax.grid(True)
ax.set_facecolor('gray')
plt.tight_layout()

# Set the clipping state of the plot that contains the center point of the bounding box to True
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox.set_clip_on(True)

# Adjust the linewidth of that plot to 1.20 for the same lines
for line in ax.lines:
    line.set_linewidth(1.20)

plt.savefig('Edit_figure.png')