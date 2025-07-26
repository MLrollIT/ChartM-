from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Data
furniture_type = ["Sofa", "Coffee Table", "Dining Table", "Bed"]
sales = [
    [100, 120, 150, 200, 250, 150, 90, 80, 70, 60, 200, 300],
    [50, 60, 70, 60, 50, 40, 30, 20, 25, 30, 35, 40],
    [300, 350, 400, 200, 150, 100, 80, 250, 270, 275, 280, 285],
    [140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 600, 500]
]
months = list(range(1, 13))

# Plotting
fig, ax = plt.subplots()
linestyles = ['-', '--', '-.', ':']
colors = ['red', 'green', 'blue', 'orange']

for i, furniture in enumerate(furniture_type):
    ax.plot(months, sales[i], linestyle=linestyles[i], color=colors[i], 
            marker='o', markersize=6, linewidth=1.5, alpha=0.7, label=furniture)
    ax.annotate(furniture, (months[-1], sales[i][-1]), textcoords="offset points", 
                xytext=(10,10), ha='center', fontsize=8, color=colors[i])

ax.set_facecolor('white')  # Changed background color to white
ax.grid(False)  # Removed the grid
ax.set_title('Monthly Sales of Furniture')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.legend()

plt.tight_layout()
plt.savefig('myplot.png')