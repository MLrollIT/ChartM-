import matplotlib.pyplot as plt
import numpy as np

# Given data
x = ["400-425", "425-450", "450-475", "475-500", "500-525", "525-550", "550-575", "575-600", "600-625", "625-650"]
y = [15, 18, 22, 28, 32, 35, 30, 25, 20, 18]

# Generate the histogram
plt.bar(x, y, color='blue', alpha=0.7)

# Set the title and labels
plt.title('Colorful Interstellar Nebulae Formation Patterns')
plt.xlabel('Color Wavelength Ranges (in nanometers)')
plt.ylabel('Frequency of Color Wavelengths')

# Show the figure with homogeneously distributed color bars
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.savefig("figure.png")

# Set the animated state of the histogram that contains the center point of the bounding box to False, and also make the visibility of that histogram False.
bbox = plt.gca().get_window_extent().transformed(plt.gcf().get_transform())
bbox = bbox.transformed(plt.gcf().get_transform().inv)
bbox = bbox.get_points()
bbox = bbox[0]
bbox = bbox.tolist()
bbox[0] = 0.25
bbox[1] = 0.25
bbox[2] = 0.5
bbox[3] = 0.5
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], facecolor='none', edgecolor='black', animated=False))
plt.gca().get_children()[0].set_visible(False)