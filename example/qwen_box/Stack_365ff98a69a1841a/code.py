import matplotlib.pyplot as plt

# List of industries
industries = ['Education', 'Healthcare', 'Technology', 'Manufacturing', 'Retail']

# Corresponding unemployment rate values
unemployment_rate = [6.5, 5.8, 4.2, 7.3, 8.1]

# Corresponding income inequality index values
income_inequality_index = [0.15, 0.25, 0.45, 0.35, 0.6]

# Creating stack plot
plt.figure(figsize=(10,7))
plt.stackplot(industries, unemployment_rate, income_inequality_index, labels=['Unemployment Rate', 'Income Inequality Index'], colors=['blue', 'orange'])

# Adding legend
plt.legend(loc='upper left')

# Setting labels for the axes
plt.xlabel('Industries')
plt.ylabel('Percentage/Index')

# Setting title for the plot
plt.title('Stack Plot of Unemployment Rate and Income Inequality Index Across Different Industries')

# Display the plot
plt.tight_layout()

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform((0.5, 0.5))

# Set the visibility of the center point of the bounding box to False
plt.gca().patch.set_visible(False)

# Adjust the z-order of the area to 9
plt.gca().patch.set_zorder(9)

# Display the plot
plt.savefig("Edit_figure.png")