from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Creating the figure and axis objects
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Set the face color of the figure
fig.patch.set_facecolor('gray')

# Dataset
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
progress = [25, 20, 30, 15, 10]

# Creating the pie chart
wedges, texts, autotexts = ax.pie(progress, explode=(0.1, 0, 0, 0, 0), labels=cities, autopct='%1.1f%%', shadow=True, startangle=90, colors=['red','blue','green','purple','orange'])

# Adding title and other enhancements
ax.set_title("Recycling Progress in Major U.S. Cities", fontsize=16)  # Changed title font size to 16
ax.legend(wedges, cities, title="Cities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=12, weight="bold")  # Changed label font size to 12
plt.setp(texts, size=12)  # Also change the font size of the legend to 12 to maintain consistency

plt.tight_layout()
plt.savefig("myplot.png")