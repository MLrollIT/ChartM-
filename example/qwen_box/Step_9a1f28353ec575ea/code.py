import matplotlib.pyplot as plt

species = ['Psychrobacter', 'Chryseobacterium', 'Pseudomonas', 'Flavobacterium', 'Arthrobacter']
abundance = [126, 93, 85, 72, 64]

plt.step(species, abundance, where='mid', color='purple')
plt.title('Microbial Diversity in Antarctic Ice Samples')
plt.xlabel('Microbial Species')
plt.ylabel('Abundance')
plt.grid(True)

# Change the color of the step that contains the center point of the bounding box to #69b8c0
plt.step(species, abundance, where='mid', color='#69b8c0')

plt.tight_layout()
plt.savefig("Edit_figure.png")