from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Data in CSV format
data = StringIO("""
Platforms,Facebook,Instagram,Snapchat
2015,155,120,100
2016,140,130,150
2017,125,160,200
2018,110,175,250
2019,95,190,300
2020,180,205,350
2021,165,190,330
2022,150,175,310
""")

# Read data using pandas
df = pd.read_csv(data)

# Prepare figure and axes
fig, ax = plt.subplots()
ax.grid(True)
ax.set_facecolor('lightgray')

# Line styles
line_styles = ['-', '--', '-.', ':']

# Plot data
for i, column in enumerate(df.columns[1:]):
    ax.plot(df['Platforms'], df[column], label=column, linestyle=line_styles[i], linewidth=2, marker='o', markersize=5, alpha=0.7)
    
# Set labels, title and legend
ax.set_xlabel('Year')
ax.set_ylabel('User Count (in millions)')
ax.set_title('Social Media Platform Usage Over the Years')
ax.legend()

# Annotations
for i, column in enumerate(df.columns[1:]):
    ax.annotate(column, (df['Platforms'].iloc[-1], df[column].iloc[-1]))

# Set animated state of lines
for line in ax.lines:
    line.set_animated(False)

# Set rasterized state of lines
for line in ax.lines:
    line.set_rasterized(True)

plt.tight_layout()
plt.savefig('myplot.png')