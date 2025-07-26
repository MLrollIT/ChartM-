import matplotlib.pyplot as plt

# Our data:
expeditions = [1, 2, 3, 4]
alien_creatures = [8, 5, 9, 6]
lost_shipwrecks = [4, 2, 1, 3]
ancient_artefacts = [6, 4, 7, 5]
mysterious_structures = [3, 1, 5, 2]

plt.figure(figsize=[10, 5])

# Plotting stackplot with desired colors:
plt.stackplot(expeditions, alien_creatures, lost_shipwrecks, ancient_artefacts, mysterious_structures, 
              colors=['green', 'blue', 'orange', 'purple'])

# Adding a legend:
plt.legend(['Alien-like Creatures', 'Lost Shipwrecks', 'Ancient Arterfacts', 'Mysterious Structures'], loc='upper left')

# Change the label of the area that contains the center point of the bounding box to 'A new Label'
plt.annotate('A new Label', xy=(2.5, 10), xytext=(2.5, 10), arrowprops=dict(facecolor='black', shrink=0.05))

# Update the line style for that same area to ':' and color to black
plt.plot([2.5, 2.5], [10, 10], color='black', linestyle=':')

plt.title('Mysterious Discoveries Across Expeditions')
plt.xlabel('Expeditions')
plt.ylabel('No. of Discoveries')


plt.tight_layout()
plt.savefig("figure.png")