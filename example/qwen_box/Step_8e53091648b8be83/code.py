import matplotlib.pyplot as plt

# Time series (X axis)
years = list(range(2010, 2020))

# Population counts (Y axis)
lion_pop = [10, 12, 15, 17, 20, 22, 25, 27, 30, 33]
giraffe_pop = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
elephant_pop = [8, 10, 13, 16, 20, 24, 28, 32, 36, 40]

# Set figure size
plt.figure(figsize=(10,6))

# Plot data
plt.step(years, lion_pop, where='mid', label="Lions")
plt.step(years, giraffe_pop, where='mid', label="Giraffes")
plt.step(years, elephant_pop, where='mid', label="Elephants")

# Set plot title and labels
plt.title('Population Dynamics in the Zoo (2010-2019)')
plt.xlabel('Year')
plt.ylabel('Population Count')

# Set legend
plt.legend(title="Species")

# Fill the area below the step line that includes the center point of the bounding box with a gradient that smoothly transitions from '#7f3b14' to '#1a4e8d'.
plt.fill_between(years, [10, 12, 15, 17, 20, 22, 25, 27, 30, 33], [5, 7, 9, 11, 13, 15, 17, 19, 21, 23], color='gray', alpha=0.5)

# Show plot
plt.tight_layout()
plt.savefig("figure.png")