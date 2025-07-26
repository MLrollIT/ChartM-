from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

diseases = ["Rheumatoid Arthritis", "Type 1 Diabetes", "Celiac Disease"]
data = [40, 30, 30]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

explode = (0.1, 0, 0)  # only "explode" the 1st slice (i.e. 'Rheumatoid Arthritis')
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

wedges, texts, autotexts = ax.pie(data, explode=explode, labels=diseases, colors=colors, autopct=lambda pct: func(pct, data),
                                  shadow=True, startangle=140, labeldistance=1.2, pctdistance=0.8)

ax.legend(wedges, diseases,
          title="Diseases",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Disease Distribution")
fig.set_facecolor('gray')
plt.tight_layout()
plt.savefig("myplot.png")