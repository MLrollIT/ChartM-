from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

architecture_style = ["Classical", "Modernist", "Postmodern", "Art Deco", "Gothic", "Baroque", "Renaissance", "Romanesque"]
percentage = [20, 15, 10, 10, 20, 15, 5, 5]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

wedges, texts, autotexts = ax.pie(percentage, autopct=lambda pct: func(pct, percentage),
                                  textprops=dict(color="w"), explode=(0.1, 0, 0, 0, 0.1, 0, 0, 0), shadow=True)

ax.legend(wedges, architecture_style,
          title="Architecture Style",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Percentage of Architecture Styles")

fig.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig("myplot.png")