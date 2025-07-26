import matplotlib.pyplot as plt  #import matplotlib library

# Define the data
elevation = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
biodiversity = [35, 45, 55, 60, 50, 40, 30, 25, 20, 15]

# Create a scatter plot
plt.scatter(elevation, biodiversity, color='g', label='Data points')

# Add labels and title
plt.xlabel('Elevation (meters)')
plt.ylabel('Biodiversity Richness (species count)')
plt.title('Biodiversity Richness in Tropical Rainforests at Different Elevations')

# Show a legend
plt.legend()

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")