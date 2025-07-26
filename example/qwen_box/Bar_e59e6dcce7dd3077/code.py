from io import StringIO
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the data
data = '''Year,Bus,Rail,Car
2010,12000,14000,10000
2011,13000,16000,11000
2012,14000,18000,12000
2013,9000,20000,13000
2014,10000,22000,14000
2015,11000,24000,15000
2016,12000,26000,16000
2017,13000,12000,17000'''
df = pd.read_csv(StringIO(data))

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
width = 0.2 # the width of the bars
x = np.arange(len(df['Year']))  # the label locations

rects1 = ax.bar(x - width, df['Bus'], width, label='Bus', color='skyblue', edgecolor='black')
rects2 = ax.bar(x, df['Rail'], width, label='Rail', color='green', edgecolor='black')
rects3 = ax.bar(x + width, df['Car'], width, label='Car', color='red', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Year')
ax.set_ylabel('Number of Passengers')
ax.set_title('Number of Passengers by Year and Transportation Type')
ax.set_xticks(x)
ax.set_xticklabels(df['Year'])
ax.legend()

# Add grid
ax.grid(True)

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add the corresponding value at the top of each bar
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")