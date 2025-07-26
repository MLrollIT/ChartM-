import matplotlib.pyplot as plt

# Data
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
animal_species = [5000, 4000, 3000, 2500, 4500, 2000]

# Create Stair Plot
plt.step(continents, animal_species, where='mid', label='Animal Species')

# Labeling Plot
plt.title('Diversity of Animal Species by Continent')
plt.xlabel('Continents')
plt.ylabel('Number of Animal Species')
plt.legend()

# Adjust transformation of the line that contains the center point of the bounding box
trans = plt.gca().transData
trans = trans.transform((0, 0))
trans = trans + plt.gca().bbox.transform((0, 0))
trans = trans + plt.gca().bbox.transform((0, 0))

# Display plot
plt.tight_layout()
plt.savefig("Edit_figure.png")