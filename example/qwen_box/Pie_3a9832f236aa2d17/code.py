from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

religions = ["Christianity", "Islam", "Unaffiliated", "Hinduism", "Buddhism", "Folk Religion", "Other Religions"]
data = [31, 24, 16, 15, 7, 6, 1]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), explode=(0.1, 0, 0, 0, 0, 0, 0), labeldistance=1.1, shadow=True, pctdistance=0.8, colors=['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])

ax.legend(wedges, religions, title="Religions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Religion Percentages")

fig.set_facecolor('gray')

plt.tight_layout()
plt.savefig("myplot.png")