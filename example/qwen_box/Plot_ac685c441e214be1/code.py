from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Define the data
data = """
City,2017,2018,2019
San Francisco,850,1200,950
New York,700,800,1600
Berlin,400,1200,800
"""
# Convert the data into a DataFrame
df = pd.read_csv(StringIO(data))

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data
l1, = ax.plot(df.columns[1:], df.iloc[0,1:], marker='o', markersize=6, linestyle='-', linewidth=2, color='blue', alpha=0.7, label=df.iloc[0,0])
l2, = ax.plot(df.columns[1:], df.iloc[1,1:], marker='v', markersize=6, linestyle='--', linewidth=2, color='red', alpha=0.7, label=df.iloc[1,0])
l3, = ax.plot(df.columns[1:], df.iloc[2,1:], marker='s', markersize=6, linestyle='-.', linewidth=2, color='green', alpha=0.7, label=df.iloc[2,0])

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title('Population Trend of Cities Over the Years')

# Add a legend
ax.legend()

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, df["City"]):
    y = line.get_ydata()[-1]
    ax.annotate(name,
                xy=(1,y),
                xytext=(6,0), 
                xycoords = ax.get_yaxis_transform(), 
                textcoords="offset points",
                size="large", 
                color=line.get_color(), 
                weight='bold')
                
# Annotate data values above the point on the chart figure
for i in range(len(df.columns[1:])):
    ax.annotate(df.iloc[0,i+1], (df.columns[i+1], df.iloc[0,i+1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df.iloc[1,i+1], (df.columns[i+1], df.iloc[1,i+1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df.iloc[2,i+1], (df.columns[i+1], df.iloc[2,i+1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Add grid
ax.grid(True)

# Set background color
ax.set_facecolor('lightgray')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")