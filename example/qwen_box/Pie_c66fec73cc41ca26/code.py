from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
data = {
    "Year": ["2017", "2018", "2019", "2020"],
    "Percentage Change": [25, 30, 35, 10]
}

# Extract labels and sizes from the data
labels = data["Year"]
sizes = data["Percentage Change"]

fig, ax = plt.subplots()

ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size': 'smaller'}, radius=0.5,
       explode=(0.1, 0, 0, 0), labeldistance=1.2,
       shadow=True, pctdistance=0.8, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])

plt.title("Yearly Percentage Change") # Add title
plt.legend(labels, title="Year", loc="upper right") # Add legend

# Change the background color of the chart figure
fig.patch.set_facecolor('lightgray')

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")