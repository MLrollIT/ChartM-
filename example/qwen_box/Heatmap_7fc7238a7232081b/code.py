from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008"]
subscriptions = ["Cable TV Subscriptions", "Online Streaming Subscriptions"]

data = np.array([[100, 120, 150, 200, 220, 200, 180, 160, 140],
                 [5, 8, 10, 20, 25, 30, 50, 100, 150]])

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='viridis', alpha=0.7)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(years)))
ax.set_yticks(np.arange(len(subscriptions)))
ax.set_xticklabels(years)
ax.set_yticklabels(subscriptions)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(subscriptions)):
    for j in range(len(years)):
        text = ax.text(j, i, data[i, j], ha="center", va="center", color="w")

ax.set_title("Comparison of Cable TV and Online Streaming Subscriptions (2000-2008)")
ax.set_xlabel("Year")
ax.set_ylabel("Type of Subscription")

# Make grid visible and set background color
ax.grid(True)
ax.set_facecolor('gray')

# Change the border color of the cells that contain the center point of the bounding box to #bf7225, and set the border thickness to 2.2 pixels.
for i in range(len(subscriptions)):
    for j in range(len(years)):
        if data[i, j] == 200:
            im.set_edgecolor((0.78, 0.44, 0.38))
            im.set_edgewidth(2.2)

fig.tight_layout()
plt.savefig("myplot.png")