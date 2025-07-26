from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

e_waste_types = ["Small Equipment", "Large Equipment", "Temperature Exchange Equipment", "Screens and Monitors", "Small IT and Telecommunication Equipment"]
data = [30, 25, 20, 15, 10]

# Updated the colors here to a new color palette
colors = ['cyan', 'magenta', 'orange', 'green', 'blue'] 
explode = (0.1, 0, 0, 0, 0) # only "explode" the 1st slice

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} %)"

wedges, texts, autotexts = ax.pie(data, explode=explode, labels=e_waste_types, colors=colors, autopct=lambda pct: func(pct, data), shadow=True, startangle=90)

ax.legend(wedges, e_waste_types, title="E-waste Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Distribution of E-waste Types")
fig.set_facecolor('gray')
plt.tight_layout()
plt.savefig("myplot.png")