from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
data = {
    'Type of Media': ['Television', 'Radio', 'Newspaper', 'Social Media', 'Books', 'Magazines'],
    'Percentage': [30, 20, 15, 25, 5, 5]
}

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Function to calculate the absolute values
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"

# Use the 'explode' parameter to slightly separate each piece of the pie
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
wedges, texts, autotexts = ax.pie(data['Percentage'], explode=explode, autopct=lambda pct: func(pct, data['Percentage']),
                                  textprops=dict(color="w"))

# Add a legend
ax.legend(wedges, data['Type of Media'],
          title="Type of Media",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Set the title
ax.set_title("Distribution of Media Types")

# Set the background color
ax.set_facecolor("lightgray")

# Modify the line width of the slice that contains the center point of the bounding box
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_bbox(dict(boxstyle="square", ec=(0.5, 0.5, 0.5), fc=(0.5, 0.5, 0.5), lw=2.40))

# Ensure that the rasterized state of the same slice is set to False
for autotext in autotexts:
    autotext.set_rasterized(False)

plt.tight_layout()
plt.savefig("myplot.png")