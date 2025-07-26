from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
data = [
    [25,30,35,70,75,30,20], # Rose
    [40,30,20,10,50,60,70], # Sunflower
    [60,50,40,30,80,90,100], # Fern
    [20,30,40,80,85,40,30], # Dandelion
    [100,90,80,70,150,140,130], # Orchid
    [30,40,50,100,105,50,40], # Cactus
    [70,60,50,40,90,100,110], # Lily
    [50,60,70,80,85,90,40] # Oak
]

fig, ax = plt.subplots(figsize=(10, 7))

# Creating box plot
bp = ax.boxplot(data, patch_artist=True, notch=True, vert=0, whis=2, widths=0.4, sym='r+')

colors = ['#FF0000', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#FF00FF', '#808080', '#000000']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Plant Growth Patterns')
plt.xlabel('Growth Rate')
plt.ylabel('Plant Species')
plt.legend(['Rose', 'Sunflower', 'Fern', 'Dandelion', 'Orchid', 'Cactus', 'Lily', 'Oak'], loc='upper right')

ax.set_facecolor('#F0F0F0')
plt.grid(linestyle='--')

plt.tight_layout()
plt.savefig("myplot.png")