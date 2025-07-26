import matplotlib.pyplot as plt

# Data
galactic_longitude = [30, 60, 90, 120, 150]
spiral_arms = [2.5, 3.0, 3.5, 4.0, 4.5]
galactic_center = [5.5, 6.0, 6.5, 7.0, 7.5]
interstellar_space = [1.0, 1.5, 2.0, 2.5, 3.0]

labels = ['Spiral Arms', 'Galactic Center', 'Interstellar Space']

# Create the stackplot
plt.figure(figsize=(10,7)) 
plt.stackplot(galactic_longitude, spiral_arms, galactic_center, interstellar_space, labels=labels)

plt.xlabel('Galactic Longitude (degrees)')
plt.ylabel('Gas Amount (10^6 solar masses)')
plt.title('Galactic Gas Cloud Formation Analysis')
plt.legend(loc='upper left')

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")

# Modify the bounding box
bbox = plt.gca().get_position()
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transform