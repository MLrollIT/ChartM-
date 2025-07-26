from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

country = ["USA", "China", "India", "Brazil"]
percentage = [30, 25, 20, 25]

def func(pct, allvals):
    absolute = int(pct)
    return f"{pct:.1f}%\n({absolute:d})"

explode = (0.1, 0, 0, 0)
colors = ['red', 'blue', 'green', 'yellow']

wedges, texts, autotexts = ax.pie(percentage, explode=explode, autopct=lambda pct: func(pct, percentage),
                                  textprops=dict(color="w"), colors=colors, shadow=True)

ax.legend(wedges, country,
          title="Countries",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Country distribution")

fig.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig("myplot.png")