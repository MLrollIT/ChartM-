from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
professions = ["Healthcare Professionals", "Engineers", "Teachers", "Artists"]
percentages = [30, 25, 20, 25]

# Set up figure
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
ax.set_facecolor('lightgray')

# Function to calculate percentage and absolute value
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"

# Create pie chart
explode = (0.1, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Healthcare')
wedges, texts, autotexts = ax.pie(percentages, explode=explode, autopct=lambda pct: func(pct, percentages),
                                  textprops=dict(color="black"), shadow=True, startangle=90)

# Add legend
ax.legend(wedges, professions,
          title="Professions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Set title
ax.set_title("Professions Pie Chart")

# Set autotexts size and weight
plt.setp(autotexts, size=10, weight="bold")

# Hide the slices that contain the center point of the bounding box
for wedge in wedges:
    if wedge.get_label() == "Healthcare Professionals":
        wedge.set_visible(False)
        wedge.set_facecolor("gray")
        wedge.set_edgecolor("gray")
        wedge.set_alpha(0.5)
        wedge.set_offset(2.07, 3.08)

# Save figure
plt.tight_layout()
plt.savefig("myplot.png")