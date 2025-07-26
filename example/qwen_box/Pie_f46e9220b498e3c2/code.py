from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# given data
fields = ["Hardware Development", "Software Development", "User Experience Design", "Market Adoption"]
percentage = [25, 35, 30, 10]

# create figure and axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# create pie chart
wedges, texts, autotexts = ax.pie(percentage, labels=fields, autopct='%1.1f%%', startangle=-40, 
                                   explode=(0.1, 0, 0, 0), labeldistance=1.15, shadow=True, 
                                   pctdistance=0.8, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

# change background color
fig.patch.set_facecolor('gray')

# setting title
ax.set_title("Percentage of Different Fields")

# saving the figure
plt.tight_layout()
plt.savefig("myplot.png")

# modify the object in the chart
for wedge in wedges:
    wedge.set_clip_on(False)
    wedge.set_edgecolor('none')
    wedge.set_facecolor('none')
    wedge.set_zorder(10)
    wedge.set_boxstyle('square,pad=0.1,rounding_size=0.1')
    wedge.set_transform(wedge.get_transform().rotate_deg(40))
    wedge.set_clip_box(ax.bbox)
    wedge.set_clip_on(True)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge.set_clip_path(ax.bbox, transform=ax.transAxes)
    wedge