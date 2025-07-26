from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

agri_practices = ["Shift to Organic Farming",
                  "Adoption of Drought Tolerant Crops",
                  "Use of Crop Rotation",
                  "Increased Irrigation",
                  "Investment in Greenhouses",
                  "Implementation of Terracing",
                  "Use of Weather Forecasting Technology",
                  "Adoption of Genetically Modified Crops"]

data = [20, 18, 15, 12, 10, 10, 10, 5]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

wedges, texts, autotexts = ax.pie(data, explode=explode, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), pctdistance=0.85, shadow=True)

ax.legend(wedges, agri_practices,
          title="Agricultural Practices",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Agricultural Practices: A Pie Chart")

fig.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")