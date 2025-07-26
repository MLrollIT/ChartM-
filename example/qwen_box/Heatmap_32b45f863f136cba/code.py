from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

professions = ["Teacher", "Doctor", "Software Developer", 
               "Construction Worker", "Nurse", "Chef", 
               "Lawyer", "Police Officer", "Retail Worker"]

weeks = ["Week 1", "Week 2"]

hours = np.array([[40, 44], [50, 75], [45, 47], [60, 42], 
                  [48, 50], [50, 50], [55, 30], [60, 60], [35, 35]])

fig, ax = plt.subplots()
im = ax.imshow(hours, cmap='viridis', alpha=0.7)

ax.set_xticks(np.arange(len(weeks)))
ax.set_yticks(np.arange(len(professions)))

ax.set_xticklabels(weeks)
ax.set_yticklabels(professions)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(professions)):
    for j in range(len(weeks)):
        text = ax.text(j, i, hours[i, j], ha="center", va="center", color="w")
        if text.get_bbox().get_width() != 1:
            text.set_fontsize(16)
            text.set_bbox(dict(boxstyle="square", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8), alpha=0.4))

ax.set_title("Hours worked by different professions")
ax.set_xlabel("Week")
ax.set_ylabel("Profession")

ax.grid(True)
ax.set_facecolor('gray')

fig.tight_layout()
plt.savefig("myplot.png")