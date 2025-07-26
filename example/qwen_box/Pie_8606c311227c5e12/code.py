from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
fig.set_facecolor('lightgray')

data = {"America": 35, "Europe": 45, "Asia": 20}
colors = ['blue', 'green', 'red']  # Define colors for each region
regions = list(data.keys())
values = list(data.values())

wedges, texts, autotexts = ax.pie(values, explode=(0.1, 0, 0), labels=regions, autopct='%1.1f%%',
                                   shadow=True, startangle=90, colors=colors)  # Add colors parameter

ax.legend(wedges, regions,
          title="Regions",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

ax.set_title("Regions by Percentage")
plt.tight_layout()
plt.savefig("myplot.png")