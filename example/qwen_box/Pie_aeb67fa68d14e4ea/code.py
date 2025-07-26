from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
pet_types = ["Dogs", "Cats", "Fish", "Birds", "Hamsters", "Rabbits", "Others"]
percentages = [35, 30, 15, 10, 5, 3, 2]  # Percentage values

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
fig.set_facecolor('gray')  # Set figure background color

colors = ['r', 'g', 'b', 'y', 'purple', 'orange', 'pink']  # Colors for each section

# Pie chart
wedges, texts, autotexts = ax.pie(percentages, explode=(0.1, 0, 0, 0, 0, 0, 0), labels=pet_types, 
                                  autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85)

# Draw a circle at the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Adjust border thickness and color of slices containing the center point of the bounding box
for wedge in wedges:
    if wedge.contains_point((0, 0)):
        wedge.set_linewidth(1.524)
        wedge.set_edgecolor('#111f0d')

# Set label font size for slices containing the center point of the bounding box
for autotext in autotexts:
    if autotext.contains_point((0, 0)):
        autotext.set_fontsize(6)

plt.title('Distribution of Pet Types')
plt.legend(pet_types, title="Pet Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig("myplot.png")