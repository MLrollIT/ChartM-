from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Data Preparation
subjects = ["Mathematics", "Science", "English", "History", "Arts","Physical Education"]
percentage = [20, 25, 30, 10, 10, 5]

# Define a new color palette
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Create Pie Chart
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(percentage, explode=(0.1, 0, 0, 0, 0, 0), labels=subjects, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)

# Draw white center for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')  

# Set the background color of the chart
ax.set_facecolor('gray')

# Title of the chart
plt.title('Subject Percentage Distribution')

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")