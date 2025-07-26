from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Creating dataframe from the given data
data = {'Country': ['USA', 'India', 'Brazil', 'China', 'Nigeria'],
        'Literacy Rate (%)': [98, 74, 92, 96, 60]}
df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize =(10, 7))
ax.set_facecolor('lightgray')  # setting the background color of the plot
ax.grid(True)  # adding grids on the background

# Creating box plot
bp = ax.boxplot(df['Literacy Rate (%)'], patch_artist = True, notch = True, vert = 0, whis=2, widths=0.5, sym='ro')

colors = ['#008000']  # Changed the color code to green

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# adding annotations
for i in range(len(df['Literacy Rate (%)'])):
    plt.text(i+1, df['Literacy Rate (%)'][i], df['Literacy Rate (%)'][i], ha = 'center')

plt.title('Boxplot of Literacy Rate in Different Countries')  # Adding the title
plt.xlabel('Country')  # Adding the label for x-axis
plt.ylabel('Literacy Rate (%)')  # Adding the label for y-axis
plt.legend([bp["boxes"][0]], ['Literacy Rate'], loc='upper right')  # Adding legend

plt.tight_layout()
plt.savefig("myplot.png")