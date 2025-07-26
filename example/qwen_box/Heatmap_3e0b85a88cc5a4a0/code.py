from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

age_groups = ["Under 18", "18-24", "25-34", "35-44", "45 and over"]
times_of_day = ["Morning Viewers", "Afternoon Viewers", "Evening Viewers"]

viewers = np.array([[100, 85, 90],
                    [80, 70, 110],
                    [70, 90, 105],
                    [60, 75, 95],
                    [50, 60, 80]])

fig, ax = plt.subplots()
im = ax.imshow(viewers, cmap='plasma', alpha=0.7)  # Changed colormap to 'plasma'

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(times_of_day)), labels=times_of_day)
ax.set_yticks(np.arange(len(age_groups)), labels=age_groups)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

ax.set_facecolor('lightgray')
ax.grid(True)

# Loop over data dimensions and create text annotations.
for i in range(len(age_groups)):
    for j in range(len(times_of_day)):
        text = ax.text(j, i, viewers[i, j],
                       ha="center", va="center", color="black")  # Changed text color to black

ax.set_title("TV Viewership by Age Group and Time of Day")
fig.tight_layout()
plt.savefig("myplot.png")