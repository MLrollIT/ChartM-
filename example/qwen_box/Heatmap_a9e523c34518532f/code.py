from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]
vehicle_types = ["Compact Cars", "SUVs", "Trucks"]

sales = np.array([[1000, 1200, 1400],
                  [1200, 1100, 1300],
                  [1400, 1000, 1200],
                  [1600, 1400, 1100],
                  [1800, 1600, 1000],
                  [2000, 1800, 1300],
                  [1600, 2000, 1500],
                  [1700, 1500, 1600],
                  [1900, 1300, 1400]])

fig, ax = plt.subplots()
im = ax.imshow(sales, cmap='hot', alpha=0.7)

ax.set_xticks(np.arange(len(vehicle_types)))
ax.set_yticks(np.arange(len(years)))
ax.set_xticklabels(vehicle_types)
ax.set_yticklabels(years)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(years)):
    for j in range(len(vehicle_types)):
        if i == 4 and j == 1:
            text = ax.text(j, i, sales[i, j],
                           ha="center", va="center", color="w", fontsize=8)
        else:
            text = ax.text(j, i, sales[i, j],
                           ha="center", va="center", color="w")

ax.set_title("Sales of Different Vehicle Types (in units/year)")
ax.set_xlabel('Vehicle Type')
ax.set_ylabel('Year')
ax.grid(True)
ax.set_facecolor('gray')
fig.tight_layout()
plt.savefig("myplot.png")