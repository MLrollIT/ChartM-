from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create data
data = {
    "Sport": ["Football", "Baseball", "Basketball", "Soccer"],
    "Popularity": [100, 80, 95, 90]
}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Create bars
bars = ax.bar(df['Sport'], df['Popularity'], color='skyblue', edgecolor='blue')

# Set title, x-label, y-label
ax.set_title('Sports Popularity')
ax.set_xlabel('Sport')
ax.set_ylabel('Popularity')

# Add grid and set facecolor
ax.grid(True)
ax.set_facecolor('gray')

# Add labels to each bar
ax.bar_label(bars)

# Change the line color of the bars that contain the center point of the bounding box to #69f39e.
for bar in bars:
    if bar.get_x() + bar.get_width() / 2 == 70:
        bar.set_edgecolor('#69f39e')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")