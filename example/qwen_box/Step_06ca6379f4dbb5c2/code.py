import matplotlib.pyplot as plt

# Given Data
longitudes = [32.5, 33.0, 33.5, 34.0, 34.5] # X-axis
depths = [1000, 920, 850, 1100, 950]  # Y-axis

# Create the plot
plt.figure()
plt.step(longitudes, depths, where='mid')

# Set label names
plt.xlabel("Longitude (degrees)")
plt.ylabel("Ocean Depth (meters)")

# Set plot title
plt.title("Ocean Depth Exploration Model")

# Show the plot
plt.grid(True)  # to enable grid

# Add a new label to the center point of the bounding box
bbox = plt.gca().bbox_to_transform((0.5, 0.5))
plt.text(0.5, 0.5, 'A new Label', transform=bbox, zorder=18, ha='center', va='center', color='black', shadow=True, offset=(3.34, 2.11))

plt.tight_layout()
plt.savefig("figure.png")