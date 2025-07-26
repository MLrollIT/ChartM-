from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
labels = 'Consumer Adoption', 'Government Fleet Adoption', 'Commercial Fleet Adoption', 'Public Transport Adoption'
sizes = [30, 25, 35, 10]

fig, ax = plt.subplots()

# Additional parameters
explode = (0.1, 0, 0, 0) # Explode 1st slice
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plotting the pie chart
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140, 
       labeldistance=1.15, pctdistance=0.85)

# Setting title and legend
plt.title("Electric Vehicle Adoption Trend")
plt.legend(labels, title="Adoption Types", loc="upper right")

# Changing the background color
fig.patch.set_facecolor('grey')

# Ensuring a tight layout and saving the figure
plt.tight_layout()
plt.savefig("myplot.png")