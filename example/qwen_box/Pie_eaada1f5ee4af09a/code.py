from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Data
decades = ["1960s", "1970s", "2000s and beyond"]
percentages = [30, 35, 35]

# Create figure and axis
fig, ax = plt.subplots()

# Pie chart
explode = (0.1, 0, 0)  # only "explode" the 1st slice (i.e. '1960s')
ax.pie(percentages, explode=explode, labels=decades, autopct='%1.1f%%', shadow=True, startangle=90)

# Title and labels
ax.set_title("Decades' Percentage")
plt.xlabel('Decades')
plt.ylabel('Percentage')

# Legend
plt.legend(decades, title="Decades", loc="upper right")

# Change the background color
fig.set_facecolor('gray')

# Layout and save
plt.tight_layout()
plt.savefig("myplot.png")