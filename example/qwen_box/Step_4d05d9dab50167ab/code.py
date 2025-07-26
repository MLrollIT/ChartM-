import matplotlib.pyplot as plt

# Data
distance = [0, 10, 20, 30, 40]
depth_100m = [5000, 4800, 4600, 4400, 4200]
depth_200m = [4800, 4600, 4400, 4200, 4000]
depth_300m = [4500, 4300, 4100, 3900, 3700]

plt.figure(figsize=(10,8))

# Line plots for each depth
plt.step(distance, depth_100m, where='mid', label='Depth 100m')
plt.step(distance, depth_200m, where='mid', label='Depth 200m')
plt.step(distance, depth_300m, where='mid', label='Depth 300m')

# Labels and Legend
plt.xlabel('Distance from coast (km)')
plt.ylabel('Volumetric flow rate (m³/s)')
plt.title('Oceanic Currents Analysis')
plt.legend()

# Show the plot
plt.grid(True)

# Fill the area below the step line that contains the center point of the bounding box with a gradient
plt.fill_between(distance, depth_100m, depth_200m, where=(distance > 10) & (distance < 20), color='green', alpha=0.5)
plt.fill_between(distance, depth_200m, depth_300m, where=(distance > 20) & (distance < 30), color='orange', alpha=0.5)

plt.tight_layout()
plt.savefig("figure.png")