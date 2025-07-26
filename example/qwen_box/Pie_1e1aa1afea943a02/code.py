from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
impact_areas = ["Decreased Crop Yield", "Increased Pests and Diseases", "Altered Planting and Harvesting Schedule", "Shift in Suitable Cropland"]
percentages = [30, 25, 22, 23]

# Figure creation
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Function for displaying percentage and absolute value
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return f"{pct:.1f}%\n({absolute:d})"

# Pie chart creation with additional parameters
wedges, texts, autotexts = ax.pie(percentages, autopct=lambda pct: func(pct, percentages),
                                   textprops=dict(color="w"), explode=(0.1, 0, 0, 0), 
                                   labeldistance=1.2, shadow=True, pctdistance=0.8, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

# Legend, title and labels
ax.legend(wedges, impact_areas, title="Impact Areas", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
ax.set_title("Impact of Climate Change on Agriculture")
ax.set_xlabel("Impact Areas")
ax.set_ylabel("Percentage")

# Set figure background color
fig.patch.set_facecolor('gray')

# Change the format of text in pie chart
plt.setp(autotexts, size=8, weight="bold")

# Layout adjustment and figure saving
plt.tight_layout()
plt.savefig("myplot.png")