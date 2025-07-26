from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

pets = ["Dogs", "Cats", "Fish", "Birds", "Small mammals", "Reptiles"]
data = [35, 30, 15, 10, 7, 3]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), colors=colors)

ax.legend(wedges, pets, title="Pets", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Pets Ownership by Percentage")

fig.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig("myplot.png")