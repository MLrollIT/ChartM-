from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
demographics = ['Teenagers', 'Adults', 'Elderly', 'Infants']
sleep_hours = [6.5, 7.3, 5.2, 14.8]

# Setting up the figure and axes
fig, ax = plt.subplots()

# Creating the bar chart
bars = ax.bar(demographics, sleep_hours, color='skyblue', edgecolor='black')

# Annotating the data values on the bars
ax.bar_label(bars)

# Adding labels and title
ax.set_xlabel('Demographic')
ax.set_ylabel('Hours of Sleep')
ax.set_title('Average Sleep Duration by Age Group')

# Adding a grid and setting the background color
ax.grid(True)
ax.set_facecolor('lightgray')

# Using tight layout and saving the figure
plt.tight_layout()
plt.savefig("myplot.png")