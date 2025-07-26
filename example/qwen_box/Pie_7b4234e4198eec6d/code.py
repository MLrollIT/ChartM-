from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

segments = ["Cable Television", "Satellite Television", "Internet Protocol Television", "Hybrid IPTV", "Other Technologies"]
data = [40, 25, 15, 12, 8]

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

def func(pct, allvals):
    absolute = int(pct)
    return f"{pct:.1f}%\n({absolute:d} %)"

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"),
                                  explode=(0.1, 0, 0, 0, 0),
                                  shadow=True,
                                  colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])

ax.legend(wedges, segments,
          title="Market Segments",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Market Segment Shares")

# Set the facecolor to white
fig.set_facecolor('white')

plt.tight_layout()

plt.savefig("myplot.png")