from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# data
data = {
    "Genre": ["Action", "Comedy", "Drama"],
    "Percentage": [40, 35, 25]
}

# create figure
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# set background color
fig.set_facecolor('gray')

# explode
explode = (0.1, 0, 0)

# autopct function
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"

# plot pie chart
wedges, texts, autotexts = ax.pie(data['Percentage'], explode=explode, labels=data['Genre'], autopct=lambda pct: func(pct, data['Percentage']),
                                  textprops=dict(color="w"), labeldistance=1.1, shadow=True, pctdistance=0.6)

# legend
ax.legend(wedges, data['Genre'],
          title="Genre",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# set title
ax.set_title("Genre Distribution")

# set autotexts size and weight
plt.setp(autotexts, size=8, weight="bold")

# layout
plt.tight_layout()

# save figure
plt.savefig("myplot.png")