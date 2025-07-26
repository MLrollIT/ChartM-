import matplotlib.pyplot as plt
import numpy as np

# data
altitude_intervals = np.array([7.5, 17.5, 27.5, 37.5, 47.5, 57.5])
fruit_specimens = np.array([8, 12, 18, 21, 15, 9])

# plot
plt.figure(figsize=(8,6))
plt.hist(altitude_intervals, weights=fruit_specimens, bins=6, alpha=0.5, color='green', edgecolor='black')

# labels
plt.xlabel('Altitude Intervals (m)', fontsize=14)
plt.ylabel('Number of Fruit Specimens', fontsize=14)
plt.title('Vertical Dispersion of Various Fruits in the Rainforest Canopy', fontsize=16)

plt.grid(True)
plt.tight_layout()
plt.savefig("figure.png")

# add text label
plt.text(15, 10, 'A new Label', fontsize=12, color='black')
plt.savefig("Edit_figure.png")