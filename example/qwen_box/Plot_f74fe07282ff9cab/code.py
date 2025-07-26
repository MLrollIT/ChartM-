from io import StringIO
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [2012, 1000, 1100, 1200],
    [2013, 1200, 1300, 1000],
    [2014, 1500, 2100, 1300],
    [2015, 2000, 1700, 1400],
    [2016, 2500, 2300, 1500],
    [2017, 3000, 2500, 1100],
    [2018, 2900, 2700, 1800],
    [2019, 3100, 2900, 2000],
    [2020, 3150, 3100, 2100]
])

fig, ax = plt.subplots(facecolor='white')  # Change background color to white

ax.plot(data[:, 0], data[:, 1], label="Organic Vegetables", color="red", linewidth=2, linestyle='-', marker='o', markersize=8, alpha=0.8)
ax.plot(data[:, 0], data[:, 2], label="Organic Fruits", color="green", linewidth=2, linestyle='--', marker='v', markersize=8, alpha=0.8)
ax.plot(data[:, 0], data[:, 3], label="Organic Grains", color="blue", linewidth=2, linestyle='-.', marker='^', markersize=8, alpha=0.8)

for i in range(1, 4):
    for x, y in zip(data[:, 0], data[:, i]):
        ax.text(x, y, str(y))

ax.set_title('Organic Products Evolution')
ax.set_xlabel('Year')
ax.set_ylabel('Quantity')
ax.legend(loc='upper left', shadow=True)

ax.grid(True, color='lightgray')  # Set gridlines to light gray
plt.tight_layout()
plt.savefig("myplot.png")