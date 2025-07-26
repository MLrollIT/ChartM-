from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Data
vehicle_types = ["Sedans", "SUVs", "Electric Vehicles", "Trucks"]
years = ["2010", "2015", "2020"]
sales = np.array([[50000, 60000, 35000],
                  [40000, 35000, 70000],
                  [500, 1500, 5000],
                  [70000, 65000, 67000]])

# Create Figure and Axes instances
fig, ax = plt.subplots()

# Display the image
im = ax.imshow(sales, cmap='viridis', alpha=0.7)

# Configure axes
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(vehicle_types)))
ax.set_xticklabels(years)
ax.set_yticklabels(vehicle_types)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Annotate the values
for i in range(len(vehicle_types)):
    for j in range(len(years)):
        text = ax.text(j, i, sales[i, j], ha="center", va="center", color="w")

# Set the title and labels
ax.set_title("Vehicle Sales over Time")
ax.set_xlabel("Year")
ax.set_ylabel("Vehicle Type")

# Set background color and disable grid
ax.set_facecolor('lightblue')  # Change background color to light blue
ax.grid(False)  # Disable grids

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")