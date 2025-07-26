import matplotlib.pyplot as plt

# Years from 1920 to 2020
years = list(range(1920, 2021, 10))

# Lists holding percentage of songs of each genre on charts for each year
jazz = [5, 12, 16, 8, 4, 2, 1, 2, 1, 2, 3]
blues = [3, 7, 10, 5, 3, 2, 1, 2, 1, 1, 1]
country = [2, 3, 8, 20, 18, 15, 10, 8, 6, 5, 4]
classical = [8, 5, 3, 2, 1, 1, 1, 4, 5, 8, 10]
pop = [1, 2, 5, 15, 25, 30, 40, 45, 50, 60, 70]

# Plotting
plt.figure(figsize=(10, 7))
plt.stackplot(years, jazz, blues, country, classical, pop, labels=['Jazz', 'Blues', 'Country', 'Classical', 'Pop'])

# Adding legend and labels
plt.legend(loc='upper left')
plt.xlabel('Years')
plt.ylabel('Percentage of Songs on Charts')
plt.title('Evolution of Music Genres 1920-2020')

# Displaying plot
plt.tight_layout()
plt.savefig("figure.png")

# Adjusting transparency and edge color of the area containing the center point of the bounding box
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.5
bbox[1] = 0.5
bbox[2] = 0.5
bbox[3] = 0.5
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], facecolor='0.316', edgecolor='#e5e49d', alpha=0.316))

plt.show()