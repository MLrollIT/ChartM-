import matplotlib.pyplot as plt
import numpy as np

#Given data
_longitude = np.array([0, 60, 120, 180, 240, 300, 360])
_density = np.array([8, 12, 10, 15, 20, 18, 6])

plt.figure(figsize=[10,6])

#Create a stair plot
plt.step(_longitude, _density, where='post')

#Labeling the Graph
plt.title("Spatial Distribution of Galactic Dust Clouds")
plt.xlabel("Galactic Longitude (in degrees)")
plt.ylabel("Density of Dust Clouds (in particles per cubic parsec)")

plt.xlim([0, 360])
plt.ylim([0, max(_density)+5])

plt.grid(True)

# Change the clipping state of the lines that contain the center point of the bounding box to False
plt.gca().set_clip_on(False)

# Set the linewidth of these lines to 3.83
plt.gca().lines[2].set_linewidth(3.83)

plt.tight_layout()
plt.savefig("Edit_figure.png")