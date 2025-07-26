from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
professions = ["Healthcare Workers", "Factory Workers", "Office Workers"]
divorce_rates = [35, 45, 20]

# Figure and Axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# New Colors
colors = ['gold', 'silver', 'darkorange']  # Updated color scheme

# Function to display percentage and absolute value
def func(pct, allvals):
    absolute = int(round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

wedges, texts, autotexts = ax.pie(divorce_rates, explode=(0.1, 0, 0), labels=professions, colors=colors, 
                                  autopct=lambda pct: func(pct, divorce_rates), shadow=True, startangle=140, 
                                  textprops=dict(color="w"))

# Legend - No need to change the code here as colors are now linked with the wedges
ax.legend(wedges, professions,
          title="Professions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

# Title
ax.set_title("Divorce Rates by Profession")

# Background color 
fig.patch.set_facecolor('gray')  # No change needed here as the instruction was only for wedge colors

# Save figure
plt.tight_layout()
plt.savefig("myplot.png")