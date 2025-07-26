from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# data
tech = ["Navigation Systems",
        "Artificial Intelligence",
        "Camera Technology",
        "Materials and Design",
        "Power Efficiency"]

data = [30, 25, 20, 15, 10]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), explode=(0, 0.1, 0, 0, 0), labeldistance=1.05, shadow=True, pctdistance=0.8, colors=['red', 'green', 'blue', 'orange', 'purple'])

ax.legend(wedges, tech,
          title="Drone Technology",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Drone Technology Distribution")

plt.tight_layout()
plt.savefig("myplot.png")