from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
fig.set_facecolor('white')  # Changed background color to white

data = ['Under 18', '18-34', '35+']
percentage = [30, 40, 30]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d}%)"

explode = (0.1, 0, 0) 
colors = ['red','green','blue']
wedges, texts, autotexts = ax.pie(percentage, labels=data, autopct=lambda pct: func(pct, percentage),
                                  explode=explode, shadow=True, startangle=90, colors=colors)

ax.legend(wedges, data,
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("TV Viewing Percentage by Age Group")

plt.tight_layout()
plt.savefig("myplot.png")