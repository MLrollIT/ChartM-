from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

region_percent = ["North America,15%",
                  "South America,10%",
                  "Europe,20%",
                  "Africa,15%",
                  "Asia,25%",
                  "Oceania,5%",
                  "Middle East,5%",
                  "Central America,4%",
                  "Caribbean,1%"]

data = [float(x.split(',')[1].replace("%", "")) for x in region_percent]
regions = [x.split(',')[0] for x in region_percent]

explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # explode 1st slice

def func(pct, allvals):
    absolute = int(pct)
    return f"{pct:.1f}%\n({absolute:d}%)"

wedges, texts, autotexts = ax.pie(data, explode=explode, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), pctdistance=0.85, shadow=True)

ax.legend(wedges, regions,
          title="Regions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Percentage Distribution of Different Regions")

fig.patch.set_facecolor('gray')

plt.tight_layout()  
plt.savefig("myplot.png")