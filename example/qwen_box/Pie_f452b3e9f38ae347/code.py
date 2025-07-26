from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
types_of_tv_show = ["Drama", "Comedy", "Reality", "News", "Documentary"]
popularity_percentage = [35, 25, 15, 15, 10]

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Plotting the pie chart
wedges, texts, autotexts = ax.pie(popularity_percentage, explode=(0.1, 0, 0, 0, 0), labels=types_of_tv_show, autopct='%1.1f%%',
                                  shadow=True, startangle=90)

# Draw a donut chart
ax.set(aspect="equal", title='TV Show Popularity')

# Change the color of the figure background
fig.set_facecolor('lightgray')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")