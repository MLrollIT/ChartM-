from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Convert string data to list of integers
dust_mites = list(map(int, "15,17,13,16,20,18,15,20,17,25,12,15,13,18,17,20,16,19,17,16".split(',')))
pollens = list(map(int, "25,28,24,23,22,30,34,33,32,30,40,35,39,36,38,32,30,28,27,25".split(',')))
dairy = list(map(int, "20,22,25,20,18,17,16,15,17,30,18,18,20,19,14,15,16,20,18,20".split(',')))

data = [dust_mites, pollens, dairy]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot
bp = ax.boxplot(data, patch_artist = True, notch = True, vert = 0, whis = 2,
                widths = 0.4, sym = 'r+')

colors = ['#0000FF', '#00FF00', '#FF0000']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Adding labels
plt.xlabel("Prevalence")
plt.ylabel("Allergy Type")
plt.title("Allergy Prevalence Box Plot")
plt.xticks([1, 2, 3], ['Dust Mites', 'Pollens', 'Dairy'])

# Adding grid
ax.grid(True)

# Changing background color
ax.set_facecolor('lightgray')

# Saving the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the box body that contain the center point of the bounding box
for box in bp['boxes']:
    # get the index of the current box
    box_index = box.get_index()
    # get the center point of the box
    center_point = box.get_center()
    # get the width of the box
    width = box.get_width()
    # get the height of the box
    height = box.get_height()
    # get the coordinates of the center point of the box
    x, y = center_point
    # get the coordinates of the top left corner of the box
    left, bottom = box.get_xy()
    # get the coordinates of the top right corner of the box
    right, top = box.get_xy() + (width, height)
    # get the coordinates of the bottom left corner of the box
    bottom_left = (left, bottom)
    # get the coordinates of the bottom right corner of the box
    bottom_right = (right, bottom)
    # get the coordinates of the top left corner of the box
    top_left = (left, top)
    # get the coordinates of the top right corner of the box
    top_right = (right, top)
    # get the coordinates of the center point of the box
    center = (x, y)
    # get the coordinates of the center point of the box
    center_point = (x, y)
    # get the width of the box
    width = box.get_width()
    # get the height of the box
    height = box.get_height()
    # get the coordinates of the center point of the box
    center = (x, y)
    # get the coordinates of the center point of the box
    center_point = (x, y)
    # get the width of the box
    width = box.get_width()
    # get the height of the box
    height = box.get_height()
    # get the coordinates of the center point of the box
    center = (x, y)
    # get the coordinates of the center point of the box
    center_point = (x, y)
    # get the width of the box
    width = box.get_width()
    # get the height of the box
    height = box.get_height()
    # get the coordinates of the center point of the box
    center = (x, y)
    # get the coordinates of the center point of the box
    center_point = (x, y)
    # get the width of the box
    width = box.get_width()
    # get the height of the box
    height = box.get_height()
    # get the coordinates of the center point of the box
    center