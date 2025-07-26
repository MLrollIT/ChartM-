from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

demographics = ["Teenagers", "Adults", "Elderly", "Infants"]
hours_of_sleep = np.array([6.5, 7.3, 5.2, 14.8])

fig, ax = plt.subplots()

ax.set_facecolor('white')  # Change background to white

im = ax.imshow(hours_of_sleep.reshape(1,4), cmap='plasma', alpha=0.7)  # Change colormap to 'plasma'

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(demographics)))
ax.set_yticks([])

ax.set_xticklabels(demographics)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(demographics)):
    text = ax.text(i, 0, hours_of_sleep[i],
                   ha="center", va="center", color="black")  # Change text color to black

ax.set_title("Hours of Sleep by Age Group")
ax.set_xlabel('Demographics')
ax.set_ylabel('Hours of Sleep')

fig.tight_layout()
plt.grid(visible=True)
plt.savefig("myplot.png")