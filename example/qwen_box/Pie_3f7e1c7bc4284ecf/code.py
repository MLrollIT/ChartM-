from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Given Data
industries = ["Power Plants", "Transportation", "Residential and Commercial Buildings",
              "Industrial Processes", "Agriculture", "Waste Management", "Deforestation", 
              "Others"]

percentages = [30, 20, 15, 10, 10, 5, 5, 5]

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(percentages, autopct='%1.1f%%', 
                                  pctdistance=0.85, labeldistance=1.1, 
                                  explode=[0.05]*8, shadow=True,
                                  startangle=140)

# Draw a white circle in the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Add a title
plt.title('Percentage Distribution of Industries')

# Add a legend
plt.legend(wedges, industries, title="Industries", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Change the background color
ax.set_facecolor('gray')

# Change the color of the slice that contains the center point of the bounding box to #0f7a01
for wedge in wedges:
    if wedge.get_label() == 'Others':
        wedge.set_facecolor('#0f7a01')

# Ensuring the figure is not cut off when saving
plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')