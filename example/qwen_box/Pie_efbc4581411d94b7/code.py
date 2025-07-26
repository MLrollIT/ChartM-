from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

phobia_data = ["30%", "20%", "15%", "10%", "15%", "10%"]
phobia_types = ["Arachnophobia", "Claustrophobia", "Aerophobia", "Acrophobia", "Cynophobia", "Ophidiophobia"]

data = [float(x.strip('%')) for x in phobia_data]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

explode = (0.1, 0, 0, 0, 0, 0)  
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

wedges, texts, autotexts = ax.pie(data, explode=explode, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="k"), colors=colors, shadow=True)

ax.legend(wedges, phobia_types,
          title="Phobias",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Pie Chart: Phobia Percentages")
fig.set_facecolor('lightgray') 
plt.tight_layout()
plt.savefig("myplot.png")