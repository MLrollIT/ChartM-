from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Define the data
age_groups = ["Under 18", "18-24", "25-34", "35-44", "45-54", "55+"]
percentages = [10, 15, 20, 25, 20, 10]

# Create the figure and the axes
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(percentages, explode=(0, 0, 0, 0.1, 0, 0), labels=age_groups, autopct='%1.1f%%', shadow=True, startangle=90)

# Set the title with a larger font size
ax.set_title("Distribution of Age Groups", fontsize=14)

# Set the color of the figure's background
fig.set_facecolor('lightgrey')

# Set properties of the legend with a larger font size
plt.legend(wedges, age_groups,
          title="Age Groups",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          fontsize=14)

# Increase the font size of the labels and autotexts
for text in texts:
    text.set_fontsize(14)
for autotext in autotexts:
    autotext.set_fontsize(14)

plt.tight_layout()
plt.savefig("myplot.png")