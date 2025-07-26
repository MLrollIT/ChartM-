from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = StringIO("""
Year,Arctic Ice Cap,Antarctic Ice Cap
2000,13.2,28.8
2001,13.5,29.1
2002,13.8,29.5
2003,14.1,30.0
2004,14.4,30.6
2005,14.6,31.3
2006,12.0,32.1
2007,12.2,33.0
2008,12.5,33.9
2009,12.8,34.9
2010,13.0,35.9
2011,15.0,36.0
2012,14.8,35.8
2013,14.6,35.6
2014,14.4,35.5
2015,14.2,35.4
2016,12.0,35.3
2017,11.8,35.2
2018,11.6,35.1
2019,11.4,35.0
2020,10.0,40.0
""")

df = pd.read_csv(data)
x = np.arange(len(df['Year']))  # the label locations
width = 0.3  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 8))

rects1 = ax.bar(x - width/2, df['Arctic Ice Cap'], width, color='blue', edgecolor='black', label='Arctic Ice Cap')
rects2 = ax.bar(x + width/2, df['Antarctic Ice Cap'], width, color='orange', edgecolor='black', label='Antarctic Ice Cap')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Ice Cap Size (Million Square km)')
ax.set_title('Ice Cap Sizes from 2000 to 2020')
ax.set_xticks(x)
ax.set_xticklabels(df['Year'], rotation=45)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Setting background color and grid
ax.set_facecolor('gray')
ax.grid(True)

# Add a shadow to the bars that share the same legend as the ones containing the center point of the bounding box
bbox = ax.bbox
bbox2 = ax.bbox
bbox2.x0 += 5
bbox2.width -= 10
bbox2.y0 += 3
bbox2.height -= 6
ax.add_patch(plt.Rectangle((bbox2.x0, bbox2.y0), bbox2.width, bbox2.height, facecolor='none', edgecolor='black', linewidth=1))

plt.tight_layout()
plt.savefig("myplot.png")