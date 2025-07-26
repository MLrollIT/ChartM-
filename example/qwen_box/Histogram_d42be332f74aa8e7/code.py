# Required Libraries
import matplotlib.pyplot as plt

# Data
depth_bins = ["0-100", "101-200", "201-300", "301-400", "401-500"]
jellyfish_sightings = [5, 12, 8, 14, 6]

# Create histogram
plt.figure(figsize=(10,6))
plt.bar(depth_bins, jellyfish_sightings, color='c', alpha=0.7)

# x-axis and y-axis labels
plt.xlabel('Depth Ranges in Meters', fontsize=14)
plt.ylabel('Frequency of Jellyfish Sightings', fontsize=14)

# Title
plt.title('Jellyfish Sightings at Different Ocean Depths', fontsize=16)

# Set the rasterized state of the histogram bars that contain the center point of the bounding box to True
plt.bar(depth_bins, jellyfish_sightings, rasterized=True, alpha=0.7)

# Ensure that the snapping state for these histogram bars is also set to True
plt.bar(depth_bins, jellyfish_sightings, snap=True, alpha=0.7)

# Show plot
plt.tight_layout()
plt.savefig("figure.png")