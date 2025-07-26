from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

species = ["Tuna", "Shark", "Cod", "Salmon", "Herring"]
years = ["2000", "2005", "2010", "2015"]

catches = np.array([[500000, 400000, 350000, 250000],
                    [400000, 300000, 350000, 200000],
                    [350000, 300000, 250000, 150000],
                    [500000, 550000, 500000, 450000],
                    [400000, 350000, 325000, 300000]])

fig, ax = plt.subplots()

im = ax.imshow(catches, alpha=0.7, cmap='RdYlBu')

ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(species)))

ax.set_xticklabels(years)
ax.set_yticklabels(species)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(species)):
    for j in range(len(years)):
        text = ax.text(j, i, catches[i, j],
                       ha="center", va="center", color="w", fontsize=14, fontweight="bold", fontstyle="italic", bbox=dict(boxstyle="square", ec=(1, 1, 1), fc=(1, 1, 1), lw=2.5, alpha=0.5, fill=True, edgecolor="#f1b103"))

ax.set_title("Catch of Sea Species over the years")
ax.set_xlabel('Years')
ax.set_ylabel('Species')

ax.grid(True)
ax.set_facecolor('lightgray')

fig.tight_layout()
plt.savefig("myplot.png")