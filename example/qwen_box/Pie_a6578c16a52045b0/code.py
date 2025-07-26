from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
fig.set_facecolor('lightgrey')

households = ["Single Person", "Couple without children", "Couple with children", "Single Parent", "Multi-generational", "Shared Accommodation", "Elderly Living Alone", "Other"]
percentages = [15, 20, 25, 15, 15, 5, 3, 2]

explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Single Person')

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)

wedges, texts, autotexts = ax.pie(percentages, explode=explode, autopct=lambda pct: func(pct, percentages),
                                  textprops=dict(color="w"), pctdistance=0.85, shadow=True)

ax.legend(wedges, households, title="Household Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Food Waste Percentage by Household Type")

plt.tight_layout()
plt.savefig("myplot.png")