from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
clothing_types = ["Casual Wear", "Formal Wear", "Athletic Wear"]
percentages = [30, 40, 30]

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Set color for the chart figure
fig.patch.set_facecolor('lightgray')

# Plot pie chart
wedges, texts, autotexts = ax.pie(percentages, explode=(0, 0.1, 0), labels=clothing_types, autopct='%1.1f%%', shadow=True, startangle=90)

# Draw white circles at the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Set title
plt.title('Distribution of Clothing Types')

# Set legend
plt.legend(wedges, clothing_types, title="Clothing Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Modify the picker state of the slices that contain the center point of the bounding box to False
for wedge in wedges:
    if wedge.contains_point((0, 0)):
        wedge.set_picker(True)

# Modify the rasterized state of those same slices to False
for wedge in wedges:
    if wedge.contains_point((0, 0)):
        wedge.set_rasterized(False)

# Save the modified figure
plt.tight_layout()
plt.savefig("Edit_figure.png")