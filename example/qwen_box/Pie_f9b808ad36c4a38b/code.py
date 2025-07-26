from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data preparation
data = {"Disease": ["Cancer", "Heart Disease", "Stroke", "Respiratory Diseases", "Diabetes", "Alzheimer's Disease", "Kidney Disease"],
        "Percentage": [20, 15, 10, 25, 15, 10, 5]}
df = pd.DataFrame(data)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

# Set the background color of the figure
fig.set_facecolor('gray')

# Create a pie chart
wedges, texts, autotexts = ax.pie(df['Percentage'], autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05))

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Set the title of the chart
plt.title('Percentage of Diseases')

# Add labels to the pie chart
labels = df['Disease']
plt.legend(wedges, labels, title ="Diseases", loc ="center left", bbox_to_anchor =(1, 0, 0.5, 1))

# Adjust layout to make room for the legend, and save the figure
plt.tight_layout()
plt.savefig("myplot.png")

# Set the clipping state of the slices that contain the center point of the bounding box to False
for wedge in wedges:
    wedge.set_clip_on(False)

# Change the linestyle of those same slices to 'dotted'
for wedge in wedges:
    wedge.set_linestyle('dotted')

plt.savefig("Edit_figure.png")