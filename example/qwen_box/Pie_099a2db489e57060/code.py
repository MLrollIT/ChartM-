from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Define the data and labels
data = [30, 25, 20, 15, 7, 3]
platforms = ["PlayStation", "Xbox", "PC", "Mobile", "Nintendo", "Others"]

# Function to calculate the absolute values
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

# New pastel color scheme
pastel_colors = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc']

# Define the pie chart with the new color scheme
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), explode=(0, 0, 0.1, 0, 0, 0), 
                                  labeldistance=1.15, shadow=True, pctdistance=0.85, 
                                  colors=pastel_colors)  # Use pastel colors

# Set the legend
ax.legend(wedges, platforms,
          title="Platforms",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Set the autotexts
plt.setp(autotexts, size=8, weight="bold")

# Set the title
ax.set_title("Platform Usage: A pie")

# Set the background color
fig.set_facecolor('gray')

# Adjust layout to make room for the legend
plt.tight_layout()

# Save the plot
plt.savefig("myplot_pastel.png")  # Save the plot with a new filename to reflect the pastel color change

# Set the picker state of the slice that contains the center point of the bounding box to False
for wedge in wedges:
    if wedge.contains_point((3.67, 3.92)):
        wedge.set_picker(True)

# Apply a shadow effect with an offset of (3.67, 3.92) and use gold as the shadow color
for wedge in wedges:
    if wedge.contains_point((3.67, 3.92)):
        wedge.set_facecolor('gold')
        wedge.set_edgecolor('none')
        wedge.set_zorder(10)
        wedge.set_boxstyle('square', pad=0.1, rounding_size=0.1)
        wedge.set_transform(wedge.get_transform().rotate_deg(90))
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge.set_picker(True)
        wedge