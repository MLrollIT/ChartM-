import matplotlib.pyplot as plt

# Data for drink preferences
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
beer = [40, 35, 45, 50, 30]
cocktails = [30, 35, 25, 20, 40]
wine = [15, 20, 10, 15, 15]
non_alcoholic = [15, 10, 20, 15, 15]

# Plotting
plt.figure(figsize=(10, 6))

plt.stackplot(weekdays, beer, cocktails, wine, non_alcoholic,
              labels=['Beer', 'Cocktails', 'Wine', 'Non-alcoholic'],
              colors=['gold', 'lightblue', 'lightgreen', 'coral'])

plt.xlabel('Weekdays')
plt.ylabel('Percentage')
plt.title('Happy Hour Drink Preferences')
plt.legend(loc='upper left')

# Adjust transparency of fill area containing the center point of the bounding box
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.5788
bbox[1] = 0.5788
plt.gca().set_position(bbox)

plt.tight_layout()
plt.savefig("figure.png")