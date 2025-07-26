import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

# Define the data
spatial_positions = [0, 1, 2, 3, 4, 5, 6]
probability_amplitudes = [0.1, 0.3, 0.5, 0.4, 0.2, 0.1, 0]

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the data using a step plot
ax.step(spatial_positions, probability_amplitudes, where='mid', color='purple', linestyle='-', linewidth=2)

# Set the labels and title
ax.set_xlabel('Spatial Positions')
ax.set_ylabel('Probability Amplitudes')
ax.set_title('Quantum Particle Position Probability Distribution')

# Display grid
ax.grid(True)

# Set the animated state of the step lines that include the center point of the bounding box to True
bbox = Bbox([[118, 333], [118 + 397, 333 + 822]])
for line in ax.get_lines():
    line.set_animated(True)
    line.set_clip_box(bbox)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")