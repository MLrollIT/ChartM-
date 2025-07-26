from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

property_types = ["Residential", "Commercial", "Industrial"]
years = ["2018", "2019", "2020"]

property_values = np.array([[150000, 120000, 185000],
                            [200000, 210000, 145000],
                            [180000, 225000, 215000]])

fig, ax = plt.subplots()
im = ax.imshow(property_values, cmap='viridis', alpha=0.6)

ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)

ax.set_yticks(np.arange(len(property_types)))
ax.set_yticklabels(property_types)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(property_types)):
    for j in range(len(years)):
        text = ax.text(j, i, property_values[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Property Values by Type and Year")
ax.set_xlabel("Year")
ax.set_ylabel("Property Type")

ax.grid(True)
ax.set_facecolor('lightgray')

fig.tight_layout()
plt.savefig("myplot.png")