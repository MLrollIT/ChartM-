from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data
data = {"Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008],
        "Arctic Ice Extent (million sq km)": [13.5, 13.2, 13.0, 12.8, 12.3, 11.9, 11.6, 12.0, 11.5],
        "Antarctic Ice Extent (million sq km)": [18.6, 18.2, 18.9, 18.0, 18.8, 17.9, 18.3, 17.5, 17.0]}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Plot the data with different line styles, markers and colors
l1, = ax.plot(df['Year'], df['Arctic Ice Extent (million sq km)'], linestyle='-', marker='o', color='blue', markersize=9.63, alpha=0.7, label='Arctic Ice Extent')
l2, = ax.plot(df['Year'], df['Antarctic Ice Extent (million sq km)'], linestyle='--', marker='v', color='red', markersize=9.63, alpha=0.7, label='Antarctic Ice Extent')

ax.legend(loc='upper left', shadow=True)

# Annotate the data points
for x, y in zip(df['Year'], df['Arctic Ice Extent (million sq km)']):
    ax.text(x, y, str(y), color='blue', fontweight='bold')
for x, y in zip(df['Year'], df['Antarctic Ice Extent (million sq km)']):
    ax.text(x, y, str(y), color='red', fontweight='bold')

# Set labels, title, and grid
ax.set_xlabel('Year')
ax.set_ylabel('Ice Extent (million sq km)')
ax.set_title('Arctic and Antarctic Ice Extents Over Time')
ax.grid(True)

# Set the background color
ax.set_facecolor('lightgray')

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("myplot.png")