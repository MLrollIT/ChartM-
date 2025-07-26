from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
labels = 'Domestic Flights', 'International Flights', 'Business Class', 'Economy Class', 'First Class', 'Other Classes'
sizes = [35, 30, 10, 15, 5, 5]

# Create a pie chart
fig, ax = plt.subplots()

# Additional parameters
explode = (0.18784179777133542, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e., 'Domestic Flights')
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'purple', 'pink']

ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Add title and labels
plt.title("Air Travel Trends")
plt.xlabel("Types of Flights and Classes")
plt.ylabel("Percentage")

# Add legend
plt.legend(labels, title="Air Travel Categories", loc="upper right")

# Change the background color
fig.patch.set_facecolor('gray')

plt.tight_layout()
plt.savefig("myplot.png")