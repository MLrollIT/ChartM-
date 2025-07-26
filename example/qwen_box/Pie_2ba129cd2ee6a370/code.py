from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
labels = 'Positive Impact', 'Negative Impact', 'No Impact'
sizes = [30, 50, 20]

fig, ax = plt.subplots()

# Optional parameters
explode = (0.1, 0, 0)  # "explode" the 1st slice (i.e., 'Positive Impact')

# New color scheme using hexadecimal values
colors = ['#99ff99', '#ff6666', '#66b3ff']  # Light green, light red, light blue

ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

ax.set_facecolor('white')  # Change the background color to white
plt.title("Social Media Impact")  # Add title
plt.legend(labels, title="Impact Type", loc="upper right")  # Add legend

plt.tight_layout()
plt.savefig("myplot.png")