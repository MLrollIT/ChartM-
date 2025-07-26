from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {
    "Sport": ["Football", "Baseball", "Basketball", "Swimming", "Running", "Golf"],
    "2008": [90, 80, 70, 50, 30, 40],
    "2012": [68, 60, 90, 75, 60, 30],
    "2016": [85, 70, 65, 60, 40, 60]
}

df = pd.DataFrame(data)

styles = ['-', '--', '-.', ':']
colors = ['red', 'green', 'blue', 'purple', 'orange', 'black']
markers = ['.', 'o', 'v', '^', 's', '*']

plt.rc('lines', linewidth=2.5)
fig, ax = plt.subplots()

for i in range(len(df)):
    ax.plot(df.columns[1:], df.iloc[i, 1:], linestyle=styles[i % len(styles)], color=colors[i % len(colors)], 
            marker=markers[i % len(markers)], markersize=10, alpha=0.7, label=df.iloc[i,0])
    ax.text(2, df.iloc[i, -1], df.iloc[i, 0])

ax.set_title('Sports Popularity Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Popularity')
ax.legend(loc='upper right', title="Sports")
ax.grid(True)
ax.set_facecolor('lightgray')

# Change the style of the line that contains the center point of the bounding box to 'solid'
ax.plot(df.columns[1:], df.iloc[1, 1:], linestyle='solid', color='red', marker='o', markersize=10, alpha=0.7, label=df.iloc[1,0])

plt.tight_layout()
plt.savefig("myplot.png")