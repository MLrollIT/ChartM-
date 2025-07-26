import matplotlib.pyplot as plt

locations = ['Point A', 'Point B', 'Point C', 'Point D', 'Point E']

# Water Flow Velocities
surface_velocity = [10, 12, 9, 11, 13]
mid_velocity = [8, 10, 7, 9, 11]
seabed_velocity = [6, 8, 5, 7, 9]

# Temperature Gradients
surface_temps = [0.5, 0.6, 0.4, 0.7, 0.8]
mid_temps = [0.3, 0.4, 0.2, 0.5, 0.6]
seabed_temps = [0.2, 0.3, 0.1, 0.4, 0.5]

plt.figure(figsize=(10,6))

# Stack plot for Water Flow Velocities
plt.subplot(2, 1, 1)
plt.stackplot(locations, surface_velocity, mid_velocity, seabed_velocity, labels=['Surface','Mid-Depth','Seabed'])
plt.title("Ocean Currents Around Barrier Reef")
plt.xlabel("Locations")
plt.ylabel("Water Flow Velocity (cm/s)")
plt.legend(loc='upper left')

# Stack plot for Temperature Gradients
plt.subplot(2, 1, 2)
plt.stackplot(locations, surface_temps, mid_temps, seabed_temps, labels=['Surface','Mid-Depth','Seabed'])
plt.title("Temperature Gradients Around Barrier Reef")
plt.xlabel("Locations")
plt.ylabel("Temperature Gradient (°C/m)")
plt.legend(loc='upper left')

# Change the face color of the areas that share the same legend with the area that contains the center point of the bounding box to #c1eb40
# Update the edge's linestyle to 'dotted' and set the edge color to #525dee for that same areas
bbox = plt.gca().get_position().get_points()
bbox[1] = [0.5, 0.5]
bbox[2] = [0.5, 0.5]
plt.gca().set_position(bbox)
plt.gca().patch.set_facecolor('#c1eb40')
plt.gca().patch.set_edgecolor('#525dee')
plt.gca().patch.set_linestyle('dotted')

plt.tight_layout()
plt.savefig("figure.png")