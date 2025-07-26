from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# The given data
data = StringIO("""
Type of Vacation,2005,2006,2007,2008,2009
Beach Vacation,5000,5250,4800,4600,6600
Cruise,2000,2300,2600,2400,2300
Safari,1000,1100,1500,1400,1100
Ski Trip,3000,2800,2600,2700,2400
Camping,4000,4200,3800,3600,5200
""")

df = pd.read_csv(data, index_col='Type of Vacation')

fig, ax = plt.subplots()

# Set the parameters
linewidth = 1.5
color = ['red', 'blue', 'green', 'purple', 'orange']
marker = ['o', 'v', '^', '<', '>']
markersize = 5
alpha = 0.7
linestyle = ['-', '--', '-.', ':', '-']

# Plot the lines
for i, (index, row) in enumerate(df.iterrows()):
    ax.plot(row.index, row.values, color=color[i], linewidth=linewidth, linestyle=linestyle[i], 
            marker=marker[i], markersize=markersize, alpha=alpha, label=index)
    for j, value in enumerate(row.values):
        ax.text(j, value, str(value), ha='center', va='bottom')

# Set the title and labels
ax.set_title("Popularity of Different Types of Vacation from 2005 to 2009")
ax.set_xlabel("Year")
ax.set_ylabel("Number of People")
ax.legend()

# Add grid and set the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, df.index):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(4,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Set the animated state of the plot that contains the center point of the bounding box to True
ax.figure.canvas.draw()
bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.get_points()
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox = bbox / fig.dpi
bbox = bbox[0] + bbox[1] / 2
bbox =