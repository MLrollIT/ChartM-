from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Define the data
data = '''\
Year,Sparrow,Eagle,Swan
2010,1500,2000,1800
2011,1700,2100,2200
2012,1650,3500,2200
2013,1800,2100,4000
2014,1900,2000,1800
2015,1550,2200,2100
2016,1750,4000,2200
2017,1600,2150,1800
'''

# Read the data into a DataFrame
df = pd.read_csv(StringIO(data))

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data with updated colors
l1, = ax.plot(df["Year"], df["Sparrow"], marker='o', markersize=10.76, linestyle='-', linewidth=2, color='purple', alpha=0.7, label="Sparrow")  # Changed color to 'purple'
l2, = ax.plot(df["Year"], df["Eagle"], marker='v', markersize=10.76, linestyle='--', linewidth=2, color='orange', alpha=0.7, label="Eagle")  # Changed color to 'orange'
l3, = ax.plot(df["Year"], df["Swan"], marker='s', markersize=10.76, linestyle='-.', linewidth=2, color='cyan', alpha=0.7, label="Swan")  # Changed color to 'cyan'

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Birds')
ax.set_title('Number of Birds over the Years')

# Add a legend
ax.legend()

# Annotate each line with the corresponding legend label
for line, name in zip(ax.lines, ['Sparrow', 'Eagle', 'Swan']):
    y = line.get_ydata()[-1]
    ax.annotate(name,
                xy=(1,y),
                xytext=(6,0), 
                xycoords = ax.get_yaxis_transform(), 
                textcoords="offset points",
                size="large", 
                color=line.get_color(),  # The color will automatically match the line color
                weight='bold')

# Annotate data values above the point on the chart figure
for i in range(len(df["Year"])):
    ax.annotate(df["Sparrow"][i], (df["Year"][i], df["Sparrow"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Eagle"][i], (df["Year"][i], df["Eagle"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Swan"][i], (df["Year"][i], df["Swan"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Add grid
ax.grid(True)

# Set background color to white
ax.set_facecolor('white')  # Changed background color to 'white'

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")