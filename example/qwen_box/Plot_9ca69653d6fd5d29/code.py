from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Creating a DataFrame from the given csv data
data = {"Households": ["Single Household", "Couple Household", "Family Household", "Multi-Generational Household", "Shared Housing", "Student Housing", "Retired Household"],
        "2018": [350, 500, 800, 1200, 600, 250, 700],
        "2019": [330, 400, 600, 1300, 700, 150, 650],
        "2020": [500, 420, 1200, 850, 650, 200, 700]}
df = pd.DataFrame(data)

# Setting the style of the plot
plt.style.use('seaborn-whitegrid')

# Creating the figure and the axes
fig, ax = plt.subplots()

# Plotting the data
for i in range(len(df)):
    ax.plot(df.columns[1:], df.iloc[i, 1:], label=df.iloc[i, 0], linewidth=1.5, linestyle='-', marker='o', markersize=5, alpha=0.7)

# Setting the title and labels
ax.set_title('Household types over the years')
ax.set_xlabel('Year')
ax.set_ylabel('Number of households')

# Setting the legend
ax.legend(loc='upper left')

# Changing the background color
ax.set_facecolor('lightgray')

# Saving the figure
plt.tight_layout()
plt.savefig("myplot.png")