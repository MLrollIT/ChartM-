import matplotlib.pyplot as plt

# given data
depth_zones = ['Surface', 'Epipelagic\nZone', 'Mesopelagic\nZone', 'Bathypelagic\nZone', 'Abyssopelagic\nZone']
temperature_ranges = [25, 20, 15, 10, 5 ]

# plot
plt.figure(figsize=(10,7))
plt.step(temperature_ranges, depth_zones, where='post')

# labels & title
plt.title("Ocean Temperature Influence on Marine Life Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Ocean Depth Zones")

plt.grid(True)

# update linewidth and transformation of the line linked to the center point of the bounding box
plt.plot([5, 5], [0, 1], linewidth=1.17, transform=plt.gca().transAxes)

plt.tight_layout()
plt.savefig("Edit_figure.png")