from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given Data
data = {
    'Year': [2016, 2017, 2018, 2019, 2020, 2021],
    'Disease A': [100, 90, 70, 50, 30, 60],
    'Disease B': [200, 225, 250, 275, 300, 150],
    'Disease C': [300, 290, 275, 280, 265, 285]
}

fig, ax = plt.subplots()

# Set background color
ax.set_facecolor('lightgray')

years = np.array(data['Year'])  # the label locations
height = 0.25  # the height of the bars
multiplier = 0

# Define shades of blue
shades_of_blue = ['navy', 'royalblue', 'lightblue']

for disease, counts in list(data.items())[1:]:
    offset = height * multiplier
    bars = ax.barh(years + offset, counts, height, label=disease, edgecolor='black', color=shades_of_blue[multiplier])
    ax.bar_label(bars, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Number of Cases')
ax.set_title('Cases of Diseases A, B and C over the years')
ax.set_yticks(years + height)
ax.set_yticklabels(data['Year'])
ax.legend(loc='upper right', ncol=1)
ax.invert_yaxis()  # labels read top-to-bottom

# Adding grid
ax.grid(True)

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")