import matplotlib.pyplot as plt
import numpy as np

# Data points for breed categories and frequencies
breeds = ["Siamese", "Persian", "Maine Coon", "Bengal", "Sphynx"]
weight_categories = ["2", "4", "6", "8", "10"]
frequencies = np.array([
    [10, 15, 8, 5, 2],
    [5, 20, 12, 10, 3],
    [2, 8, 10, 15, 6],
    [9, 12, 10, 7, 4],
    [4, 6, 7, 10, 12]
])

x = np.arange(len(weight_categories))
width = 0.15

fig, ax = plt.subplots()
for i in range(len(breeds)):
    rects = ax.bar(x - 2*width + i*width, frequencies[i], width, label=breeds[i], edgecolor='black', linewidth=2, alpha=0.5, hatch='//', facecolor='none')

ax.set_ylabel('Number of Cats')
ax.set_xlabel('Weight (pounds)')
ax.set_title('Weight Distribution of Cats by Breed')
ax.set_xticks(x)
ax.set_xticklabels(weight_categories)
ax.legend()

fig.tight_layout()

plt.tight_layout()
plt.savefig("figure.png")