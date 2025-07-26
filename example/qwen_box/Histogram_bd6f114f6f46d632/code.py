import matplotlib.pyplot as plt

# Data
sizes = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0]
frequency = [30, 55, 48, 42, 38, 20, 15, 10, 5, 2]

# Create histogram
plt.hist(sizes, weights=frequency, bins=len(sizes), edgecolor='black')

# Add labels and title
plt.xlabel("Dust Particle Sizes in Micrometers")
plt.ylabel("Frequency of Dust Particles")
plt.title("Size distribution of cosmic dust particles in an interstellar cloud")

# Add stroke to bars containing center point of bounding box
bbox = plt.gca().get_position().bounds
bbox = [bbox[0] + 0.05, bbox[1] + 0.05, bbox[2] - 0.1, bbox[3] - 0.1]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], fill=False, edgecolor='black', linewidth=2.31, snap=False))

# Display plot
plt.tight_layout()
plt.savefig("Edit_figure.png")