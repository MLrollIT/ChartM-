from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia'],
    '2018': [5000, 4500, 3000, 6000, 3500, 4000],
    '2019': [6000, 3500, 5000, 4000, 2000, 3000],
    '2020': [5000, 6000, 4000, 6000, 3500, 5000]
}

df = pd.DataFrame(data)

# Plot the data
fig, ax = plt.subplots()

# Define the bar labels and colors
bar_labels = ['2018', '2019', '2020']
bar_colors = ['tab:blue', 'tab:orange', 'tab:green']

# Draw the bars
bars = ax.bar(df['Region'], df['2018'], color=bar_colors[0], edgecolor='black', tick_label=df['Region'])
bars2 = ax.bar(df['Region'], df['2019'], bottom=df['2018'], color=bar_colors[1], edgecolor='black')
bars3 = ax.bar(df['Region'], df['2020'], bottom=df['2018']+df['2019'], color=bar_colors[2], edgecolor='black')

# Set the chart title and labels
ax.set_ylabel('Sales')
ax.set_xlabel('Region')
ax.set_title('Sales by Region and Year')

# Add a legend
ax.legend([bars, bars2, bars3], bar_labels, title='Year')

# Annotate the bar values
ax.bar_label(bars, label_type='edge')
ax.bar_label(bars2, label_type='edge')
ax.bar_label(bars3, label_type='edge')

# Add grid and set background color
ax.grid(True)
ax.set_facecolor('gray')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")