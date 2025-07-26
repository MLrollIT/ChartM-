from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = StringIO("""Month,Refrigerator,Washing Machine,Dishwasher,Air Conditioner
1,100,80,60,100
2,105,85,65,105
3,110,95,70,50
4,90,100,75,55
5,95,120,80,60
6,140,90,85,65
7,150,70,90,70
8,160,80,95,75
9,100,90,85,70
10,200,180,105,85
11,210,190,110,90
12,190,200,115,95""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

x = np.arange(1, len(df["Month"])+1)

for i in range(1, df.shape[1]):
    line, = ax.plot(x, df.iloc[:, i], marker='o', linestyle='--', linewidth=2, markersize=6, label=df.columns[i])
    ax.text(len(x), df.iloc[-1, i], df.columns[i], ha='right')

ax.set_xlabel('Month')
ax.set_ylabel('Usage')
ax.set_title('Monthly Usage of Home Appliances')
ax.legend(loc='upper right', shadow=True)
ax.set_xticks(x)
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")

# Set the rasterized state of the plot that contains the center point of the bounding box to False.
fig.canvas.draw()
bbox = ax.bbox_to_image(ax.bbox)
bbox.set_rasterized(False)

# Set the snap state of the same line to False.
line.set_snap(False)

plt.savefig("Edit_figure.png")