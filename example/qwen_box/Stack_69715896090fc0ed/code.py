import matplotlib.pyplot as plt

# Define the distance in kilometers
distance = [0, 10, 20, 30, 40, 50, 60]

# Define the height of ash dispersed in meters for each eruption
eruption1 = [200, 150, 120, 80, 40, 20, 10]
eruption2 = [250, 200, 180, 140, 100, 50, 30]
eruption3 = [180, 160, 130, 100, 70, 40, 20]

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Create a stack plot for the ash dispersed data
ax.stackplot(distance, eruption1, eruption2, eruption3, labels=['Eruption 1', 'Eruption 2', 'Eruption 3'])

# Set the title for the stack plot
ax.set_title('Ash Dispersion from Explosive Volcanic Eruptions')

# Set the label for X-axis and Y-axis
ax.set_xlabel('Distance from the Volcano (km)')
ax.set_ylabel('Height of Ash Dispersion (m)')

# Create a legend for the stack plot
ax.legend(loc='upper right')

# Adjust the z-order of the area that contains the center point of the bounding box to 1
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5, transform=ax.transAxes)
bbox = ax.bbox_to_anchor(0.5, 0.5