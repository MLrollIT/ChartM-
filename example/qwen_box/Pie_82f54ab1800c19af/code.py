from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Residential Property", "Commercial Property", "Industrial Property", 
              "Rural Property", "Rental Rates", "Property Taxes", 
              "Interest Rates", "Construction Costs", "Property Insurance"]

percentages = [20, 15, 15, 10, 10, 10, 10, 5, 5]

# Figure and axis
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Set background color
fig.patch.set_facecolor('#f2f2f2')  # Light grey background
ax.set_facecolor('#f2f2f2')

# Pie chart
wedges, texts, autotexts = ax.pie(percentages, explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0), 
                                   labels=categories, autopct='%1.1f%%', 
                                   shadow=True, startangle=90)

# Adding gridlines - not typically done for pie charts, but adding for instruction
# Since pie charts do not have gridlines, this step does nothing
# If you want to add lines, you'd need to draw them manually or change the chart type

# Draw white circle at the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Title
plt.title("Distribution of Property-Related Costs")

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")