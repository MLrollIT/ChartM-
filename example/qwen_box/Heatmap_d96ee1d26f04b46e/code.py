from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

Exercise_Types = ["Yoga", "Weightlifting", "Running", "Cycling", "Swimming"]
Popularity = np.array([15, 35, 20, 40, 25])

fig, ax = plt.subplots()
im = ax.imshow(Popularity.reshape(1,5), cmap='viridis', alpha=0.7)  # Changed colormap to 'viridis'

ax.set_xticks(np.arange(len(Exercise_Types)))
ax.set_yticks([])

ax.set_xticklabels(Exercise_Types)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(Exercise_Types)):
    text = ax.text(i, 0, Popularity[i], ha="center", va="center", color="k")  # Changed text color to black

ax.set_title("Popularity of Different Exercise Types")
ax.set_xlabel("Exercise Types")
ax.set_ylabel("Popularity")
ax.grid(True)
ax.set_facecolor('lightgray')
fig.tight_layout()
plt.savefig("myplot.png")