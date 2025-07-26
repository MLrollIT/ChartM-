import matplotlib.pyplot as plt

# Sleep Quality Levels
quality_levels = ['Poor', 'Fair', 'Good', 'Excellent']

# Daily Caffeine Consumption
low_consumption = [10, 20, 30, 15]  # Low
moderate_consumption = [15, 25, 40, 20] # Moderate
high_consumption = [5, 15, 25, 10]  # High

# Define the colors for different consumption levels 
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

# Create the stackplot
plt.figure(figsize=(10, 7))
plt.stackplot(quality_levels, low_consumption, moderate_consumption, high_consumption, labels=['Low','Moderate','High'], colors=colors)

# Define labels and title
plt.xlabel('Sleep Quality Level')
plt.ylabel('Number of Students')
plt.title('Sleep Quality and Daily Caffeine Consumption among College students')

# Display the legend
plt.legend(loc='upper left')

# Set animated state of the areas that contain the center point of the bounding box to True
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.3
bbox[1] = 0.3
bbox[2] = 0.5
bbox[3] = 0.5
plt.gca().set_position(bbox)

# Ensure that the clipping state for these areas is set to True as well
plt.gca().set_clip_path(bbox_to_image(plt.gca().get_position().get_points()))

plt.tight_layout()
plt.savefig("figure.png")