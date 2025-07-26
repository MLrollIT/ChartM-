from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

age_group = ["Under 18","18-34","35-64","65+"]
percentages = [15, 35, 40, 10]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return f"{pct:.1f}%\n({absolute:d} %)"

# Updated color scheme for the pie chart
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

wedges, texts, autotexts = ax.pie(percentages, autopct=lambda pct: func(pct, percentages),
                                  textprops=dict(color="w"), explode=[0.1,0,0,0], shadow=True, pctdistance=0.85, colors=new_colors)

ax.legend(wedges, age_group,
          title="Age Group",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Age Distribution")

fig.set_facecolor('lightgray')

plt.tight_layout()
plt.savefig("myplot.png")