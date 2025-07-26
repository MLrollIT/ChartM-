from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

decades = ["1960", "1970", "1980", "1990", "2000", "2010", "2020", "2030"]
scores = np.array([20, 25, 40, 35, 60, 65, 90, 30])

fig, ax = plt.subplots()
im = ax.imshow(scores.reshape(1,8), cmap='viridis', alpha=0.7)

ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(scores)):
    text = ax.text(i, 0, scores[i], ha="center", va="center", color="w")

ax.set_title("Fashion Trend Score by Decades")
ax.set_xlabel("Decades")
ax.set_ylabel("Scores")

ax.grid(True)
ax.set_facecolor('lightgray')

fig.tight_layout()
plt.savefig("myplot.png")