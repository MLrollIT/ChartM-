import matplotlib.pyplot as plt

# years from 2010 to 2020
years = list(range(2010, 2021))

# average lifetimes data 
green_turtles = [75, 70, 78, 80, 72, 76, 74, 77, 75, 79, 71]
loggerhead_turtles = [63, 61, 58, 64, 61, 59, 62, 65, 60, 63, 58]
hawksbill_turtles = [55, 57, 54, 52, 56, 53, 50, 51, 55, 52, 48]
leatherback_turtles = [90, 88, 87, 85, 89, 92, 86, 91, 88, 84, 90]
olive_ridley_turtles = [50, 47, 48, 51, 49, 52, 46, 50, 47, 49, 45]

# plot the data using stackplot function
plt.stackplot(years, green_turtles, loggerhead_turtles, hawksbill_turtles, 
              leatherback_turtles, olive_ridley_turtles, 
              labels=['Green Turtles - Atlantic Ocean','Loggerhead Turtles - Pacific Ocean',
                      'Hawksbill Turtles - Indian Ocean','Leatherback Turtles - Southern Ocean',
                      'Olive Ridley Turtles - Mediterranean Sea'])

# labels for x and y axis
plt.xlabel('Years')
plt.ylabel('Average Lifetimes')

# title of the plot
plt.title('Average Lifetimes of Different Species of Sea Turtles in Various Oceans (2010-2020)')

# legend in the upper left corner
plt.legend(loc='upper left')

# modify the face color of the area that contains the center point of the bounding box to #731665, and update the edge color in that area to #8bf473
bbox = plt.gca().get_position().get_points()
bbox[0] = 0.5
bbox[1] = 0.5
bbox[2] = 0.5
bbox[3] = 0.5
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], facecolor='#731665', edgecolor='#8bf473'))

# show the plot
plt.tight_layout()
plt.savefig("figure.png")