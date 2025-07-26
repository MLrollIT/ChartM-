from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data = StringIO("""
Year,AI Research Papers,AI Investments
2005,100,150
2006,150,300
2007,300,500
2008,500,700
2009,700,1300
2010,1300,650
2011,650,800
2012,800,1000
""")

df = pd.read_csv(data)

plt.rc('lines', linewidth=2.5)
fig, ax = plt.subplots()

# Set the background color of the chart figure
ax.set_facecolor('lightgray')

# Plotting data with different line styles, colors, markers, marker sizes, and transparency levels.
line1, = ax.plot(df['Year'], df['AI Research Papers'], linestyle='-', color='red', marker='o', markersize=8, alpha=0.8, label='AI Research Papers')
line2, = ax.plot(df['Year'], df['AI Investments'], linestyle='--', color='blue', marker='v', markersize=8, alpha=0.8, label='AI Investments')

# Setting title, labels and legends
ax.set_title('AI Research Papers and Investments over the years')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.legend()

# Adding grid
ax.grid(True)

# Annotating the lines
for x, y in zip(df['Year'], df['AI Research Papers']):
    ax.text(x, y, 'AI Research Papers', color=line1.get_color(), ha='right')

for x, y in zip(df['Year'], df['AI Investments']):
    ax.text(x, y, 'AI Investments', color=line2.get_color(), ha='right')

# Set the rasterized state of the line that contains the center point of the bounding box to False.
line3 = ax.plot(df['Year'], df['AI Research Papers'], linestyle='-', color='red', marker='o', markersize=8, alpha=0.8, label='AI Research Papers')
line3.set_rasterized(False)

# Stroke the same lines to the Target_object with a linewidth of 4.449089049276784 and a #9f8451 foreground color.
line3.set_linewidth(4.449089049276784)
line3.set_color('#9f8451')

plt.tight_layout()
plt.savefig('myplot.png')