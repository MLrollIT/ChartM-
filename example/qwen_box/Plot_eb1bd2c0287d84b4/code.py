from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
        '2017': [75, 85, 60, 80],
        '2018': [85, 70, 65, 75],
        '2019': [70, 90, 60, 85]}
df = pd.DataFrame(data)

# Plot
plt.rc('lines', linewidth=2.5)
fig, ax = plt.subplots()
ax.set_facecolor('lightgray')  # Set background color
ax.grid(True)  # Add grid lines

# Line styles
linestyles = ['-', '--', '-.', ':']

# Plot each city's data
for i, city in enumerate(df['City']):
    ax.plot(df.columns[1:], df.loc[i, df.columns[1:]], linestyle=linestyles[i % len(linestyles)],
            marker='o', markersize=5, label=city, alpha=0.7)

# Annotate each line
for i, line in enumerate(ax.get_lines()):
    y = line.get_ydata()[-1]
    ax.annotate(df['City'][i], (2, y), textcoords="offset points", xytext=(5,0), ha='left')

# Labels, title, legend
ax.set_xlabel('Year')
ax.set_ylabel('Value')
ax.set_title('City Data over the Years')
ax.legend()

plt.tight_layout()
plt.savefig('myplot.png')