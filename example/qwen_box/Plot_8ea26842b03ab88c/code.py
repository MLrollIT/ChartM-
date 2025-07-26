from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'Year': [2017, 2018, 2019, 2020],
        'Bird Species 1': [1000, 950, 900, 1200],
        'Bird Species 2': [900, 1050, 1200, 1100],
        'Bird Species 3': [800, 850, 750, 600]}
df = pd.DataFrame(data)

plt.rc('lines', linewidth=2.5)
fig, ax = plt.subplots()

# Plot data
line1, = ax.plot(df['Year'], df['Bird Species 1'], linestyle='-', color='red', marker='o', markersize=10, alpha=0.5, label='Bird Species 1')
line2, = ax.plot(df['Year'], df['Bird Species 2'], linestyle='--', color='green', marker='v', markersize=10, alpha=0.5, label='Bird Species 2')
line3, = ax.plot(df['Year'], df['Bird Species 3'], linestyle='-.', color='blue', marker='s', markersize=10, alpha=0.5, label='Bird Species 3')

# Set title and labels
ax.set_title('Bird Species Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Count')

# Set legend
ax.legend(loc='best')

# Set grid and background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Save figure
plt.tight_layout()
plt.savefig('myplot.png')