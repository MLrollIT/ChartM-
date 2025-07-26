import matplotlib.pyplot as plt

# number of days
days = range(1, 31)

# coffee consumption data
coffee = [3, 2, 4, 2, 3, 4, 5, 3, 2, 4, 2, 3, 4, 5, 3, 2, 4, 2, 3, 4, 5, 3, 2, 4, 2, 3, 4, 5, 3, 2]

# productivity levels data
productivity = [5, 4, 7, 3, 6, 7, 8, 6, 4, 7, 3, 5, 7, 8, 6, 4, 7, 3, 5, 7, 8, 6, 4, 7, 3, 5, 7, 8, 6, 4]

# create the stackplot
plt.stackplot(days, coffee, productivity, labels=['Coffee', 'Productivity'], colors=['#ff7f0e', '#1f77b4'])

plt.legend(loc='upper left')

plt.title("Coffee Consumption vs Productivity")
plt.xlabel("Days")
plt.ylabel("Number of Cups/ Productivity Level")

plt.tight_layout()

# Set the animated state of the area that contains the center point of the bounding box to True
bbox = plt.gca().bbox_to_transform((0.5, 0.5))
plt.gca().set_animated(True)

# Add a stroke to the area with a linewidth of 4.78 and a foreground color of #01812a
plt.gca().add_patch(plt.Rectangle((0.5, 0.5), 0.01, 0.01, facecolor='none', edgecolor='#01812a', linewidth=4.78))

plt.tight_layout()
plt.savefig("figure.png")