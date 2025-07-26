from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

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

# Create a color map
norm = Normalize(vmin=min(migrants), vmax=max(migrants))
cmap = plt.get_cmap('Greens')
colors = cmap(norm(migrants))

bars = ax.barh(y, migrants, color=colors, edgecolor='green')

# Add bar labels
ax.bar_label(bars, padding=3)

# Create a ScalarMappable and initialize a data structure
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

# Optional: Create a colorbar
cbar = plt.colorbar(sm)
cbar.set_label('Number of Migrants')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Number of Migrants')
ax.set_title('Number of Migrants (2000-2008)')
ax.set_yticks(y)
ax.set_yticklabels(years)
ax.grid(True)
ax.set_facecolor('lightgray')

# Invert the y-axis so the years read top-to-bottom
ax.invert_yaxis()

# Set the clipping box for the bars that contain the center point of the bounding box
bbox = plt.Bbox([[2, 252], [277, 245]])
for bar in bars:
    bar.set_clip_box(bbox)

# Enable the picker state for the bars related to the Target_object at the same coordinates
for bar in bars:
    bar.set_picker(True)

plt.tight_layout()
plt.savefig("myplot.png")