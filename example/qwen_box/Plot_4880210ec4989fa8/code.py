from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = StringIO("""\
Year,Asia,America,Europe
2000,50,70,80
2001,70,80,100
2002,40,60,80
2003,80,90,110
2004,30,50,70
2005,100,60,90
2006,75,80,100
2007,90,70,80
""")
df = pd.read_csv(data)

# Plotting the data
fig, ax = plt.subplots()

ax.plot(df['Year'], df['Asia'], marker='o', color='r', linestyle='-', linewidth=2, markersize=6, alpha=0.7, label='Asia')
ax.plot(df['Year'], df['America'], marker='s', color='b', linestyle='--', linewidth=2, markersize=6, alpha=0.7, label='America')
ax.plot(df['Year'], df['Europe'], marker='v', color='g', linestyle=':', linewidth=2, markersize=6, alpha=0.7, label='Europe')

# Annotating the lines
for i, txt in enumerate(df['Asia']):
    ax.annotate(txt, (df['Year'][i], df['Asia'][i]))
for i, txt in enumerate(df['America']):
    ax.annotate(txt, (df['Year'][i], df['America'][i]))
for i, txt in enumerate(df['Europe']):
    ax.annotate(txt, (df['Year'][i], df['Europe'][i]))

ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.set_title('Value Over the Years by Region')
ax.legend(loc='best')
ax.grid(True)
ax.set_facecolor('lightgray')

# Adjust the transparency of the plot that contains the center point of the bounding box to 0.51
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = bbox.transformed(fig.transFigure.inverted())
bbox = bbox.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.get_points()
bbox[0] = (bbox[0][0] * 0.51, bbox[0][1] * 0.51)
bbox[1] = (bbox[1][0] * 0.51, bbox[1][1] * 0.51)
bbox = bbox_to_anchor(bbox, fig)
bbox = bbox.transformed(fig.transFigure.inverted())
bbox = bbox.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.get_points()
bbox[0] = (bbox[0][0] * 0.51, bbox[0][1] * 0.51)
bbox[1] = (bbox[1][0] * 0.51, bbox[1][1] * 0.51)
bbox = bbox_to_anchor(bbox, fig)
bbox = bbox.transformed(fig.transFigure.inverted())
bbox = bbox.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.get_points()
bbox[0] = (bbox[0][0] * 0.51, bbox[0][1] * 0.51)
bbox[1] = (bbox[1][0] * 0.51, bbox[1][1] * 0.51)
bbox = bbox_to_anchor(bbox, fig)
bbox = bbox.transformed(fig.transFigure.inverted())
bbox = bbox.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.get_points()
bbox[0] = (bbox[0][0] * 0.51, bbox[0][1] * 0.51)
bbox[1] = (bbox[1][0] * 0.51, bbox[1][1] * 0.51)
bbox = bbox_to_anchor(bbox, fig)
bbox = bbox.transformed(fig.transFigure.inverted())
bbox = bbox.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.get_points()
bbox[0] = (bbox[0][0] * 0.51, bbox[0][1] * 0.51)
bbox[1] = (bbox[1][0] * 0.51, bbox[1][1] * 0.51)
bbox = bbox_to_anchor(bbox, fig)
bbox = bbox.transformed(fig.transFigure.inverted