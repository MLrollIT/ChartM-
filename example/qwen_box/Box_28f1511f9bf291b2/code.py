from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data_string = StringIO("""
Platform,Year 1,Year 2,Year 3,Year 4,Year 5,Year 6,Year 7,Year 8,Year 9
Facebook,5000,5500,3000,3500,4000,6000,6500,3000,3500
Twitter,3000,3500,4000,3000,2500,2000,1500,1000,500
Instagram,2000,4500,5000,5500,5000,4500,4000,8500,8000
Snapchat,1000,2000,3000,2000,1000,800,600,400,200
LinkedIn,2000,2500,3000,3500,4000,4500,5000,5500,6000
""")
data_df = pd.read_csv(data_string)

data = [data_df[col].values for col in data_df.columns if col != 'Platform']

fig, ax = plt.subplots(figsize =(10, 7))
bp = ax.boxplot(data, patch_artist = True,
                notch = True, vert = 0, widths = 0.5)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_yticklabels(data_df.columns[1:])
ax.set_xlabel('Popularity')
ax.set_ylabel('Years')
ax.set_title('Popularity of Social Media Platforms Over 9 Years')

for i in range(len(data_df.columns[1:])):
    ax.text(data[i].mean(), i+1, f'{data[i].mean():.2f}', horizontalalignment='center', verticalalignment='center')

ax.set_facecolor('lightgray')
ax.grid(True)
plt.tight_layout()
plt.savefig('myplot.png')

# Update the visibility of the median line of the box that contain the center point of the bounding box to False.
# For those same box, set the z-order of its body to 6.
# Additionally, apply a stroke effect to the box body with an offset of (3.93, 3.50) and shadow color of red.