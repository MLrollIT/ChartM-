from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

debris = ["Defunct satellites",
          "Spent rocket stages",
          "Fragmentation debris",
          "Mission-related debris",
          "Functional spacecraft",
          "Anomalous debris"]

data = [20, 25, 30, 15, 5, 5]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return f"{pct:.1f}%\n({absolute:d} %)"

explode = (0.1, 0, 0, 0, 0, 0) 

wedges, texts, autotexts = ax.pie(data, explode=explode, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), shadow=True, pctdistance=0.85, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])

ax.legend(wedges, debris,
          title="Type of Debris",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Space Debris Distribution")

fig.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")