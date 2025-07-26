from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given data
data = {
    "Platform": ["Facebook", "Instagram", "Twitter", "Snapchat", "LinkedIn", "Pinterest", "Reddit", "WeChat", "WhatsApp"],
    "2016": [100, 80, 90, 70, 60, 50, 30, 20, 10],
    "2017": [120, 110, 70, 100, 80, 75, 60, 40, 5],
    "2018": [85, 130, 95, 70, 85, 55, 65, 45, 30]
}

df = pd.DataFrame(data)

# Size of the figure
fig, ax = plt.subplots(figsize=(10, 8))

# Number of bars
N = len(df["Platform"])

# Position of bars on x-axis
ind = np.arange(N)

# Width of a bar 
width = 0.25       

# Plotting
ax.bar(ind, df["2016"], width, label='2016', color = 'b', edgecolor = 'gray')
ax.bar(ind + width, df["2017"], width, label='2017', color = 'r', edgecolor = 'gray')
ax.bar(ind + width + width, df["2018"], width, label='2018', color = 'g', edgecolor = 'gray')

ax.set_xlabel('Platform')
ax.set_ylabel('Usage')
ax.set_title('Usage of Social Media Platforms from 2016 to 2018')

# Adding xticks  
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(df["Platform"])

ax.legend(loc='best')
ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")

# Get the bounding box of the center point of the bounding box
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)

# Get the bar with the center point of the bounding box
bar = ax.bar(ind + width / 2, df["2018"][4], width, label='2018', color = 'g', edgecolor = 'gray')

# Set the transparency of the bars that share the same legend with the bar that contains the center point of the bounding box to 0.17, and also update their linewidth to 0.93
for bar in ax.containers[4]:
    bar.set_alpha(0.17)
    bar.set_edgecolor('gray')
    bar.set_linewidth(0.93)

plt.savefig("Edit_figure.png")