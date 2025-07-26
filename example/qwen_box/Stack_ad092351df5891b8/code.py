import matplotlib.pyplot as plt
import numpy as np

# Stacking the 'x' values for each ocean layer
ocean_layers = ('Surface Layer', 'Thermocline', 'Deep Ocean', 'Seafloor')

# Stacking the 'y' values for temperature values
surface_layer = np.array([25, 24, 23, 22])
thermocline = np.array([20, 18, 16, 14])
deep_ocean = np.array([8, 6, 4, 2])
seafloor = np.array([3, 2, 1, 0])

# Aggregate values for stacking bars
aggregate = np.row_stack((surface_layer, thermocline, deep_ocean, seafloor))

# Creating the stackplot
fig, ax = plt.subplots()

ax.stackplot(ocean_layers, aggregate, labels=['Surface Layer', 'Thermocline','Deep Ocean','Seafloor'])
ax.legend(loc='upper right')

plt.ylabel('Temperature (°C)')
plt.title('Temperature Distribution in Ocean Layers')

# Set the clipping box for the area that contains the center point of the bounding box
bbox = plt.Bbox([[79, 151], [79 + 269, 151 + 257]])
ax.add_patch(plt.Rectangle((bbox.x0, bbox.y0), bbox.width, bbox.height, facecolor='#5fd5ff', alpha=0.5))

plt.tight_layout()
plt.savefig("figure.png")