# import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# established data
birth_weights = [2050, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950]
frequencies = [5, 12, 8, 15, 10, 3, 6, 2, 5, 1]

# repeats each weight by its frequency to simulate the dataset
data = np.repeat(birth_weights, frequencies)

# create histogram
plt.figure(figsize=(10,6))
plt.hist(data, bins=np.arange(2000, 3000, 100), edgecolor = 'black')

# add labels and title
plt.xlabel('Birth weight (grams)')
plt.ylabel('Number of newborns')
plt.title('Distribution of Neonatal Birth Weights')

# make x-axis readable
plt.xticks(np.arange(2000, 3000, 100))

# add shadow below the bars that contain the center point of the bounding box
bbox = (2300, 2400, 2500, 2600)
plt.bar([bbox[0]], [bbox[1]], color='black', edgecolor='black', linewidth=2.6, hatch='/', bottom=bbox[2], alpha=0.5)

# add shadow below the bars that contain the center point of the bounding box
bbox = (2300, 2400, 2500, 2600)
plt.bar([bbox[0]], [bbox[1]], color='black', edgecolor='black', linewidth=2.6, hatch='/', bottom=bbox[2], alpha=0.5)

# make x-axis readable
plt.xticks(np.arange(2000, 3000, 100))

plt.tight_layout()
plt.savefig("figure.png")