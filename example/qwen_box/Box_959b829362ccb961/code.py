from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Given data
data = StringIO('''\
Platform,2016,2017,2018
Facebook,100,120,85
Instagram,80,110,130
Twitter,90,70,95
Snapchat,70,100,70
LinkedIn,60,80,85
Pinterest,50,75,55
Reddit,30,60,65
WeChat,20,40,45
WhatsApp,10,5,30
''')

df = pd.read_csv(data)

# Prepare data for box plot
plot_data = [df['2016'], df['2017'], df['2018']]

fig, ax = plt.subplots(figsize =(10, 7))

# Creating box plot with customized labels
bp = ax.boxplot(plot_data, patch_artist = True, notch = True, vert = 0, 
                labels = ['2016', '2017', '2018'], 
                sym = "ro", widths = 0.4)

colors = ['#0000FF', '#00FF00', '#FFFF00']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Setting titles and labels
plt.title("Platform vs Yearly User Count")
plt.xlabel("Year")
plt.ylabel("User Count in Millions")

# Adding legend
plt.legend([bp["boxes"][0], bp["boxes"][1], bp["boxes"][2]], ['2016', '2017', '2018'], loc='upper right')

# Adding grid
plt.grid(True)

# Change the facecolor of the figure
fig.patch.set_facecolor('lightgray')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")