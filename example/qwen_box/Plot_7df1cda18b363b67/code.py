from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = StringIO("""
Year,Number of Migrants
2000,1000000
2001,950000
2002,920000
2003,1500000
2004,1300000
2005,1800000
2006,1100000
2007,1200000
2008,900000
""")

df = pd.read_csv(data)

fig, ax = plt.subplots()

l1, = ax.plot(df["Year"], df["Number of Migrants"], linestyle='--', linewidth=2, color='blue', marker='o', markersize=10, alpha=0.7)

ax.legend([l1], ['Number of Migrants'], loc='upper right', shadow=True)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Migrants')
ax.set_title('Number of Migrants over Years')

# Change the color of the grid to red
ax.grid(True, color='red')

ax.set_facecolor('lightgray')

# annotate each line
for x, y in zip(df["Year"], df["Number of Migrants"]):
    ax.text(x, y, 'Number of Migrants')

# Change the clipping state of the plot that contains the center point of the bounding box to False
ax.set_clip_on(False)

plt.tight_layout()
plt.savefig("myplot.png")