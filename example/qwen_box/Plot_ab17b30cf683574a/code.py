from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
"Software","Q1","Q2","Q3","Q4"
"Antivirus",100,75,325,90
"CRM",150,300,280,315
"ERP",200,175,205,225
"Graphic Design",250,550,250,255
""")

# Load data into a DataFrame
df = pd.read_csv(data, quotechar='"')

# Create a figure and an axes
fig, ax = plt.subplots()

# Set the background color of the chart
ax.set_facecolor('lightgray')

# Plot data
for index, row in df.iterrows():
    ax.plot(['Q1', 'Q2', 'Q3', 'Q4'], row[1:], label=row[0], linestyle='-', linewidth=1.5, marker='o', markersize=4, alpha=0.7)

# Set labels and title
ax.set(xlabel='Quarters', ylabel='Sales',
       title='Software Sales Over Quarters')

# Add legend and grid
ax.legend()
ax.grid()

# Annotate each line with the corresponding legend label
for line, name in zip(ax.lines, df['Software']):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Set the transform of the line that contains the center point of the bounding box to the Coordinate system of data.
bbox = ax.bbox_to_transform(ax.bbox.get_points()[0])
line = ax.lines[2]
line.set_transform(bbox)
line.set_zorder(8)
line.set_shadecolor('none')
line.set_alpha(1)

# Set the shadow effect of the same line with a offset of (3.76,2.87)
shadow = ax.annotate("", xy=(1, 0), xytext=(1, 0), xycoords='data', textcoords='data',
                      arrowprops=dict(arrowstyle="->", connectionstyle="arc3", lw=2, color=line.get_color()))
shadow.set_visible(False)
shadow.set_transform(bbox)
shadow.set_zorder(line.get_zorder()+1)
shadow.set_offset((3.76,2.87))

# Tight layout and save figure
plt.tight_layout()
fig.savefig("myplot.png")