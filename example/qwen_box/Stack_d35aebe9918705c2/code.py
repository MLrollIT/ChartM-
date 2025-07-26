import matplotlib.pyplot as plt

# Data for Tyrannosaurus Rex
tyrannosaurus_rex_years = [500, 400, 300, 200, 100]
tyrannosaurus_rex_population = [100000, 90000, 80000, 60000, 50000]

# Data for Stegosaurus
stegosaurus_years = [500, 400, 300, 200, 100]
stegosaurus_population = [50000, 60000, 70000, 80000, 90000]

# Data for Triceratops
triceratops_years = [500, 400, 300, 200, 100]
triceratops_population = [80000, 70000, 60000, 50000, 40000]

# Data for Velociraptor
velociraptor_years = [500, 400, 300, 200, 100]
velociraptor_population = [30000, 40000, 50000, 60000, 70000]

# Plotting
plt.figure(figsize=(10, 6))

plt.stackplot(tyrannosaurus_rex_years, tyrannosaurus_rex_population, stegosaurus_population, triceratops_population, velociraptor_population,
              labels=['Tyrannosaurus Rex', 'Stegosaurus', 'Triceratops', 'Velociraptor'],
              colors=['blue', 'orange', 'green', 'purple'])

plt.xlabel('Millions of Years Ago')
plt.ylabel('Population Count')
plt.title('Population Progression of Dinosaur Species')
plt.legend(loc='upper left')


plt.savefig('figure.png')
# plt.show()
plt.tight_layout()
plt.savefig("figure.png")