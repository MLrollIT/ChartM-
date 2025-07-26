from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = """
Year,Organic Vegetables,Organic Fruits,Organic Grains
2012,100,110,95
2013,95,105,90
2014,80,115,85
2015,85,130,70
2016,70,135,65
2017,75,145,60
2018,110,155,55
2019,115,165,50
"""
# Read data into pandas dataframe
df = pd.read_csv(StringIO(data))

# Create a plot figure
fig, ax = plt.subplots()

# Define colors for each series
colors = {'Organic Vegetables': 'green', 'Organic Fruits': 'red', 'Organic Grains': 'purple'}

# Plot each column in dataframe with a unique color and solid line
for column in df.columns[1:]:
    ax.plot(df['Year'], df[column], marker='o', linestyle='-', color=colors[column], linewidth=2, markersize=5, alpha=0.7, label=column)

# Annotate each line with corresponding legend label
for line, name in zip(ax.lines, df.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(),
                xycoords = ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

# Add details to the plot
ax.set_xlabel('Year')
ax.set_ylabel('Quantity')
ax.set_title('Organic Food Trends Over the Years')
ax.legend()
ax.grid(True)
ax.set_facecolor('lightgray')

# Save the plot as a PNG file
plt.tight_layout()
plt.savefig('myplot.png')