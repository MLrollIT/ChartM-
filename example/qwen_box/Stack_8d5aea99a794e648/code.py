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

# hide the edge around the filled area that contains the center point of the bounding box
plt.gca().patch.set_edgecolor("none")
plt.gca().patch.set_alpha(0.3536)

plt.savefig("figure.png")