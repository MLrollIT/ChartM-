from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
profession = ["Healthcare Professionals", "Teachers", "Engineers"]
percentage = [35, 40, 25]

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Define explode values to offset each slice, and colors for each slice
explode = (0.1, 0.1, 0.1)
colors = ['lightblue', 'lightcoral', 'yellow']

# Plot pie chart
wedges, texts, autotexts = ax.pie(percentage, explode=explode, labels=profession, colors=colors, 
                                  autopct='%1.1f%%', shadow=True, startangle=140, 
                                  labeldistance=1.05, pctdistance=0.6)

# Set title, change background color and tweak layout
ax.set_title("Percentage of Different Professions")
ax.set_facecolor("gray")
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")

# Modify the object in the chart
for wedge in wedges:
    wedge.set_linestyle('dotted')
    wedge.set_picker(False)