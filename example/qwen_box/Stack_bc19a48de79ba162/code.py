import matplotlib.pyplot as plt

# Academic years
years = [1, 2, 3, 4, 5, 6, 7]

gryffindor = [5000, 7000, 6000, 8000, 9000, 7500, 6500]
hufflepuff = [3000, 4500, 3500, 5500, 4000, 5000, 4200]
ravenclaw = [4000, 5500, 4800, 6000, 7000, 5900, 6300]
slytherin = [2000, 3000, 2500, 4000, 3500, 3200, 3800]

# Create the stack plot
plt.stackplot(years, gryffindor, hufflepuff, ravenclaw, slytherin, colors=["r", "y", "b", "g"])

# Adding legend
plt.legend(["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"], loc="upper left")

plt.xlabel("Academic Years")
plt.ylabel("Amount of Magical Ingredients Consumed (in grams)")

plt.title("Magical ingredient consumption of different houses over the years")


plt.tight_layout()
plt.savefig("figure.png")