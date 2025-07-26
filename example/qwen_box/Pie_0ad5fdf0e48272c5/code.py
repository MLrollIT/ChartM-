from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
fig.set_facecolor('lightgray')

meat_types = ["Poultry","Beef","Pork","Lamb","Fish","Shellfish","Game","Other Meats"]
percentages = [25,20,30,10,5,2,3,5]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"

explode = (0, 0, 0.1, 0, 0, 0, 0, 0)
wedges, texts, autotexts = ax.pie(percentages, autopct=lambda pct: func(pct, percentages),
                                  textprops=dict(color="w"), explode=explode)

ax.legend(wedges, meat_types,
          title="Meat Types",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Meat Consumption")

plt.tight_layout()
plt.savefig("myplot.png")