import matplotlib.pyplot as plt

# Names of regions
regions = ['Valles Marineris', 'Olympus Mons', 'Tharsis Montes', 'Hellas Planitia']

# Data for each terrain type in each region
plains = [30, 10, 35, 25]
plateaus = [20, 30, 15, 25]
canyons = [25, 20, 10, 30]
mountains = [25, 40, 40, 20]

# Generate a stack plot
plt.figure(figsize=(10,7))
plt.stackplot(regions, plains, plateaus, canyons, mountains, labels=['Plains','Plateaus','Canyons','Mountains'], alpha=0.8)

# Define labels and title
plt.legend(loc='upper left')
plt.title('Terrain Composition in Various Martian Regions')
plt.xlabel('Martian Regions')
plt.ylabel('Terrain Composition (%)')

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(plt.gca().bbox_to_transform(