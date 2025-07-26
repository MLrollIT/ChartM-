from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Given data in csv format
data = """
Year,Manned Missions,Unmanned Missions,Private Missions
1960,5,10,0
1970,20,30,0
1980,15,35,0
1990,10,40,1
2000,5,45,3
2010,2,50,10
2020,1,55,25
"""

# Convert the data into DataFrame
df = pd.read_csv(StringIO(data))

# Create a figure and axis
fig, ax = plt.subplots()

# Scatter plot for each column
for column in df.columns[1:]:
    ax.scatter(df['Year'], df[column], label=column, alpha=0.5)

# Set title and labels for axes
ax.set_xlabel("Year")
ax.set_ylabel("Number of Missions")
ax.set_title("Number of Missions Over Years")

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(), 
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Annotate data values above the point on the chart figure
for i in range(len(df.columns[1:])):
    for x,y in zip(df['Year'],df[df.columns[i+1]]):
        label = "{:.2f}".format(y)
        plt.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center') 

# Add grids on the background
ax.grid(True)

# Set the background color of the chart figure to light gray
ax.set_facecolor('lightgray')

# Add legend
ax.legend()

# Adjust layout
plt.tight_layout()

# Save the final figure
plt.savefig("myplot.png")