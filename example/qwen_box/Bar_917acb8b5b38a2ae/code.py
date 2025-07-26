from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
bus_traffic = [34000, 35500, 36000, 20000, 22000, 40000]
car_traffic = [75000, 78000, 80000, 65000, 70000, 95000]
bike_traffic = [4000, 4100, 2000, 1000, 5000, 6000]
pedestrian_traffic = [15000, 15500, 13000, 7000, 17500, 20000]

# Create plot
fig, ax = plt.subplots()

# Create bars
bars1 = ax.bar(days, bus_traffic, color='b', edgecolor='black', label='Bus Traffic')
bars2 = ax.bar(days, car_traffic, bottom=bus_traffic, color='r', edgecolor='black', label='Car Traffic')
bars3 = ax.bar(days, bike_traffic, bottom=[i+j for i,j in zip(bus_traffic, car_traffic)], color='g', edgecolor='black', label='Bike Traffic')
bars4 = ax.bar(days, pedestrian_traffic, bottom=[i+j+k for i,j,k in zip(bus_traffic, car_traffic, bike_traffic)], color='y', edgecolor='black', label='Pedestrian Traffic')

# Add labels and title
ax.set_ylabel('Traffic Count')
ax.set_xlabel('Day of the Week')
ax.set_title('Traffic Count by Vehicle Type and Day of the Week')

# Add grid and set background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Add legend
ax.legend()

# Annotate data values on bars
ax.bar_label(bars1, label_type='center')
ax.bar_label(bars2, label_type='center')
ax.bar_label(bars3, label_type='center')
ax.bar_label(bars4, label_type='center')

# Layout adjustment and save figure
plt.tight_layout()
plt.savefig("myplot.png")