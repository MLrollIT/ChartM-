from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
book_types = ["Fantasy", "Science Fiction", "Mystery", "Romance", "Biography", "Non-Fiction", "Children's Books", "Others"]
percentages = [20, 15, 15, 10, 10, 15, 10, 5]

fig, ax = plt.subplots()

# Additional parameters
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 1st slice (i.e. 'Fantasy')

ax.pie(percentages, explode=explode, labels=book_types, autopct='%1.1f%%', shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')

# Customizations: Title, labels, and legend
plt.title("Percentage of Book Types")  # Add title
plt.xlabel("Book Types")  # Add x-label
plt.ylabel("Percentage")  # Add y-label
plt.legend(book_types, title="Book Types", loc="upper right")  # Add legend

# Set background color of the figure to gray
fig.set_facecolor('gray')

# Use tight_layout to automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")