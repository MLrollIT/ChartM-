from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

region = ["North America", "Europe", "Asia"]

percentage = [35, 45, 20]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)

wedges, texts, autotexts = ax.pie(percentage, autopct=lambda pct: func(pct, percentage),
                                  textprops=dict(color="w"), explode=(0.1, 0, 0), 
                                  shadow=True, startangle=90)

ax.legend(wedges, region,
          title="Regions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Percentage of Population by Region")

# Change the background color here
fig.patch.set_facecolor('white')  # Changed from 'gray' to 'white'

plt.tight_layout()

plt.savefig("myplot.png")