from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Data
internet_access = ["Mobile Internet","Satellite Internet","Dial-Up Internet","Fixed Wireless Internet","Cable Internet","DSL Internet","No Internet Access"]
percentage = [30, 15, 5, 15, 20, 10, 5]

# Define new color palette
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#C0C0C0', '#F08080']

# Create figure and axes
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Plot the pie chart with the new colors
wedges, texts, autotexts = ax.pie(percentage, explode=(0.1, 0, 0, 0, 0, 0, 0), labels=internet_access, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)

# Draw white circle in the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Set the background color
ax.set_facecolor('gray')

# Set the title
ax.set_title('Internet Access Type Distribution')

# Modify the label of the slice that contains the center point of the bounding box to 'A new Label'
for text in autotexts:
    text.set_text('A new Label')

# Set the linewidth of that slice to 3.92
for wedge in wedges:
    wedge.set_linewidth(3.92)

# Save figure
plt.tight_layout()
plt.savefig("myplot.png")