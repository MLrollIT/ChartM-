from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
Age_Groups = ['18-24', '25-34', '35-44', '45-54']
Electronics = [100, 200, 300, 250]
Fashion = [125, 175, 275, 200]
Groceries = [80, 210, 320, 180]
Books = [90, 190, 310, 170]

data = [Electronics, Fashion, Groceries, Books]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot
bp = ax.boxplot(data, patch_artist = True, notch = True, vert = 0, whis = 2,
                sym='ro', widths=0.3)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # New color scheme

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Changing color and line width of whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B', linewidth = 1.5, linestyle =':')

# Changing color and linewidth of caps
for cap in bp['caps']:
    cap.set(color ='#8B008B', linewidth = 2)

# Changing color and linewidth of medians
for median in bp['medians']:
    median.set(color ='red', linewidth = 3)

# Changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D', color ='#e7298a', alpha = 0.5)

# x-axis labels
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(Age_Groups)

# Adding title
plt.title("Box plot of Purchases by Age Group")

# Removing top axes and right axes ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# Adding grid
ax.grid(True)

# Adding legend
ax.legend(['Electronics', 'Fashion', 'Groceries', 'Books'])

# Changing background color
ax.set_facecolor('#f0f0f0')

plt.tight_layout()
plt.savefig("myplot.png")