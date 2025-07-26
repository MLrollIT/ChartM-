import matplotlib.pyplot as plt

# Seasons
seasons = ["Spring", "Summer", "Fall", "Winter"]

# Temperature data for each coral reef
great_barrier_reef = [28, 30, 29, 27]
caribbean_coral_reef = [29, 31, 30, 28]
red_sea_coral_reef = [30, 32, 31, 29]

# Plotting data
plt.stackplot(seasons, great_barrier_reef, caribbean_coral_reef, red_sea_coral_reef, labels=['Great Barrier Reef','Caribbean Coral Reef','Red Sea Coral Reef'])

# Adding labels and title
plt.xlabel("Seasons")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variability in Coral Reef Ecosystems")

# Adding legend
plt.legend(loc='upper left')

# Adding bounding box
bbox = plt.Rectangle((0.25, 0.5), 0.2, 0.2, fill=False, edgecolor='black', linewidth=2)
plt.gca().add_patch(bbox)

# Adding center point
center_point = plt.Circle((0.25 + 0.2 / 2, 0.5 + 0.2 / 2), 0.05, fill=False, edgecolor='black', linewidth=2)
plt.gca().add_artist(center_point)

# Changing color and z-order of center point area
plt.gca().patch.set_facecolor('#93e3af')
plt.gca().patch.set_zorder(18)

# Adding shadow effect to center point area
plt.gca().patch.set_facecolor('gray')
plt.gca().patch.set_edgecolor('gray')
plt.gca().patch.set_zorder(18)

# Displaying plot
plt.tight_layout()
plt.savefig("figure.png")