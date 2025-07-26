from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from io import StringIO

# given csv data
data = StringIO("""
Household Type,Food Waste (2019),Food Waste (2020)
Single Person Household,450,550
Two-Person Household,1000,1100
Three-Person Household,700,800
Four-Person Household,800,600
Five-Person Household,500,700
Six or More Person Household,1100,1300
Average Household,720,790
""")

# convert csv data to pandas dataframe
df = pd.read_csv(data)

# Set the household types as the x-axis labels
households = df["Household Type"].values

# Set the food waste data for each year
food_waste_2019 = df["Food Waste (2019)"].values
food_waste_2020 = df["Food Waste (2020)"].values

# width of the bars
width = 0.35

# plot the bar chart
fig, ax = plt.subplots()

# create bars for 2019 and 2020 data
bars1 = ax.bar(np.arange(len(households)) - width/2, food_waste_2019, width, label='2019', color='skyblue', edgecolor='black')
bars2 = ax.bar(np.arange(len(households)) + width/2, food_waste_2020, width, label='2020', color='lightgreen', edgecolor='black')

# Add title, labels and legend
ax.set_title("Food Waste by Household Type in 2019 and 2020")
ax.set_xlabel("Household Type")
ax.set_ylabel("Food Waste (kg)")
ax.set_xticks(np.arange(len(households)))
ax.set_xticklabels(households)
ax.legend(loc="upper right")

# Annotate the data value on the chart figure
ax.bar_label(bars1)
ax.bar_label(bars2)

# Add grids on the background
ax.grid(True)

# Set the face color to a light color
ax.set_facecolor('lightgray')

# Save chart as a png file
plt.tight_layout()
plt.savefig("myplot.png")