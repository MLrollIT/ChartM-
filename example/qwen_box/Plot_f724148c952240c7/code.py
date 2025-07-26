from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data
data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Internet': [250, 320, 500, 480, 700],
        'Cloud Storage': [100, 200, 300, 100, 320],
        'Online Shopping': [50, 100, 200, 50, 220],
        'Video Streaming': [30, 60, 90, 30, 110],
        'Social Media': [10, 20, 30, 10, 50]}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Plot the data with different line styles, markers and colors
l1, = ax.plot(df['Year'], df['Internet'], linestyle='-', marker='o', color='blue', markersize=8, alpha=0.7, label='Internet')
l2, = ax.plot(df['Year'], df['Cloud Storage'], linestyle='--', marker='v', color='red', markersize=8, alpha=0.7, label='Cloud Storage')
l3, = ax.plot(df['Year'], df['Online Shopping'], linestyle='-.', marker='s', color='green', markersize=8, alpha=0.7, label='Online Shopping')
l4, = ax.plot(df['Year'], df['Video Streaming'], linestyle=':', marker='^', color='purple', markersize=8, alpha=0.7, label='Video Streaming')
l5, = ax.plot(df['Year'], df['Social Media'], linestyle='-', marker='*', color='orange', markersize=8, alpha=0.7, label='Social Media')

ax.legend(loc='upper left', shadow=True)

# Annotate the data points
for x, y in zip(df['Year'], df['Internet']):
    ax.text(x, y, str(y), color='blue', fontweight='bold')
for x, y in zip(df['Year'], df['Cloud Storage']):
    ax.text(x, y, str(y), color='red', fontweight='bold')
for x, y in zip(df['Year'], df['Online Shopping']):
    ax.text(x, y, str(y), color='green', fontweight='bold')
for x, y in zip(df['Year'], df['Video Streaming']):
    ax.text(x, y, str(y), color='purple', fontweight='bold')
for x, y in zip(df['Year'], df['Social Media']):
    ax.text(x, y, str(y), color='orange', fontweight='bold')

# Set labels, title, and grid
ax.set_xlabel('Year')
ax.set_ylabel('Usage')
ax.set_title('Service Usage Over Time')
ax.grid(True)

# Set the background color
ax.set_facecolor('lightgray')

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("myplot.png")