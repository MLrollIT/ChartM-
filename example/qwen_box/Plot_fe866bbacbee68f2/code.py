from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data
data_csv = '''Year,Smartphones,E-Waste Recycling,Computers,Household Appliances
2015,100,200,300,400
2016,90,210,280,390
2017,85,220,275,385
2018,120,230,250,380
2019,110,240,260,370'''

# Convert the CSV data to DataFrame
data = pd.read_csv(StringIO(data_csv))

# Predefined colors for the products
colors = ['blue', 'green', 'red', 'purple']

# Plot
fig, ax = plt.subplots()

for (column, color) in zip(data.columns[1:], colors):
    ax.plot(data['Year'], data[column], marker='o', linestyle='-.', linewidth=2.0, markersize=5.0, label=column, color=color)
    for x, y in zip(data['Year'], data[column]):
        ax.text(x, y, str(y), color=color)

# Annotations
for (line, name) in zip(ax.lines, data.columns[1:]):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1, y), xytext=(6, 0), color=line.get_color(), 
                xycoords=ax.get_yaxis_transform(), textcoords="offset points",
                size=14, va="center")

ax.set_xlabel('Year')
ax.set_ylabel('Quantity')
ax.set_title('Quantity of Different Products Over the Years')
ax.legend()
ax.grid(True)
ax.set_facecolor('white')  # Set the background color to white
plt.tight_layout()
plt.savefig('myplot.png')