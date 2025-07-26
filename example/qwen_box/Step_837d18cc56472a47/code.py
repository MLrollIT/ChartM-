import matplotlib.pyplot as plt

# In your data, Time period and Number of Sales are:
time_periods = ['Q1', 'Q2', 'Q3', 'Q4']
eco_friendly_products = [50, 45, 58, 52]
conventional_products = [60, 62, 55, 48]

# Creating the stairs plot
plt.step(time_periods, eco_friendly_products, label='Eco-Friendly Products')
plt.step(time_periods, conventional_products, label='Conventional Products')

# Adding legend to distinguish the lines
plt.legend(loc='best')

# Adding title and labels for the axes
plt.title('Sales Performance Comparison')
plt.xlabel('Quarters')
plt.ylabel('Sales Volume (in thousands)')

# Updating the label of the steps that contain the center point of the bounding box to 'A new Label'
plt.gca().get_xticklabels()[1].set_text('A new Label')

# Adjusting the marker size for those same steps to 11.43
plt.gca().get_xticklabels()[1].set_markersize(11.43)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")