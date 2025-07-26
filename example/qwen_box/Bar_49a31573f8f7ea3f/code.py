from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Define the data
data = StringIO("""
"Diet Type","2010","2015","2020"
"Vegetarian",10,15,9
"Vegan",5,10,8
"Paleo",20,35,20
"Keto",5,15,5
""")

df = pd.read_csv(data, sep=",")
diet_types = df["Diet Type"].values
values_2010 = df["2010"].values
values_2015 = df["2015"].values
values_2020 = df["2020"].values

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10,7))

# Plot the data
bars1 = ax.bar(diet_types, values_2010, color='skyblue', edgecolor='black')
bars2 = ax.bar(diet_types, values_2015, bottom=values_2010, color='lightgreen', edgecolor='black')
bars3 = ax.bar(diet_types, values_2020, bottom=values_2010+values_2015, color='orange', edgecolor='black')

# Set title, x-label and y-label
ax.set_title('Popularity of Different Diet Types Over the Years')
ax.set_xlabel('Diet Types')
ax.set_ylabel('Popularity')

# Add grid
ax.grid(True, which='both')

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend
ax.legend(["2010", "2015", "2020"], loc='upper right')

# Annotate the data value on the chart figure
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height() / 2,
                str(int(bar.get_height())), ha='center', va='center',
                color='black')

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")