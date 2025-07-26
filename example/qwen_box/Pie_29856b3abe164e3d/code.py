from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Data
labels = ["Anxiety", "Depression", "Bipolar Disorder", "Schizophrenia",
          "Post-Traumatic Stress Disorder", "Eating Disorders",
          "Attention Deficit Hyperactivity Disorder", "Obsessive-Compulsive Disorder", "Others"]
sizes = [25, 20, 15, 10, 10, 5, 7, 5, 3]

# Create figure and axis
fig, ax = plt.subplots()

# Set background color
fig.patch.set_facecolor('gray')

# Plot pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', pctdistance=0.85, labeldistance=1.1, colors=plt.cm.Pastel1.colors)

# Draw white circle at the center
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Add title, legend
plt.title("Prevalence of Mental Health Disorders") 
plt.legend(labels, title="Disorders", loc="upper right") 

# Modify the label of the slice that contains the center point of the bounding box to 'A new Label' and set its snap state to False
ax.patches[0].label2text.set_text('A new Label')
ax.patches[0].set_snap(False)

# Tight layout and save figure
plt.tight_layout()
plt.savefig("myplot.png")