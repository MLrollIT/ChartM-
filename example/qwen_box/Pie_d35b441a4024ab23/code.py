from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Set the face color of the figure
fig.patch.set_facecolor('gray')

# Define the social media platforms and corresponding percentages
social_media = ["Facebook", "Instagram", "Snapchat", "Twitter", "YouTube", "LinkedIn", "WhatsApp", "Others"]
percentage = [20, 20, 15, 15, 10, 10, 5, 5]

# Define the function for autopct
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"

# Define the explode parameter to emphasize the first wedge
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

# Plot the pie chart with autopct and explode parameters
wedges, texts, autotexts = ax.pie(percentage, explode=explode, autopct=lambda pct: func(pct, percentage),
                                  textprops=dict(color="w"), pctdistance=0.85, shadow=True)

# Add the legend
ax.legend(wedges, social_media,
          title="Social Media Platforms",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Set the title
ax.set_title("Social Media Usage")

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the slice that contains the center point of the bounding box
for text in autotexts:
    if text.get_bbox_to_anchor().get_points()[0][0] == 0.5:
        text.set_visible(False)
        text.set_path_effects([plt.pie.PiePathEffect(linewidth=2.83, foregroundcolor="#631e45")])