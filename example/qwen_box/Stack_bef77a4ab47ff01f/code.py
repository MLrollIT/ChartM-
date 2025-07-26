import matplotlib.pyplot as plt

# Specify the data
physical_activity_levels = ['No Activity', 'Low Activity', 'Moderate Activity', 'High Activity']
below_average = [25, 20, 15, 10]
average = [40, 35, 30, 25]
above_average = [35, 45, 55, 65]

# Create the stack plot
fig, ax = plt.subplots()
ax.stackplot(physical_activity_levels, below_average, average, above_average, labels=['Below Average','Average','Above Average'])

# Specify the legend location
plt.legend(loc='upper left')

# Set the title and labels
plt.title('Academic Performance vs Physical Activity')
plt.xlabel('Level of Physical Activity')
plt.ylabel('Percentage of Students')

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")