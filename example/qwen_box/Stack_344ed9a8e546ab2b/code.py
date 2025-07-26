import matplotlib.pyplot as plt

# Years of the journey
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']

# Distances from Earth
alpha_centauri = [4.3, 4.4, 4.5, 4.5, 4.6]
sirius = [8.6, 8.5, 8.4, 8.3, 8.2]
betelgeuse = [642, 640, 638, 636, 634]
polaris = [443, 442, 441, 441, 440]

plt.stackplot(years, alpha_centauri, sirius, betelgeuse, polaris, colors=['red', 'blue', 'green', 'purple'])

# Add legend
plt.legend(['Alpha Centauri', 'Sirius', 'Betelgeuse', 'Polaris'], loc='upper left')

plt.title("Journey of a Spacecraft to Various Stars")
plt.xlabel("Years")
plt.ylabel("Distance from Earth (in light-years)")

# Set the snap state of the area containing the center point of the bounding box to False, and also make this area invisible
bbox = plt.gca().bbox
bbox.width = 0
bbox.height = 0
plt.gca().set_snap(False)

plt.tight_layout()
plt.savefig("Edit_figure.png")