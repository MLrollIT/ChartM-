from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
age_groups = ['Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
study_hours_percentage = [20, 25, 15, 10, 15, 10, 5]

fig, ax = plt.subplots()

# Additional parameters
explode = (0.1, 0, 0, 0, 0, 0, 0)  # Only "explode" the first slice (i.e. 'Under 18')

# Updated color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

ax.pie(study_hours_percentage, explode=explode, labels=age_groups, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)

# Draw the pie chart such that the angles start and end vertically
ax.axis('equal')

plt.title("Distribution of Study Hours by Age Group") # Add title
plt.legend(age_groups, title="Age Groups", loc="upper right") # Add legend
fig.patch.set_facecolor('gray') # Change the background color of the chart figure
plt.tight_layout() # Adjust the padding between and around the subplots

plt.savefig("myplot.png")