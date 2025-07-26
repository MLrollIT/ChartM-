from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Define the data
data = '''\
Household,Water_Consumption
Household1,100
Household2,120
Household3,50
Household4,140
Household5,130
Household6,180
Household7,70
Household8,200
'''

# Convert the data into a DataFrame
df = pd.read_csv(StringIO(data))

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data
l1, = ax.plot(df["Household"], df["Water_Consumption"], marker='o', markersize=6, linestyle='-', linewidth=2, color='blue', alpha=0.7, label="Water Consumption")

# Set labels and title
ax.set_xlabel('Household')
ax.set_ylabel('Water Consumption')
ax.set_title('Water Consumption of Different Households')

# Add a legend
ax.legend()

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, ['Water Consumption']):
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
for i in range(len(df["Household"])):
    ax.annotate(df["Water_Consumption"][i], (df["Household"][i], df["Water_Consumption"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Add grid
ax.grid(True)

# Set background color
ax.set_facecolor('lightgray')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")