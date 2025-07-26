from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 5), subplot_kw=dict(aspect="equal"))
ax.set_facecolor('lightblue')  # Changing background color to light blue

music_types = ["Rock","Pop","Classical","Country","Jazz","Rap","Reggae","R&B","Others"]
percentages = [20,25,15,10,10,5,5,5,5]

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Rock')

# Shades of blue for monochromatic theme
colors = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600', '#ff6361']

wedges, texts, autotexts = ax.pie(percentages, explode=explode, labels=music_types, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors, pctdistance=0.85)

# Draw white circle in the middle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Adding legend
ax.legend(wedges, music_types,
          title="Music Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Adding title and labels
ax.set_title("Percentage of Music Types")
plt.xlabel('Music Types')
plt.ylabel('Percentage')

plt.tight_layout()
plt.savefig("myplot_blue_theme.png")  # Saving the figure with a new name to reflect the theme change

# Disable clipping for the slices that contain the center point of the bounding box
for wedge in wedges:
    if wedge.contains_point((0, 0)):
        wedge.set_clip_on(False)
        wedge.set_facecolor('#a24222')