from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Given data
data_str = '''"Injury Type","2010","2015","2020"
"Burns",120,200,180
"Fractures",300,380,250
"Sprains",70,300,310'''

# Read the data using pandas
data = pd.read_csv(StringIO(data_str), quotechar='"')

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars = ax.bar(data['Injury Type'], data['2010'], color='skyblue', edgecolor='black', label='2010')
ax.bar(data['Injury Type'], data['2015'], bottom=data['2010'], color='lightcoral', edgecolor='black', label='2015')
ax.bar(data['Injury Type'], data['2020'], bottom=data['2010']+data['2015'], color='lightgreen', edgecolor='black', label='2020')

# Annotate the data value on the chart with increased font size
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), 
             fontsize=12, color='black', ha='center', va='bottom')  # Font size increased from 10 to 12

# Set title, x-label and y-label
ax.set_title('Injury Cases Over Years')
ax.set_xlabel('Injury Type')
ax.set_ylabel('Number of Cases')

# Add grid
ax.grid(True)

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend
ax.legend(loc='upper right')

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")