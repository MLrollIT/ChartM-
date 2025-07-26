from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    "Category": ["Baking", "Grilling", "Roasting", "Stir-frying", "Steaming", "Deep-frying", "Boiling", "Sautéing", "Poaching"],
    "2016": [50, 70, 85, 30, 60, 80, 75, 55, 40],
    "2017": [60, 60, 100, 25, 65, 75, 70, 60, 45],
    "2018": [40, 75, 90, 45, 64, 85, 68, 55, 50]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

x = np.arange(len(df["Category"]))

color_palette = ['blue', 'green', 'red']  # Defined color palette
linestyles = ['-', '--', '-.', ':']

for i in range(1, df.shape[1]):
    line, = ax.plot(x, df.iloc[:, i], marker='x', linestyle=linestyles[i % len(linestyles)], linewidth=2, markersize=6, label=df.columns[i], color=color_palette[i % len(color_palette)])  # Set line color from palette
    for j in range(len(x)):
        ax.text(j, df.iloc[j, i], df.columns[i], ha='center')

ax.set_xlabel('Category')
ax.set_ylabel('Values')
ax.set_title('Cooking Method Popularity by Year')
ax.legend(loc='upper right', shadow=True)
ax.set_xticks(x)
ax.set_xticklabels(df["Category"], rotation=45)
ax.grid(True, color='lightblue')  # Change grid color to light blue
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")