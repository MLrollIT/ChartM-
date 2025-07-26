from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
vehicle_type = ["Sedans", "SUVs", "Electric Vehicles", "Trucks", "Motorcycles", "Hybrids"]
years = ["2016", "2017", "2018", "2019", "2020"]

sales = np.array([[4000, 8000, 6000, 7000, 9000],
                  [3000, 3000, 6000, 5000, 8000],
                  [1000, 5000, 2000, 2500, 5000],
                  [2500, 2000, 3000, 2000, 1000],
                  [5000, 4000, 6000, 8000, 7000],
                  [2000, 3000, 7000, 5000, 6000]])

fig, ax = plt.subplots()
im = ax.imshow(sales, cmap='viridis', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)), labels=years)
ax.set_yticks(np.arange(len(vehicle_type)), labels=vehicle_type)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vehicle_type)):
    for j in range(len(years)):
        text = ax.text(j, i, sales[i, j], ha="center", va="center", color="w", fontsize=16)

# Adding grid, title and setting light blue face color
ax.grid(True)
ax.set_facecolor('#add8e6')  # Modify the face color here
ax.set_title("Sales of Vehicles from 2016 to 2020")
ax.set_xlabel("Years")
ax.set_ylabel("Vehicle Type")

fig.tight_layout()
plt.savefig("myplot.png")