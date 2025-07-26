from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

types_of_game = ["Action",
                 "Sports",
                 "Adventure",
                 "Role-playing",
                 "Strategy",
                 "Puzzle"]

data = [20, 25, 15, 20, 10, 10]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"

explode = (0, 0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Sports')

wedges, texts, autotexts = ax.pie(data, explode=explode, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, types_of_game,
          title="Types of Game",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Game Types: A Pie Chart")

fig.set_facecolor('gray')
plt.tight_layout()
plt.savefig("myplot.png")