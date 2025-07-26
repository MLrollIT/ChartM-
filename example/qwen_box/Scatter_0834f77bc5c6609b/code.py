import matplotlib.pyplot as plt

# Creating lists for the type of pets and the number of pets owned
types_of_pets = ['Dogs', 'Cats', 'Rabbits', 'Hamsters', 'Guinea Pigs', 'Birds', 'Fish', 'Reptiles']
number_owned = [5, 8, 3, 7, 4, 6, 2, 1]

# This code is utilized to create a scatter plot
plt.figure(figsize=(10,6))
plt.scatter(number_owned, types_of_pets)

# This code is utilized to name the x-axis and y-axis respectively
plt.xlabel('Number of Each Type of Pet Owned')
plt.ylabel('Type of Small Pet')

# This code is utilized to make each data point easier to comprehend
for i in range(len(number_owned)):
    plt.text(number_owned[i], types_of_pets[i], (number_owned[i], types_of_pets[i]))

# This code is utilized to give our scatter plot a title
plt.title('Popularity of Different Types of Small Pets')

# This code is utilized to change the shape of the points that contain the center point of the bounding box to 'triangle'
plt.scatter(number_owned[6], types_of_pets[6], marker='^', color='gold', edgecolors='black', linewidths=2, s=100, alpha=0.5)

# This code is utilized to apply a shadow effect to these points with a 5.1-pixel offset and a foreground color of gold
plt.scatter(number_owned[6], types_of_pets[6], marker='^', color='gold', edgecolors='black', linewidths=2, s=100, alpha=0.5, offset=[5.1, 0], transform=plt.gca().transAxes)

# This code is utilized to give our scatter plot a title
plt.title('Popularity of Different Types of Small Pets')

# Finally, this code is utilized to showcase our scatter plot
plt.tight_layout()
plt.savefig("Edit_figure.png")