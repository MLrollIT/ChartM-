from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
exercises = ["Running", "Swimming", "Cycling", "Weightlifting", "Yoga", "Pilates", "CrossFit", "Dance", "Others"]
data = [20, 15, 10, 15, 10, 10, 10, 5, 5]

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Function to display percentage and absolute values
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return f"{pct:.1f}%\n({absolute:d})"

# Additional parameters for pie chart
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'purple', 'orange', 'cyan', 'brown']

wedges, texts, autotexts = ax.pie(data, explode=explode, labels=exercises, colors=colors, autopct=lambda pct: func(pct, data),
                                  shadow=True, startangle=140, textprops=dict(color="w"))

ax.legend(wedges, exercises,
          title="Exercise Type",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Exercise Type Distribution")

fig.patch.set_facecolor('gray')
plt.tight_layout()
plt.savefig("myplot.png")