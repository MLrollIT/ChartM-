import matplotlib.pyplot as plt

# data
coral_reef_m2 = [120, 150, 200, 180, 250, 220, 300, 280, 320, 350]
biodiversity_index = [3.2, 4.1, 2.8, 3.7, 4.6, 3.9, 5.2, 4.8, 5.5, 6.0]

# create scatter plot
plt.scatter(coral_reef_m2, biodiversity_index)

# title and labels
plt.title("Correlation between Coral Reef Coverage and Fish Biodiversity")
plt.xlabel("Coverage Area of Live Coral Reefs (m²)")
plt.ylabel("Biodiversity Index of Fish Species")

# show plot

plt.tight_layout()
plt.savefig("figure.png")