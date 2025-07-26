# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Given data points
star_cluster_density = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
frequency_of_sectors = np.array([12, 18, 25, 30, 22, 15, 10, 8, 4, 2])

# Create bins for histogram
bins = np.linspace(star_cluster_density.min(), star_cluster_density.max(), 10)

# Create histogram
plt.hist(star_cluster_density, bins, weights=frequency_of_sectors, alpha=0.7, color='skyblue', edgecolor='black')

# Plot labels and title
plt.xlabel('Star Cluster Density (clusters per square kiloparsec)')
plt.ylabel('Frequency of Galactic Sectors')
plt.title('Density of Massive Star Clusters Along the Galactic Spiral Arms')

# Set clipping state of bars containing the center point of the bounding box to False
plt.setp(plt.gca().patches, clip_on=False)

# Change snap state of those bars to False
plt.setp(plt.gca().patches, snap=False)

# Show plot
plt.tight_layout()
plt.savefig("figure.png")