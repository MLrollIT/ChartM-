from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = {'Year': [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
        'Organic Crops': [1000, 1150, 1300, 1450, 1600, 1800, 2000, 2200],
        'Organic Livestock': [300, 500, 700, 400, 1100, 1500, 1600, 1400],
        'Organic Aquaculture': [100, 80, 60, 140, 160, 120, 100, 130]}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

# Plotting the data
bars1 = ax.bar(df['Year'] - 0.2, df['Organic Crops'], width=0.2, color='b', align='center', label='Organic Crops')
bars2 = ax.bar(df['Year'], df['Organic Livestock'], width=0.2, color='r', align='center', label='Organic Livestock')
bars3 = ax.bar(df['Year'] + 0.2, df['Organic Aquaculture'], width=0.2, color='g', align='center', label='Organic Aquaculture')

# Annotating the data value on the bar
ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)
ax.bar_label(bars3, padding=3)

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Production')
ax.set_title('Organic Production Over Years')

# Adding legend
ax.legend()

# Adding grid and setting background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Set the fill pattern of the bars that share the same legend as those containing the center point of the bounding box to '-', and change their edge color to '#2c87ad'
for bar in bars1:
    bar.set_fill('-')
    bar.set_edgecolor('#2c87ad')
for bar in bars2:
    bar.set_fill('-')
    bar.set_edgecolor('#2c87ad')
for bar in bars3:
    bar.set_fill('-')
    bar.set_edgecolor('#2c87ad')

plt.tight_layout()
plt.savefig("myplot.png")