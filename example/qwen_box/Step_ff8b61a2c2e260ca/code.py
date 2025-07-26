import matplotlib.pyplot as plt
import numpy as np

# Declaring the data in lists
planets = ['Planet A', 'Planet B', 'Planet C', 'Planet D', 'Planet E']
species_x = [1000, 800, 2000, 1500, 300]
species_y = [5000, 3000, 1000, 200, 4000]
species_z = [200, 1000, 500, 8000, 700]

# Creating subplots
fig, ax = plt.subplots()

# Setting line sequences and plotting
ax.step(planets, species_x, where='mid', label='Species X')
ax.step(planets, species_y, where='mid',label='Species Y')
ax.step(planets, species_z, where='mid',label='Species Z')

# Adding some extra space to the y-axis for readablity
ymax = max(max(species_x), max(species_y), max(species_z)) + 500
plt.ylim(0, ymax)

# Defining labels, title and grid
plt.xlabel('Planets')
plt.ylabel('Estimated population numbers')
plt.title('Estimated populations of different types of extraterrestrial life forms')

# Adding a legend
ax.legend()

# Overlaying a dashed line on the portion of the step chart that contains the center point of the bounding box
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox = ax.bbox_to_anchor((0.5, 0.5), transform=ax.transAxes)
bbox =