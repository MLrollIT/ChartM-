import matplotlib.pyplot as plt

# specify depth levels
depth_levels = ['10m', '20m', '30m', '40m']

# specify the abundance of each coral species at each depth level
coral_species_A = [15, 10, 5, 2]
coral_species_B = [8, 12, 6, 4]
coral_species_C = [5, 3, 2, 1]

# create a stackplot
plt.stackplot(depth_levels, coral_species_A, coral_species_B, coral_species_C, labels=['Coral Species A','Coral Species B','Coral Species C'])

# define the plot title, x-label, and y-label
plt.title('Biodiversity Distribution of Different Coral Species')
plt.xlabel('Depth Levels')
plt.ylabel('Abundance')

# add a legend
plt.legend(loc='upper right')

# display the plot

plt.tight_layout()
plt.savefig("figure.png")