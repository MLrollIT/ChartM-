import matplotlib.pyplot as plt

# Depth measurements in meters
point_A_depths = [200, 250, 300, 275, 320]
point_B_depths = [150, 180, 200, 210, 190]
point_C_depths = [300, 320, 350, 330, 310]
point_D_depths = [180, 200, 220, 210, 190]
point_E_depths = [250, 280, 300, 290, 270]

# The order of the depth measurements
depth_order = range(1, len(point_A_depths) + 1)

# Create a new figure
plt.figure()

# Create a stack plot
plt.stackplot(depth_order, point_A_depths, point_B_depths, point_C_depths, point_D_depths, point_E_depths,
              labels=['Point A', 'Point B', 'Point C', 'Point D', 'Point E'])

# Set the title and labels
plt.title("Ocean Depth Soundings along Marine Research Expedition")
plt.xlabel("Order of Depth Measurements")
plt.ylabel("Ocean Depths (meters)")

# Add a legend
plt.legend(loc='upper left')

# Set the linestyle of the area that contains the center point of the bounding box to 'dashdot' and color to 'yellow'
bbox = plt.gca().get_position().get_points()
bbox[1] = [bbox[1][0], 800]
bbox[2] = [bbox[2][0], 800]
plt.gca().add_patch(plt.Rectangle((bbox[0][0], bbox[0][1]), bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1],
                                   fill=False, linestyle='dashdot', color='yellow', rasterized=True))

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")