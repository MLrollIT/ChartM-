from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Data for plotting
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]
circulation = [200000, 210000, 250000, 255000, 260000, 180000, 210000, 215000, 180000]

fig, ax = plt.subplots()

# Plotting the data with modified colors
ax.plot(years, circulation, linestyle='dashdot', linewidth=2, color='red', 
        marker='o', markersize=5, alpha=0.8, markeredgecolor='black', markerfacecolor='yellow')

# Setting the labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Newspaper Circulation')
ax.set_title('Newspaper Circulation Over Years')

# Annotating the line
for i, txt in enumerate(circulation):
    ax.annotate(txt, (years[i], circulation[i]))

# Adding a grid and setting a light grey background
ax.grid(True)
ax.set_facecolor('lightgrey')

# Saving the figure
plt.tight_layout()
fig.savefig("myplot.png")