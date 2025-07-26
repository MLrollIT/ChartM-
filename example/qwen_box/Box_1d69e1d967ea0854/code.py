from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {'Demographics': ['Young Adults', 'Middle Aged', 'Seniors', 'Teens'],
        'Recycling Habits': [[10, 12, 14, 20, 22, 25, 6, 30, 32, 35, 18, 20], 
                             [12, 13, 11, 9, 8, 7, 20, 10, 7, 6, 5, 50], 
                             [20, 18, 15, 13, 10, 9, 12, 30, 35, 32, 28, 25],
                             [10, 15, 20, 25, 30, 12, 14, 50, 45, 40, 35, 30]]
       }

df = pd.DataFrame(data, columns=['Demographics', 'Recycling Habits'])

fig, ax = plt.subplots(figsize =(10, 7))

bp = ax.boxplot(df['Recycling Habits'], patch_artist = True, notch = True, vert = 0, widths=0.7, sym='r+')

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_yticklabels(df['Demographics'])
ax.set_xlabel('Recycling Habits')
ax.set_title('Boxplot of Recycling Habits by Demographics')
ax.grid(True)
ax.set_facecolor('lightgrey')

plt.tight_layout()
plt.savefig('myplot.png')