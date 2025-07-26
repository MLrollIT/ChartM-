from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# The given data
age_groups = ["Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
percentage = [10, 20, 30, 20, 10, 5, 5]  # converted the percentage into integer

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

wedges, texts, autotexts = ax.pie(percentage, autopct=lambda pct: func(pct, percentage),
                                  textprops=dict(color="w"),
                                  explode=(0, 0.1, 0, 0, 0, 0, 0),  # only "explode" the 1st slice (i.e. 'Under 18')
                                  labeldistance=1.15,
                                  shadow=True,
                                  pctdistance=0.6,
                                  colors=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

ax.legend(wedges, age_groups,
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Age Group Distribution")
fig.set_facecolor('gray')  # set background color to gray

plt.tight_layout()
plt.savefig("myplot.png")