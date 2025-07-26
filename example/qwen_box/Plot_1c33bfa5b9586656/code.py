from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
years = ['2017', '2018', '2019']
sprains_and_strains = [150, 220, 100]
fractures = [100, 500, 90]
burns = [70, 80, 70]

fig, ax = plt.subplots()

# Plotting the data with updated colors
ax.plot(years, sprains_and_strains, label='Sprains and Strains', linestyle='--', color='purple', marker='o', markersize=10, alpha=0.7)
ax.plot(years, fractures, label='Fractures', linestyle='-.', color='orange', marker='s', markersize=10, alpha=0.7)
ax.plot(years, burns, label='Burns', linestyle=':', color='black', marker='^', markersize=10, alpha=0.7)

# Setting labels, title, and grid
ax.set(xlabel='Year', ylabel='Number of Injuries',
       title='Number of Injuries by Type from 2017 to 2019')
ax.grid()

# Adding legend and annotations
ax.legend()
for (i, j) in zip(years, sprains_and_strains):
    ax.annotate('Sprains and Strains', (i, j))
for (i, j) in zip(years, fractures):
    ax.annotate('Fractures', (i, j))
for (i, j) in zip(years, burns):
    ax.annotate('Burns', (i, j))

# Changing the background color to white
ax.set_facecolor('white')

plt.tight_layout()
fig.savefig("myplot_modified.png")