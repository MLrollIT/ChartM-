from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# The given data
social_media_platforms = ["Facebook", "Instagram", "Twitter", "LinkedIn", "YouTube", "Pinterest"]
years = ["2016", "2017", "2018", "2019", "2020"]

data = np.array([[500, 600, 800, 400, 1000],
                 [200, 400, 200, 800, 1000],
                 [300, 500, 300, 900, 200],
                 [200, 500, 800, 1000, 200],
                 [400, 600, 400, 800, 400],
                 [300, 200, 900, 200, 1000]])

fig, ax = plt.subplots()

# Change colormap to 'plasma'
im = ax.imshow(data, cmap='plasma', alpha=0.8)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(social_media_platforms)))

ax.set_xticklabels(years)
ax.set_yticklabels(social_media_platforms)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations with color changed to black.
for i in range(len(social_media_platforms)):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="black")  # Change text color to black

# Setting title and labels
ax.set_title("Social Media Usage from 2016 to 2020")
ax.set_xlabel("Years")
ax.set_ylabel("Social Media Platforms")

# Add Grid
ax.grid(True)

# Set the figure background color to light gray
ax.set_facecolor('lightgray')

# Save the plot
fig.tight_layout()
plt.savefig("myplot.png")

# Enhance the border thickness of the cells that contain the center point of the bounding box to 1.6 pixels, changing their color to #a7424e. Additionally, update the annotation text color in those cells to #d42d92.
for i in range(len(social_media_platforms)):
    for j in range(len(years)):
        if data[i, j] == 1000:
            text = ax.text(j, i, data[i, j],
                           ha="center", va="center", color="#d42d92")  # Change text color to #d42d92
            text.set_bbox(dict(boxstyle="square", ec="#a7424e", lw=1.6, fc="#a7424e"))  # Change border color and thickness