import matplotlib.pyplot as plt
import numpy as np

# Define the time points and entanglement values for each pair of particles
time = np.array([1,2,3,4,5])
entanglement_pair1 = np.array([0.82, 0.75, 0.68, 0.61, 0.56])
entanglement_pair2 = np.array([0.91, 0.85, 0.78, 0.72, 0.66])
entanglement_pair3 = np.array([0.95, 0.89, 0.83, 0.77, 0.71])

# Create the scatter plot
plt.scatter(time, entanglement_pair1, label='Particle Pair 1')
plt.scatter(time, entanglement_pair2, label='Particle Pair 2')
plt.scatter(time, entanglement_pair3, label='Particle Pair 3')

plt.xlabel('Time')
plt.ylabel('Entanglement')
plt.title('Quantum Entanglement in TimeSpace Theory')
plt.legend()
plt.grid(True)

# Modify the shape of the points that share the same legend as those containing the center point of the bounding box to 'star'
# Set their edge color to #e9b2c1 and adjust the edge width to 2.3
bbox = plt.gca().bbox_to_transform((0.5, 0.5))
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.get_window_extent().transformed(plt.gcf().transFigure)
bbox = bbox.get_points()
bbox = bbox.tolist()
bbox = [bbox[0][0], bbox[1][0], bbox[0][1], bbox[1][1]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1], bbox[3]]
bbox = [bbox[0], bbox[2], bbox[1