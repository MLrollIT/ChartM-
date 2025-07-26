import matplotlib.pyplot as plt

# Data Points for Terrain Elevation
regions = ['R1', 'R2', 'R3']
terrain_elevation = [[100, 150, 200, 180, 120], [80, 120, 160, 140, 100], [60, 90, 120, 110, 70]]

# Data Points for Water Flow
water_flow = [[50, 60, 70, 65, 55], [45, 55, 65, 60, 50], [40, 50, 60, 55, 45]]

# Stack Plot for Terrain Elevation
plt.figure(figsize=(10,6))
plt.stackplot(range(1,6), terrain_elevation, labels=['R1 Elevation', 'R2 Elevation', 'R3 Elevation'])
plt.legend(loc='upper left')

# Overlay Plot for Water Flow
for i, flow in enumerate(water_flow):
    plt.plot(range(1,6), flow, marker='o', label=f'{regions[i]} Flow')

plt.title('Terrain Elevation vs. Water Flow in River Regions')
plt.xlabel('Time Period')
plt.ylabel('Elevation/Flow')
plt.legend(loc='lower right')

# Update the linewidth of the area that contains the center point of the bounding box to 4.04, and edge color of red
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.3
bbox[1] = 0.3
bbox[2] = 0.4
bbox[3] = 0.4
plt.gca().set_position(bbox)
plt.gca().patch.set_linewidth(4.04)
plt.gca().patch.set_edgecolor('red')

# Apply a stroke to the same area with a linewidth of 2.20 and set the foreground color to #bd10f1
plt.gca().patch.set_linewidth(2.20)
plt.gca().patch.set_facecolor('#bd10f1')

plt.tight_layout()
plt.savefig("figure.png")