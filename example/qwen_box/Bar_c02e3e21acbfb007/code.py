from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = StringIO("""
Year,USA Consumption,Brazil Consumption,Germany Consumption
2017,10.2,13.4,7.8
2018,9.7,14.2,7.3
2019,10,15.1,8
2020,10.3,15.9,8.9
""")

df = pd.read_csv(data)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8,6))

# Plot the data
bar1 = ax.bar(df['Year'] - 0.2, df['USA Consumption'], color='skyblue', edgecolor='black', width=0.2)
bar2 = ax.bar(df['Year'], df['Brazil Consumption'], color='lightgreen', edgecolor='black', width=0.2)
bar3 = ax.bar(df['Year'] + 0.2, df['Germany Consumption'], color='lightcoral', edgecolor='black', width=0.2)

# Add data value labels to the bars
ax.bar_label(bar1, padding=3)
ax.bar_label(bar2, padding=3)
ax.bar_label(bar3, padding=3)

# Set title, x-label and y-label
ax.set_title('Country-wise Consumption Over Years')
ax.set_xlabel('Year')
ax.set_ylabel('Consumption')

# Add grid
ax.grid(True, which='both')

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend
ax.legend(["USA", "Brazil", "Germany"], loc='upper left')

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")