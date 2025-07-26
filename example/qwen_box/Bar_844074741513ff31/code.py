from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the data
data = StringIO("""
Year,Arctic Sea Ice,Antarctic Sea Ice,Global Sea Level
2000,12.4,10.8,0
2005,11.7,11.2,2.1
2010,11.2,12.1,3.4
2015,10.8,12.2,4.6
2020,9.3,11.6,5.8
2025,8.7,11.3,6.5
""")
df = pd.read_csv(data)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars1 = ax.bar(df['Year'] - 1, df['Arctic Sea Ice'], color='skyblue', edgecolor='black', width=1, label='Arctic Sea Ice')
bars2 = ax.bar(df['Year'], df['Antarctic Sea Ice'], color='lightgreen', edgecolor='black', width=1, label='Antarctic Sea Ice')
bars3 = ax.bar(df['Year'] + 1, df['Global Sea Level'], color='lightcoral', edgecolor='black', width=1, label='Global Sea Level')

# Set title, x-label and y-label
ax.set_title('Sea Ice and Sea Level Changes')
ax.set_xlabel('Year')
ax.set_ylabel('Value')

# Add grid
ax.grid(True, which='both')

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend
ax.legend(loc='upper left')

# Add the corresponding value at the end of each bar
ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)
ax.bar_label(bars3, padding=3)

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")