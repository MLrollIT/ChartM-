from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

art_types = ["Sculpture", "Painting", "Photography", "Digital Art", "Conceptual Art", "Performance Art"]
popularity_index = np.array([45, 60, 20, 70, 15, 30])

fig, ax = plt.subplots()
im = ax.imshow(popularity_index.reshape(1, -1), cmap='hot', alpha=0.8)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(art_types)), labels=art_types)
ax.set_yticks([])

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(art_types)):
    text = ax.text(i, 0, popularity_index[i], ha="center", va="center", color="w")

ax.set_title("Popularity Index of Different Art Types")
ax.set_xlabel("Art Types")
ax.set_ylabel("Popularity Index")
ax.grid(True)
ax.set_facecolor('lightgray')

fig.tight_layout()
plt.savefig("myplot.png")