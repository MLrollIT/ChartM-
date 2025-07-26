from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
professions = ["Doctors", "Lawyers", "Teachers", "Engineers", "Artists", "Others"]
rates = [15, 20, 10, 25, 20, 10]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(rates, labels=professions, autopct='%1.1f%%', shadow=True, startangle=90)

# Set up properties for the legend and title
ax.set_title("Divorce Rates in Different Professions")
ax.legend(wedges, professions, title="Professions", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Change the background color of the figure
fig.set_facecolor('gray')

# Set layout to tight to minimize the amount of empty space on the figure
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")