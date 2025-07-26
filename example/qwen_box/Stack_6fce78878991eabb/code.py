import matplotlib.pyplot as plt

# Data
days = [i for i in range(1, 8)]
valley = [10, 8, 6, 12, 9, 7, 11]
crater = [5, 3, 7, 4, 5, 2, 6]
mountain = [2, 4, 1, 6, 3, 8, 1]

# Plotting
plt.stackplot(days, valley, crater, mountain, labels=['Valley', 'Crater', 'Mountain'])
plt.legend(loc='upper left')

# Labels and Title
plt.xlabel('Days')
plt.ylabel('Number of Rock Samples')
plt.title('Terrain Mapping Data Collected by Mars Rover')

# Set the color of the area that contains the center point of the bounding box to #d734d4
bbox = plt.gca().get_position().get_points()
bbox[0] = (2.5, 12.5)
bbox[1] = (3.5, 13.5)
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[1][0], facecolor='#d734d4', transform=plt.gca().transAxes))

plt.tight_layout()
plt.savefig("figure.png")