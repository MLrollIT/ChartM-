from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = StringIO("""
Time,Homemade Bread,Homemade Pasta,Homemade Soup
2000,100,120,80
2010,110,90,70
2020,210,120,60
2030,100,220,90
2040,110,100,70
2050,210,120,75
""")

# Convert the data into a DataFrame
df = pd.read_csv(data)

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data
l1, = ax.plot(df["Time"], df["Homemade Bread"], marker='o', markersize=6, linestyle='-', linewidth=3, color='blue', alpha=0.7, label="Homemade Bread")
l2, = ax.plot(df["Time"], df["Homemade Pasta"], marker='v', markersize=6, linestyle='--', linewidth=3, color='red', alpha=0.7, label="Homemade Pasta")
l3, = ax.plot(df["Time"], df["Homemade Soup"], marker='s', markersize=6, linestyle='-.', linewidth=3, color='green', alpha=0.7, label="Homemade Soup")

# Set labels and title with a larger font size
label_fontsize = 14
title_fontsize = 16
legend_fontsize = 12

ax.set_xlabel('Time', fontsize=label_fontsize)
ax.set_ylabel('Number of Meals', fontsize=label_fontsize)
ax.set_title('Number of Homemade Meals Over Time', fontsize=title_fontsize)

# Add a legend with a larger font size
ax.legend(fontsize=legend_fontsize)

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, ['Homemade Bread', 'Homemade Pasta', 'Homemade Soup']):
    y = line.get_ydata()[-1]
    ax.annotate(name,
                xy=(1,y),
                xytext=(6,0), 
                xycoords = ax.get_yaxis_transform(), 
                textcoords="offset points",
                size=legend_fontsize,  # Change the size here
                color=line.get_color(), 
                weight='bold')

# Annotate data values above the point on the chart figure
for i in range(len(df["Time"])):
    ax.annotate(df["Homemade Bread"][i], (df["Time"][i], df["Homemade Bread"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Homemade Pasta"][i], (df["Time"][i], df["Homemade Pasta"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Homemade Soup"][i], (df["Time"][i], df["Homemade Soup"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Add grid
ax.grid(True)

# Set background color
ax.set_facecolor('lightgray')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")