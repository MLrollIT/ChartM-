import matplotlib.pyplot as plt

# Years from 2010 to 2020
years = list(range(2010, 2021))

# Corresponding percentage increase in coral reef coverage annually
growth_percentage = [4, 6, 8, 10, 12, 15, 17, 19, 22, 25, 28]

# Creating step plot
plt.step(years, growth_percentage, where='mid')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Percentage Increase in Coral Reef Coverage')
plt.title('Growth Patterns of Underwater Coral Reefs from 2010 to 2020')

# Displaying the plot

plt.tight_layout()
plt.savefig("figure.png")