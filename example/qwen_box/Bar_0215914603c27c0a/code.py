from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

data = {
    "Year": np.array([1963, 1969, 1972, 1975, 1979, 1981, 1986, 1990, 1995]),
    "Space Technology": np.array([20, 100, 80, 85, 40, 50, 25, 30, 60]),
    "Space Exploration": np.array([20, 100, 80, 85, 40, 50, 25, 30, 60]),
}

fig, ax = plt.subplots()
width = 0.35

bars1 = ax.bar(data["Year"] - width/2, data["Space Technology"], width, label='Space Technology', color='b', edgecolor='black')
bars2 = ax.bar(data["Year"] + width/2, data["Space Exploration"], width, label='Space Exploration', color='g', edgecolor='black')

ax.set_title("Space Tech and Exploration Over the Years")
ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.legend(loc="upper left")
ax.grid(True)
ax.set_facecolor('lightgray')

ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)

plt.tight_layout()
plt.savefig("myplot.png")