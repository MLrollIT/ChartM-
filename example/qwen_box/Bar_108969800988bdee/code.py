from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# The given data in csv format
data = StringIO("""
"Year","Asia","Africa"
2000,120,160
2005,80,180
2010,110,190
""")

# Reading the data into a pandas dataframe
df = pd.read_csv(data, sep=",")

# The label locations
x = np.arange(len(df["Year"]))  

# The width of the bars
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))

# Creating the bar chart with updated colors and edge colors
bars1 = ax.bar(x - width/2, df["Asia"], width, label='Asia', color='magenta', edgecolor='white')
bars2 = ax.bar(x + width/2, df["Africa"], width, label='Africa', color='cyan', edgecolor='white')

# Adding labels, title and custom x-axis tick labels
ax.set_ylabel('Population (in millions)')
ax.set_title('Population comparison between Asia and Africa')
ax.set_xticks(x)
ax.set_xticklabels(df["Year"])
ax.legend()

# Annotating the data value on the chart
ax.bar_label(bars1, padding=3)
ax.bar_label(bars2, padding=3)

# Setting background color and grid
ax.set_facecolor('gray')
ax.grid(True)

# Change the transparency of the bars that share the same legend with the bar that contains the center point of the bounding box to 0.90 and set their visibility to False.
for bar in bars1:
    if bar.get_label() == 'Asia':
        bar.set_alpha(0.90)
        bar.set_visible(False)

for bar in bars2:
    if bar.get_label() == 'Africa':
        bar.set_alpha(0.90)
        bar.set_visible(False)

plt.tight_layout()
plt.savefig("myplot.png")