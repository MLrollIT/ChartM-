from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Given data
data = """Year,EV Sales,EV Charging Stations
2011,5000,1000
2012,4500,950
2013,4000,900
2014,3500,2300
2015,7000,2100
2016,10000,2000
2017,9500,1800
2018,9000,2500
2019,8500,2400"""

# Read the data into a pandas DataFrame
df = pd.read_csv(StringIO(data))

fig, ax = plt.subplots()

# Draw the bars for EV Sales and EV Charging Stations
bars1 = ax.bar(df['Year'] - 0.2, df['EV Sales'], width=0.4, color='b', align='center', label='EV Sales', edgecolor='black')
bars2 = ax.bar(df['Year'] + 0.2, df['EV Charging Stations'], width=0.4, color='r', align='center', label='EV Charging Stations', edgecolor='black')

# Annotate the data values on the bars
ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)

# Set the x-ticks and labels
ax.set_xticks(df['Year'])
ax.set_xticklabels(df['Year'])

# Set the labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of EV Sales/Charging Stations')
ax.set_title('EV Sales and Charging Stations Over the Years')

# Add the legend
ax.legend()

# Remove the grid and set the background color to white
ax.grid(False)
ax.set_facecolor('white')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")