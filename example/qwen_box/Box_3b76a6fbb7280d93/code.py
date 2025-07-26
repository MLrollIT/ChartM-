from matplotlib.transforms import Bbox
from matplotlib.figure import Figure

# Get the figure instance
fig = plt.gcf()

# Get the axes instance
ax = fig.axes[0]

# Get the bounding box of the boxes that contain the center point of the bounding box
bbox = ax.bbox_to_transform(ax.bbox)

# Set the clipping box for the boxes that contain the center point of the bounding box
bbox = Bbox([[112, 139], [112 + 169, 139 + 175]])

# Set the clipping state of the boxes to False for these coordinates
bbox.set_clip_on(False)

# Save the figure
plt.savefig('Edit_figure.png')