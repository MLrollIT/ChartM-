from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

csv_data = StringIO("""
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

data = np.genfromtxt(csv_data, delimiter=",", names=True, dtype=None)

years = data['Year']
migrants = data['Number_of_Migrants']

y = np.arange(len(years))

fig, ax = plt.subplots()

bars = ax.barh(y, migrants, color='skyblue', edgecolor='blue')

# Add bar labels
ax.bar_label(bars, padding=3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Number of Migrants')
ax.set_title('Number of Migrants (2000-2008)')
ax.set_yticks(y)
ax.set_yticklabels(years)
ax.grid(True)
ax.set_facecolor('lightgray')

# Invert the y-axis so the years read top-to-bottom
ax.invert_yaxis()

# Add a shadow to the bars that contain the center point of the bounding box
for bar in bars:
    x = bar.get_x() + bar.get_width() / 2
    y = bar.get_y() + bar.get_height() / 2
    ax.annotate("", xy=(x, y), xytext=(x + 3, y + 5), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2"))

plt.tight_layout()
plt.savefig("myplot.png")