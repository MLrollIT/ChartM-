from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

professions = ["Software Engineers", "Actors", "Doctors", "Teachers", "Farmers", "Chefs", "Mechanics", "Lawyers", "Artists"]
scores = np.array([56, 89, 67, 102, 73, 85, 92, 75, 66])

fig, ax = plt.subplots()
im = ax.imshow(scores.reshape(1,9), cmap='viridis', alpha=0.7)

# Set the face and edge color to light gray
fig.patch.set_facecolor('#f0f0f0')
ax.set_facecolor('#f0f0f0')

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(professions)))
ax.set_yticks([])

ax.set_xticklabels(professions)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
ax.set_title("Dietary Score among Different Professions")
ax.set_xlabel('Professions')
ax.set_ylabel('Dietary Score')

# Add a colorbar
cbar = fig.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Dietary Score', rotation=-90, va="bottom")

# Loop over data dimensions and create text annotations.
for i in range(len(scores)):
    text = ax.text(i, 0, scores[i], ha="center", va="center", color="w")

ax.grid(True)
plt.tight_layout()
plt.savefig("myplot.png")