import matplotlib.pyplot as plt

# Define the data for the plot
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
depth_0_200 = [20, 22, 19, 18]
depth_200_500 = [15, 17, 14, 13]
depth_500_1000 = [10, 12, 9, 8]
depth_1000_2000 = [5, 7, 4, 3]
depth_2000_4000 = [3, 4, 2, 1]

# Create the stackplot
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(seasons, depth_0_200, depth_200_500, depth_500_1000, depth_1000_2000, depth_2000_4000, labels=['0-200m','200-500m','500-1000m','1000-2000m','2000-4000m'])
ax.legend(loc='upper left')
ax.set_title('Seasonal variations in ocean temperature across different depths in the Pacific Ocean')
ax.set_xlabel('Seasons')
ax.set_ylabel('Temperature (°C)')

# Set the transparency of the areas that contain the center point of the bounding box to 0.97
bbox = ax.bbox_to_anchor((0.5, 0.5), fig=fig)
bbox_points = bbox.get_points()
bbox_points[0] = (bbox_points[0][0], 0.97)
bbox_points[1] = (bbox_points[1][0], 0.97)
bbox.set_points(bbox_points)

# Set the snap state to False for those same areas
bbox.set_snap(False)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")