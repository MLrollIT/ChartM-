from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

exercise_types = ("Yoga", "Running", "Cycling", "Swimming", "CrossFit", "Zumba", "Kickboxing", "Pilates")
data = {
    "Year 1": np.array([100, 200, 150, 100, 250, 300, 350, 400]),
    "Year 2": np.array([120, 180, 160, 90, 240, 280, 330, 380]),
    "Year 3": np.array([130, 160, 250, 80, 230, 260, 310, 360]),
    "Year 4": np.array([140, 250, 240, 70, 220, 240, 290, 340]),
    "Year 5": np.array([60, 240, 250, 260, 210, 220, 270, 320]),
    "Year 6": np.array([150, 220, 260, 250, 400, 200, 250, 300]),
    "Year 7": np.array([160, 200, 270, 240, 390, 400, 230, 280]),
    "Year 8": np.array([170, 180, 200, 230, 380, 380, 210, 260])
}
width = 0.1

# Define a list of colors for each year
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

fig, ax = plt.subplots()
x = np.arange(len(exercise_types))
bars = []

for i, (year, popularity) in enumerate(data.items()):
    p = ax.bar(x + i*width, popularity, width, label=year, color=colors[i])  # Use color from colors list
    bars.append(p)

ax.set_title("Popularity of Exercise Types Over 8 Years")
ax.set_xlabel("Exercise Types")
ax.set_ylabel("Popularity")
ax.set_xticks(x + width / 2)
ax.set_xticklabels(exercise_types)
ax.legend(loc="upper right")
ax.grid(True)
ax.set_facecolor('lightgray')

# Add labels to each bar
for bar in bars:
    ax.bar_label(bar, label_type="center")

plt.tight_layout()
plt.savefig("myplot.png")