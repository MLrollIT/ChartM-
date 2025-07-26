from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Define the data
data = StringIO("""
"Social Media Platform","Monthly Active Users"
"Facebook",2.8
"Instagram",1.5
"Twitter",1.2
"Snapchat",0.5
"WeChat",1.1
"WhatsApp",2.0
""")
df = pd.read_csv(data, sep=",")
platforms = df['Social Media Platform'].tolist()
users = df['Monthly Active Users'].tolist()

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars = ax.bar(platforms, users, color='skyblue', edgecolor='black')

# Set title, x-label and y-label
ax.set_title('Monthly Active Users on Social Media Platforms')
ax.set_xlabel('Social Media Platforms')
ax.set_ylabel('Monthly Active Users (in billions)')

# Add grid
ax.grid(True, which='both')

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend
ax.legend(["Monthly Active Users"], loc='upper right')

# Add the corresponding value at the end of each bar
ax.bar_label(bars)

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")