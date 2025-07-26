from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# create the data
data = {
    "Household Type": ["Single Person Household", "Two-Person Household", "Three-Person Household", 
                       "Four-Person Household", "Five-Person Household", 
                       "Six or More Person Household", "Average Household"],
    "Food Waste (2019)": [450, 1000, 700, 800, 500, 1100, 720],
    "Food Waste (2020)": [550, 1100, 800, 600, 700, 1300, 790]
}

# convert the data to DataFrame
df = pd.DataFrame(data)

# set the figure size and create the box plots
fig, ax = plt.subplots(figsize =(10, 7))
bp = ax.boxplot([df["Food Waste (2019)"], df["Food Waste (2020)"]], patch_artist=True, notch=True, vert=0, widths=0.5)

# add special values
colors = ['#343323', '#676f85', '#06755b']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# set the x-axis and y-axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Food Waste')

# set the title
ax.set_title('Comparison of Food Waste between 2019 and 2020')

# add legend
ax.legend(["Food Waste (2019)", "Food Waste (2020)"])

# add grid
ax.grid(True)

# set the background color
ax.set_facecolor('lightgray')

# annotate the data value
for i, val in enumerate(df["Food Waste (2019)"]):
    ax.text(1, i, val, ha='center')
for i, val in enumerate(df["Food Waste (2020)"]):
    ax.text(2, i, val, ha='center')

plt.tight_layout()
plt.savefig('myplot.png')