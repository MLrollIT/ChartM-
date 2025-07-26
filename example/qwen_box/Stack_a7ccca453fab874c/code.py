import matplotlib.pyplot as plt
import numpy as np

# Initialize data
years = np.array(range(2010, 2020))
temperature = np.array([-20, -19, -18, -17, -16, -15, -14, -13, -12, -11])
species_a = np.array([50, 50, 49, 48, 47, 46, 45, 44, 43, 42])
species_b = np.array([80, 78, 75, 73, 70, 68, 65, 63, 60, 57])

# Create a figure and a set of subplots
fig, ax1 = plt.subplots()

# Plotting temperature
ax1.plot(years, temperature, color="black", label="Temperature")
ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature (°C)")
ax1.tick_params('y')

# Instantiate a second axes that shares the same x-axis
ax2 = ax1.twinx()

# Plotting populations
ax2.stackplot(years, [species_a, species_b], labels=['Species A', 'Species B'], alpha=0.6)
ax2.set_ylabel("Population (in thousands)")
ax2.tick_params('y')

# Adding a legend
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

# Show the plot
plt.tight_layout()

# Set the rasterized state of the areas that contain the center point of the bounding box to True
bbox = ax2.bbox_to_anchor((0.5, 0.5), fig)
bbox = bbox.transformed(fig.transFigure.inverted())
bbox = bbox.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
bbox = bbox.get_points()

# Apply a stroke to these areas with a line width of 3.84 and a foreground color of #66a1eb
for point in bbox:
    ax2.add_patch(plt.Rectangle(point, 0, 0, fill=False, edgecolor="#66a1eb", linewidth=3.84))

plt.savefig("figure.png")