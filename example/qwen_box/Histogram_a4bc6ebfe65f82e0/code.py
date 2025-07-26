import matplotlib.pyplot as plt

# Data
distances = [1.2, 2.7, 3.5, 4.1, 5.9, 6.3, 7.4, 8.0, 9.2, 10.5, 11.3, 12.8, 13.5, 14.7, 15.1, 16.9, 17.3, 18.6, 19.2, 20.4, 21.7, 22.8, 23.4, 24.6, 25.0, 26.2, 27.3, 28.5, 29.1, 30.3]

# Create Histogram
plt.hist(distances, bins=20, edgecolor='black')

# Set Labels
plt.xlabel('Distance in meters')
plt.ylabel('Number of robots')
plt.title('Robot Swarm Movement Analysis')

# Show Plot
plt.tight_layout()
plt.savefig("figure.png")

# Modify the transparency of the bars that contain the center point of the bounding box to 0.57, and change their face color to #a19664.
bbox = (10, 15, 20, 25)
plt.bar(distances[bbox[0]:bbox[1]], alpha=0.57, color="#a19664")