from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Given CSV data
csv_data = '''Year,AI Technology,Robotics,IoT Technology
2010,500,200,150
2011,510,210,160
2012,550,220,170
2013,520,230,180
2014,600,240,190
2015,610,250,200
2016,620,260,210
2017,650,500,220
2018,660,510,230
2019,670,520,240
2020,680,250,250
2021,690,260,500'''

# Create DataFrame from CSV data
data = pd.read_csv(StringIO(csv_data))

# Prepare figure and axis
fig, ax = plt.subplots()

# Bar configurations
width = 0.2
x = np.arange(len(data))

# Draw bars
bars1 = ax.bar(x - width, data['AI Technology'], width, label='AI Technology', edgecolor='black', color='blue')
bars2 = ax.bar(x, data['Robotics'], width, label='Robotics', edgecolor='black', color='red')
bars3 = ax.bar(x + width, data['IoT Technology'], width, label='IoT Technology', edgecolor='black', color='green')

# Add bar labels
ax.bar_label(bars1)
ax.bar_label(bars2)
ax.bar_label(bars3)

# Set x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(data['Year'])

# Set labels, title, legend
ax.set_xlabel('Year')
ax.set_ylabel('Investment in Technology (in millions)')
ax.set_title('Investment in AI, Robotics and IoT Technologies Over the Years')
ax.legend()

# Set grid and background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Modify the bars that shares the same legend with the bar that contains the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0