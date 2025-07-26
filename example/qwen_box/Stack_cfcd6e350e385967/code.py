import matplotlib.pyplot as plt

# Define years
years = list(range(2010, 2021))

# Define data for each dog breed
breed_1_data = [10, 9, 8, 7, 5, 6, 5, 4, 3, 4, 5]
breed_2_data = [8, 7, 6, 7, 8, 9, 10, 9, 8, 7, 6]
breed_3_data = [6, 7, 8, 8, 9, 8, 8, 8, 9, 10, 11]
breed_4_data = [9, 9, 8, 8, 7, 7, 6, 7, 7, 6, 5]
breed_5_data = [12, 13, 14, 15, 17, 18, 18, 19, 20, 20, 19]

# Plot data
plt.stackplot(years, breed_1_data, breed_2_data, breed_3_data, breed_4_data, breed_5_data, labels=['Breed 1', 'Breed 2', 'Breed 3', 'Breed 4', 'Breed 5'])
plt.legend(loc='upper left')

# Customize plot
plt.title('Popularity of Top 5 Dog Breeds Over the Years')
plt.xlabel('Years')
plt.ylabel('Popularity Percentage')

# Show plot
plt.tight_layout()
plt.savefig("figure.png")