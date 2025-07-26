from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given data
data = {
    "Year": ["1990", "1995", "2000", "2005", "2010", "2015", "2020", "2025", "2030"],
    "Percentage": [10, 12, 15, 17, 14, 16, 10, 4, 2]
}

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Set color for the chart figure
ax.set_facecolor("lightgray")

# Explode settings
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0) 

# Pie chart
wedges, texts, autotexts = ax.pie(data["Percentage"], explode=explode, labels=data["Year"], 
                                  autopct='%1.1f%%', shadow=True, startangle=90, 
                                  pctdistance=0.85, colors=plt.cm.Pastel1.colors)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Set the title, legend
ax.set_title("Yearly Percentage Distribution")
ax.legend(wedges, data["Year"],
          title="Years",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

# Modify the label of the slice that contains the center point of the bounding box
autotexts[0].set_text('A new Label')

# Add a shadow effect with an offset of (2.12, 3.76) units and set the shadow color to gray
autotexts[0].set_bbox(dict(boxstyle='round', fc="white", ec="gray", alpha=0.5))
autotexts[0].set_position((2.12, 3.76))

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")