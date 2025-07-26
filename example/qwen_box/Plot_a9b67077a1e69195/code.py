from io import StringIO
import numpy as np

from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = StringIO("""
Year,Smartphone Usage
2016,60
2017,65
2018,130
2019,70
2020,80
2021,40
2022,90
2023,45
2024,75
2025,105
2026,50
2027,35
2028,65
2029,75
""")

# Convert the data into a DataFrame
df = pd.read_csv(data)

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data
l1, = ax.plot(df["Year"], df["Smartphone Usage"], marker='o', markersize=6, linestyle='-', linewidth=2, color='blue', alpha=0.7, label="Smartphone Usage")

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Smartphone Usage')
ax.set_title('Smartphone Usage Over the Years')

# Add a legend
ax.legend()

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, ['Smartphone Usage']):
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
    ax.annotate(df["Smartphone Usage"][i], (df["Year"][i], df["Smartphone Usage"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Add grid
ax.grid(True)

# Set background color
ax.set_facecolor('lightgray')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")