import matplotlib.pyplot as plt

# Data points for population count at different depths for each underground society
depths = [1, 2, 3, 4, 5]
populations = {
    'Society X': [500, 600, 550, 700, 650],
    'Society Y': [300, 450, 400, 350, 300],
    'Society Z': [800, 700, 750, 900, 850]
}

plt.figure(figsize=(10, 6))

for society, population in populations.items():
    plt.step(depths, population, label=society, where='mid')

plt.xlabel('Depth (km)')
plt.ylabel('Population Count')
plt.title('Subterranean Civilizations Mapped Using 3D')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("figure.png")

# Modify the transparency of the step lines that contain the center point of the bounding box to 0.89
bbox = plt.gca().bbox
bbox_points = bbox.get_points()
bbox_points[1][0] = 0.5
bbox_points[1][1] = 0.5
bbox.set_points(bbox_points)

# Set the picker state of those same lines to False
plt.step(depths, populations['Society X'], label='Society X', where='mid', picker=False)
plt.step(depths, populations['Society Y'], label='Society Y', where='mid', picker=False)
plt.step(depths, populations['Society Z'], label='Society Z', where='mid', picker=False)

plt.xlabel('Depth (km)')
plt.ylabel('Population Count')
plt.title('Subterranean Civilizations Mapped Using 3D')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("figure.png")