from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Given Data
labels = 'Nanomaterial Synthesis', 'Nanoelectronics', 'Nanomedicine', 'Nanophotonics', 'Nanoenergy', 'Nanorobotics', 'Nanosensors', 'Nanoenvironment'
sizes = [20, 15, 25, 10, 10, 10, 5, 5]

fig, ax = plt.subplots()

# Plotting pie chart with additional parameters
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # Exploding first slice
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140, labeldistance=1.05, pctdistance=0.8)

# Setting background color to light gray
fig.patch.set_facecolor('lightgray')

plt.title("Distribution of Nanotechnology Research")  # Add title
plt.legend(labels, title="Research Fields", loc="upper right")  # Add legend

plt.tight_layout()
plt.savefig("myplot.png")