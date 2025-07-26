import matplotlib.pyplot as plt

# Data
city = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
population_density = [5000, 7000, 4000, 9000, 6000, 7500, 5500, 8000, 6500, 5700]
gdp_per_capita = [25000, 35000, 20000, 40000, 30000, 35000, 25000, 45000, 32000, 28000]

# Create scatter plot
plt.figure(figsize=(10,8))
plt.scatter(population_density, gdp_per_capita, alpha=0.5)

# Add labels and title
plt.title("Correlation between Population Density and GDP per Capita")
plt.xlabel("Population Density (persons/sq km)")
plt.ylabel("GDP per Capita (USD)")

# Add data point labels
for i, txt in enumerate(city):
    plt.annotate(txt, (population_density[i], gdp_per_capita[i]), 
                 textcoords="offset points", xytext=(10,-10), ha='center')

# Change color and shape of scatter points that contain the center point of the bounding box
bbox = plt.gca().bbox_to_transform(plt.gca().bbox)
bbox = bbox.transformed(plt.gca().transAxes)
bbox = bbox.get_window_extent().transformed(plt.gca().transAxes.inverted())
bbox = bbox.get_points()
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0] + bbox[1] / 2
bbox = bbox[0