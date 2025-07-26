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

# Modify the bars that contain the center point of the bounding box
bbox = plt.Bbox([[146, 41], [146 + 120, 41 + 471]])
for bar in plt.gca().patches:
    if bbox.contains(bar.get_bbox().get_points()[0]):
        bar.set_linewidth(4.96)
        bar.set_facecolor('#c53ee0')

# Display plot
plt.tight_layout()
plt.savefig("figure.png")