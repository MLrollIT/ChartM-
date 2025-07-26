import matplotlib.pyplot as plt
import numpy as np

# x: Luminosity levels ranges, y: Frequencies
x = ['100-150', '151-200', '201-250', '251-300', '301-350']
y = [5, 12, 8, 4, 3]

# Convert the x ranges to midpoints for better representation on histogram
x_midpoints = [(int(range.split('-')[0]) + int(range.split('-')[1])) / 2 for range in x]
x_tick_locations = np.arange(len(x))

# Creating the histogram
plt.bar(x_tick_locations, y, align='center')

# Setting x-ticks to represent ranges
plt.xticks(x_tick_locations, x)

# Labels and title
plt.xlabel('Luminosity Level Ranges')
plt.ylabel('Frequency of Luminosity Observations')
plt.title('Histogram of Firework Display Luminosity in Different Galaxies')

# Modify the histogram by adding a stroke to the bars that contain the center point of the bounding box
bbox = plt.gca().get_position()
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt