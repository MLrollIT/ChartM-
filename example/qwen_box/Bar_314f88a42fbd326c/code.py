from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

services = ["Online Shopping", "Food Delivery", "Video Streaming", "Online Gaming"]
usage_values = {
    "Online Shopping": np.array([250, 275, 310, 350, 415, 420, 430, 500, 510, 300, 350, 375]),
    "Food Delivery": np.array([100, 120, 150, 140, 130, 120, 110, 90, 80, 70, 60, 50]),
    "Video Streaming": np.array([200, 400, 600, 800, 1000, 1200, 800, 400, 200, 100, 50, 25]),
    "Online Gaming": np.array([50, 100, 150, 200, 250, 300, 350, 100, 50, 0, 0, 0])
}
months = np.arange(1, 13)
width = 0.2

fig, ax = plt.subplots(figsize=(10, 6))
bars = []

for index, (service, usage) in enumerate(usage_values.items()):
    bar = ax.bar(months + index * width, usage, width, label=service)
    bars.append(bar)

ax.set_xlabel("Months")
ax.set_ylabel("Usage")
ax.set_title("Usage of Different Services over Months")
ax.set_xticks(months + width / 2)
ax.set_xticklabels(months)
ax.legend()

for bar in bars:
    ax.bar_label(bar)

ax.grid(True)
ax.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")