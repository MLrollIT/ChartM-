import matplotlib.pyplot as plt

sectors = [1, 2, 3, 4]
Alien1 = [10, 12, 8, 15]
Alien2 = [5, 7, 10, 3]
Alien3 = [8, 6, 4, 12]

plt.stackplot(sectors, Alien1, Alien2, Alien3, labels=['Alien1','Alien2','Alien3'])
plt.xlabel("Sectors")
plt.ylabel("Number of Aliens")
plt.title("Distribution of Alien Life Forms Across Sectors")
plt.legend(loc='upper left')

# Change the edge color of the filled area that contains the center point of the bounding box to #2252c9
plt.fill_betweenx([1.5], sectors, color='#2252c9', edgecolor='none', linestyle='solid')

# Set the edge linestyle of this area to 'solid' and update its color to #74621f
plt.fill_betweenx([1.5], sectors, color='#74621f', edgecolor='none', linestyle='solid')

plt.tight_layout()
plt.savefig("figure.png")