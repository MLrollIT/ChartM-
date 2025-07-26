from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = StringIO("""
Country,2000,2010,2020
USA,30.5,35.7,42.4
UK,23.0,26.9,28.0
Australia,21.7,24.6,31.3
China,5.5,12.2,14.3
India,3.8,5.2,9.5
Brazil,11.4,15.8,22.1
""")
df = pd.read_csv(data)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars = ax.bar(df['Country'], df['2020'], color='skyblue', edgecolor='black')

# Set title, x-label and y-label with increased font size
ax.set_title('Country Population in 2020', fontsize=16) # Changed font size here
ax.set_xlabel('Country', fontsize=14) # Changed font size here
ax.set_ylabel('Population', fontsize=14) # Changed font size here

# Add grid
ax.grid(True, which='both')

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend with increased font size
ax.legend(["Population"], loc='upper right', fontsize=12) # Changed font size here

# Add the corresponding value at the end of each bar
ax.bar_label(bars)

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")