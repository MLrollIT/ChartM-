from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

# Data from csv
regions = ["North America", "Europe", "Asia", "Africa", "Australia"]
percentages = [20, 25, 30, 15, 10]

# Function to format the autopct
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d}%)"

# Parameters for explode
explode = (0.1, 0.1, 0.1, 0.1, 0.1)  # only "explode" the slices

wedges, texts, autotexts = ax.pie(percentages, explode=explode, autopct=lambda pct: func(pct, percentages), textprops=dict(color="w"))

ax.legend(wedges, regions,
          title="Regions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Regional Distribution")

# Set the facecolor
fig.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")