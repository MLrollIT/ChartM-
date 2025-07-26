import matplotlib.pyplot as plt

# Days
days = [1, 2, 3, 4, 5, 6, 7]

# Facebook activity level
facebook_activity = [60, 72, 80, 55, 90, 63, 70]

# Reported anxiety level
anxiety_level = [4, 5, 6, 3, 7, 4, 5]

# Plot stack plot
plt.stackplot(days, facebook_activity, anxiety_level, colors=['blue', 'green'], labels=['Facebook Activity', 'Anxiety Level'])

plt.legend(loc='upper left')

plt.title('Facebook Activity and Anxiety Level Over Time')
plt.xlabel('Day')
plt.ylabel('Minutes/Level')

# Set the z-order of the filled areas that contain the center point of the bounding box to 14
bbox = plt.gca().bbox
bbox_points = bbox.get_points()
bbox_points[4][0] = 4.5
bbox_points[4][1] = 75
bbox_points[5][0] = 5.5
bbox_points[5][1] = 90
bbox.set_points(bbox_points)

# Update the edge's linestyle to 'dashdot' and change the color to #73e97e
bbox.set_edgecolor('#73e97e')
bbox.set_linestyle('dashdot')

plt.tight_layout()
plt.savefig("figure.png")