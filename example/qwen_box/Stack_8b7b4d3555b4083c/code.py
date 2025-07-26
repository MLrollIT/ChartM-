import matplotlib.pyplot as plt

# X-axis Cities
cities = ['City 1', 'City 2', 'City 3']

# Y-axis Temperature
north_hem = [-2, 0, -5]  # As all temperatures are negative
south_hem = [25, 20, 15] 

# Since there are negative values in North Hemisphere and stack plot doesn't allow negative values, let's convert to positive for visualization
north_hem_positive = [abs(temp) for temp in north_hem]

# Stacked plot 
fig, ax = plt.subplots()

ax.stackplot(cities, north_hem_positive, south_hem, labels=['Northern Hemisphere','Southern Hemisphere'], colors = ['skyblue', 'coral'])
plt.legend(loc='upper left')

plt.xlabel("Cities")
plt.ylabel("Average Winter Temperature (°C)") 
plt.title("Weather Patterns in Different Hemisphere Winters")


# Adjust the transparency of the filled area that contains the center point of the bounding box to 0.3068
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((0.5, 0.5), fig)
bbox = ax.bbox_to_anchor((