from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    "Year": ["2000", "2005", "2010", "2015", "2020"],
    "Beef": [50, 55, 52, 54, 60],
    "Poultry": [30, 35, 37, 40, 80],
    "Pork": [70, 75, 80, 78, 79],
    "Fish": [40, 50, 60, 45, 48],
    "Lamb": [10, 12, 14, 16, 30]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data
l1, = ax.plot(df["Year"], df["Beef"], marker='o', markersize=6, linestyle='-', linewidth=2, color='blue', alpha=0.7, label="Beef")
l2, = ax.plot(df["Year"], df["Poultry"], marker='v', markersize=6, linestyle='--', linewidth=2, color='red', alpha=0.7, label="Poultry")
l3, = ax.plot(df["Year"], df["Pork"], marker='s', markersize=6, linestyle='-.', linewidth=2, color='green', alpha=0.7, label="Pork")
l4, = ax.plot(df["Year"], df["Fish"], marker='*', markersize=6, linestyle=':', linewidth=2, color='purple', alpha=0.7, label="Fish")
l5, = ax.plot(df["Year"], df["Lamb"], marker='D', markersize=6, linestyle='-', linewidth=2, color='brown', alpha=0.7, label="Lamb")

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Consumption')
ax.set_title('Meat Consumption Over the Years')

# Add a legend
ax.legend()

# Annotate each line at the end of the line with the corresponding legend label
for line, name in zip(ax.lines, ['Beef', 'Poultry', 'Pork', 'Fish', 'Lamb']):
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
    ax.annotate(df["Beef"][i], (df["Year"][i], df["Beef"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Poultry"][i], (df["Year"][i], df["Poultry"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Pork"][i], (df["Year"][i], df["Pork"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Fish"][i], (df["Year"][i], df["Fish"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    ax.annotate(df["Lamb"][i], (df["Year"][i], df["Lamb"][i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Add grid
ax.grid(True)

# Set background color
ax.set_facecolor('lightgray')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")