from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

travel_types = ["Car Travel", "Train Travel", "Bus Travel", "Air Travel", "Bike Travel", "Boat Travel", "Foot Travel", "Camel Travel", "Horse Travel"]
popularity_scores = np.array([5, 15, 7, 30, 9, 20, 3, 8, 12])

fig, ax = plt.subplots(figsize=(10,6))
im = ax.imshow(popularity_scores.reshape(1,9), cmap='hot', alpha=0.7)

ax.set_xticks(np.arange(len(travel_types)), labels=travel_types)
ax.set_yticks([])

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(travel_types)):
    text = ax.text(i, 0, popularity_scores[i], ha="center", va="center", color="white", fontsize=12, edgecolor="#e08666")

ax.set_title("Popularity of different types of travel")
ax.set_xlabel("Travel type")
ax.set_ylabel("Popularity score")
ax.grid(True)
ax.set_facecolor('gray')

fig.tight_layout()
plt.savefig("myplot.png")