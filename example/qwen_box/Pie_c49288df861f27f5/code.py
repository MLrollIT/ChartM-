from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

region_percentage = {
    "North America": "10%",
    "South America": "12%",
    "Europe": "20%",
    "Africa": "17%",
    "Asia": "28%",
    "Middle East": "5%",
    "Oceania": "5%",
    "Polar Regions": "3%",
    "International Waters": "0%"
}

data = [int(x[:-1]) for x in region_percentage.values()]
regions = [x for x in region_percentage.keys()]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d}%)"

# Custom color palette for the wedges
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#f7dc6f']

wedges, texts, autotexts = ax.pie(data, explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0), autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), pctdistance=0.85, shadow=True, colors=colors)

ax.legend(wedges, regions,
          title="Regions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Percentage of Data by Region")

fig.patch.set_facecolor('lightgray')

# Adjust the transparency of the slices that contain the center point of the bounding box to 0.716
for wedge in wedges:
    if wedge.contains_point((0.5, 0.5)):
        wedge.set_alpha(0.716)

# Apply a diagonal stripe fill to these slices
for wedge in wedges:
    if wedge.contains_point((0.5, 0.5)):
        wedge.set_facecolor("#f0f0f0")

plt.tight_layout()
plt.savefig("myplot.png")