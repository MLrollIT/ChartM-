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
im = ax.imshow(data, cmap='viridis', alpha=0.7)  # Changed color map to 'viridis'

ax.set_xticks(np.arange(len(activities)))
ax.set_yticks(np.arange(len(age_groups)))

ax.set_xticklabels(activities)
ax.set_yticklabels(age_groups)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(age_groups)):
    for j in range(len(activities)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="white")  # Changed text color to white

ax.set_title("Activity Preferences by Age Group")
ax.grid(True, color='white')  # Changed grid lines to white
ax.set_facecolor('gray')
fig.tight_layout()
plt.savefig("myplot.png")