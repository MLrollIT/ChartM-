import matplotlib.pyplot as plt

# Artifacts Volume
pottery = [1500, 1200, 1300, 1100, 1000]
metal_artifacts = [800, 700, 750, 600, 500]
stone_tools = [600, 500, 550, 450, 400]
ceramics = [300, 250, 270, 200, 180]

# Names of Sites
sites = ['Site A', 'Site B', 'Site C', 'Site D', 'Site E']

# Creating stackplot
plt.stackplot(sites, pottery, metal_artifacts, stone_tools, ceramics, labels=['Pottery','Metal Artifacts','Stone Tools','Ceramics'])

# Adding Labels and Title
plt.xlabel('Archaeological Sites')
plt.ylabel('Volume of Artifacts (cubic meters)')
plt.title('Volumetric Distribution of Artifacts at Underwater Archaeological Sites')

# Adding Legend
plt.legend(loc='upper right')

# Displaying Plot

plt.tight_layout()
plt.savefig("figure.png")