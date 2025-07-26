from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

age_groups = ["18-25", "26-35", "36-45", "46-55", "56-65"]
activities = ["Gym Visits", "Outdoor Activities"]

data = np.array([[12, 35],
                 [27, 30],
                 [45, 25],
                 [60, 15],
                 [30, 5]])

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='YlGnBu', alpha=0.7)

ax.set_xticks(np.arange(len(activities)))
ax.set_yticks(np.arange(len(age_groups)))

ax.set_xticklabels(activities)
ax.set_yticklabels(age_groups)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(age_groups)):
    for j in range(len(activities)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="black")

ax.set_title("Activity Preferences by Age Group")
ax.grid(True)
ax.set_facecolor('gray')
fig.tight_layout()

# Change the border color of the cells that contain the center point of the bounding box to #cb8dc8 with a width of 0.7 pixels.
# Then, update the border thickness of these cells to 1.6 pixels and modify the color to #a38ac5.
bbox = ax.bbox
bbox_points = bbox.get_points()
bbox_points[1][0] = (bbox_points[1][0][0] + bbox_points[1][0][1]) / 2
bbox_points[1][1] = (bbox_points[1][1][0] + bbox_points[1][1][1]) / 2
bbox_points[2][0] = (bbox_points[2][0][0] + bbox_points[2][0][1]) / 2
bbox_points[2][1] = (bbox_points[2][1][0] + bbox_points[2][1][1]) / 2
bbox_points[3][0] = (bbox_points[3][0][0] + bbox_points[3][0][1]) / 2
bbox_points[3][1] = (bbox_points[3][1][0] + bbox_points[3][1][1]) / 2
bbox_points[4][0] = (bbox_points[4][0][0] + bbox_points[4][0][1]) / 2
bbox_points[4][1] = (bbox_points[4][1][0] + bbox_points[4][1][1]) / 2
bbox.set_points(bbox_points)
bbox.set_edgecolor("#cb8dc8")
bbox.set_linewidth(0.7)
bbox.set_linestyle("-")
bbox.set_capstyle("round")
bbox.set_joinstyle("round")

bbox = ax.bbox
bbox_points = bbox.get_points()
bbox_points[1][0] = (bbox_points[1][0][0] + bbox_points[1][0][1]) / 2
bbox_points[1][1] = (bbox_points[1][1][0] + bbox_points[1][1][1]) / 2
bbox_points[2][0] = (bbox_points[2][0][0] + bbox_points[2][0][1]) / 2
bbox_points[2][1] = (bbox_points[2][1][0] + bbox_points[2][1][1]) / 2
bbox_points[3][0] = (bbox_points[3][0][0] + bbox_points[3][0][1]) / 2
bbox_points[3][1] = (bbox_points[3][1][0] + bbox_points[3][1][1]) / 2
bbox_points[4][0] = (bbox_points[4][0][0] + bbox_points[4][0][1]) / 2
bbox_points[4][1] = (bbox_points[4][1][0] + bbox_points[4][1][1]) / 2
bbox.set_points(bbox_points)
bbox.set_edgecolor("#a38ac5")
bbox.set_linewidth(1.6)
bbox.set_linestyle("-")
bbox.set_capstyle("round")
bbox.set_joinstyle("round")

fig.tight_layout()
plt.savefig("myplot.png")