import matplotlib.pyplot as plt

# Define data
locations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
heights = [0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 2.3, 2.6, 2.9]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot data
ax.scatter(locations, heights)

# Set the title and labels for the plot
ax.set_title('Growth Patterns of Alien Plants on Exoplanet')
ax.set_xlabel('Terrain Locations')
ax.set_ylabel('Plant Heights (in meters)')

# Modify the size and shape of the scatter points that contain the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox_points = ax.get_children()[1].get_children()[1].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children()[0].get_children