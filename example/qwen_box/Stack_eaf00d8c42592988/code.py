import matplotlib.pyplot as plt
import numpy as np

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# Water flow data for each basin
basin_X = [100,120,110,130,140,135,150,155,140,130,125,110]
basin_Y = [80,85,90,95,100,105,110,115,120,125,130,135]
basin_Z = [70,75,80,85,90,95,100,105,110,115,120,125]

plt.figure(figsize=[10,5])
plt.stackplot(months, basin_X, basin_Y, basin_Z, labels=['Basin X','Basin Y','Basin Z'])
plt.legend(loc='upper left')
plt.title('Monthly Average Water Flow Rates in River Basins X, Y, Z')
plt.xlabel('Month')
plt.ylabel('Water flow rate (m³/s)')

# Change the color of the area that contains the center point of the bounding box to #f78037
bbox = plt.gca().get_position().get_points()
bbox[1] = [0.5, 0.5]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), 0.05, 0.05, facecolor='#f78037', edgecolor='none'))

# Set the face color of the same area to #30926f
bbox = plt.gca().get_position().get_points()
bbox[1] = [0.5, 0.5]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), 0.05, 0.05, facecolor='#30926f', edgecolor='none'))

plt.tight_layout()
plt.savefig("figure.png")