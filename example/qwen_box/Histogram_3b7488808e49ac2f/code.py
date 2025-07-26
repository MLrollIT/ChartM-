import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Given data
elevation_ranges = ['1000-1100', '1100-1200', '1200-1300', '1300-1400', '1400-1500', '1500-1600', '1600-1700', '1700-1800']
frequency_samples = [12, 18, 25, 30, 28, 20, 15, 10]

# Creating the histogram
plt.figure(figsize=(10,6)) # To make sure the labels are readable
plt.bar(elevation_ranges, frequency_samples, color='green', alpha=0.7)

# Let's set up titles and labels
plt.title('Alien Planet Terrain Elevation Analysis')
plt.xlabel('Elevation Ranges (in meters)')
plt.ylabel('Frequency of Terrain Samples')

# Displaying the histogram
plt.tight_layout()
plt.savefig("figure.png")

# Add a shadow effect to the bars that contain the center point of the bounding box
bbox = (1300, 1400)  # Center point of the bounding box
shadow_color = 'gray'
shadow_offset = (2.97, 3.56)  # Offset for the shadow

# Get the bar objects
bars = plt.gca().patches

# Find the bar that contains the center point of the bounding box
for bar in bars:
    if bar.get_bbox().center() == bbox:
        bar.set_facecolor('none')  # Remove the face color
        bar.set_edgecolor(shadow_color)  # Set the edge color
        bar.set_linewidth(2)  # Set the linewidth
        bar.set_zorder(2)  # Set the z-order to ensure it's on top
        break

# Enable the animated state for these bars
for bar in bars:
    if bar.get_bbox().center() == bbox:
        bar.set_animated(True)

plt.tight_layout()
plt.savefig("Edit_figure.png")