from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = """Year,Depression,Anxiety,Substance Abuse
2000,75,90,60
2001,70,95,55
2002,65,100,50
2003,60,105,70
2004,55,110,40
2005,70,115,50
2006,65,120,80
2007,60,125,35
2008,80,130,60"""

# Convert the data into a DataFrame
df = pd.read_csv(StringIO(data))

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data
l1, = ax.plot(df["Year"], df["Depression"], marker='o', markersize=6, linestyle='-', linewidth=2, color='blue', alpha=0.7, label="Depression")
l2, = ax.plot(df["Year"], df["Anxiety"], marker='v', markersize=11.80, linestyle='--', linewidth=2, color='red', alpha=0.7, label="Anxiety")
l3, = ax.plot(df["Year"], df["Substance Abuse"], marker='s', markersize=6, linestyle='-.', linewidth=2, color='green', alpha=0.7, label="Substance Abuse")

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Cases')
ax.set_title('Number of Cases of Different Mental Health Issues Over the Years')

# Add a legend
ax.legend()

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, ['Depression', 'Anxiety', 'Substance Abuse']):
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
for i in range(len(df["Year"])):
    ax.annotate(df["Depression"][i], (df["Year"][i], df["Depression"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Anxiety"][i], (df["Year"][i], df["Anxiety"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Substance Abuse"][i], (df["Year"][i], df["Substance Abuse"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Add grid
ax.grid(True)

# Set background color
ax.set_facecolor('lightgray')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")