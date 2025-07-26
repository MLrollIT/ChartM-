import matplotlib.pyplot as plt

# The layers
layers = ['Upper Canopy', 'Middle Canopy', 'Lower Canopy']

# The different species
species = ['Birds', 'Insects', 'Primates', 'Reptiles', 'Others']

# The data
birds = [120, 80, 40]
insects = [180, 120, 60]
primates = [60, 40, 20]
reptiles = [40, 30, 10]
others = [50, 30, 10]

# The stackplot
plt.figure(figsize=(10, 6))
plt.stackplot(layers, birds, insects, primates, reptiles, others, labels=species)

# Formatting the plot
plt.legend(loc='upper right')
plt.title('Biome Diversity in Rainforest Canopy')
plt.xlabel('Layers of Rainforest Canopy')
plt.ylabel('Total Number of Species')


plt.tight_layout()
plt.savefig("figure.png")