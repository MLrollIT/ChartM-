from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

debris_type = ["Defunct Satellites", "Rocket Body Debris", "Mission-Related Debris", "Fragmentation Debris"]
data = [40, 25, 20, 15]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, debris_type,
          title="Debris Type",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Space Debris Types")
fig.set_facecolor('grey')
plt.tight_layout()
plt.savefig("myplot.png")