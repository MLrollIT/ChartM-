import matplotlib.pyplot as plt

# Different agricultural techniques
agri_techniques = ['Traditional Farming', 'Hydroponics']

# Representing crop yield data
crop_yield = [2500, 4000]

# Resource consumption values
resource_consumption = [5000, 2000]

# Create a new figure and a subplots
fig, ax = plt.subplots()

# Create and display a Step plot for crop yield
ax.step(agri_techniques, crop_yield, where='post', label='Crop Yield')

# Create and display a Step plot for resource consumption
ax.step(agri_techniques, resource_consumption, where='post', label='Resource Consumption')

# Adding a legend
ax.legend()

# Label for x axis
plt.xlabel('Agricultural Techniques')

# Label for y axis
plt.ylabel('Crop Yield/Resource Consumption')

# Title for plot
plt.title('Comparison between Traditional Farming and Hydroponics')

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")

# Overlay a dashed step line on the section of the step chart that contains the center point of the bounding box to create a glow effect
ax.step([2500, 2500], [2500, 4000], where='mid', linestyle='--', color='#dcd2ab', alpha=0.5)