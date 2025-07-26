from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# The data given in csv format
data = StringIO("""
Year,Smartphones,IoT Devices,AI Technology
2015,500,100,50
2016,550,200,60
2017,700,300,70
2018,2000,400,100
2019,2100,600,130
""")

# Read the data into a pandas DataFrame
df = pd.read_csv(data)

# Create a new figure and a set of subplots
fig, ax = plt.subplots()

# The x-axis labels
years = df['Year'].values

# The bar heights
smartphones = df['Smartphones'].values
iot_devices = df['IoT Devices'].values
ai_technology = df['AI Technology'].values

# The labels for the bars
bar_labels = ['Smartphones', 'IoT Devices', 'AI Technology']

# The colors for the bars
bar_colors = ['tab:blue', 'tab:orange', 'tab:green']

# Plot the data
bars1 = ax.bar(years-0.2, smartphones, width=0.2, color=bar_colors[0], align='center', label=bar_labels[0])
bars2 = ax.bar(years, iot_devices, width=0.2, color=bar_colors[1], align='center', label=bar_labels[1])
bars3 = ax.bar(years+0.2, ai_technology, width=0.2, color=bar_colors[2], align='center', label=bar_labels[2])

# Add the labels to the bars
ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)
ax.bar_label(bars3, padding=3)

# Set the labels for the x-axis and y-axis
ax.set_xlabel('Year')
ax.set_ylabel('Number of Devices')

# Set the title for the plot
ax.set_title('Number of Devices by Year and Type')

# Add a legend
ax.legend(title='Device Type')

# Add grid
ax.grid(True)

# Set the background color for the plot
ax.set_facecolor('lightgray')

# Ensure everything fits
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")