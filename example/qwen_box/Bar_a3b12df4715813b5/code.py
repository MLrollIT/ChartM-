from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Define the data
data = StringIO("""
"Meat Type","Consumption (in million tonnes)"
"Beef",120
"Pork",150
"Poultry",200
"Lamb",80
"Fish",90
"Seafood",70
"Venison",50
"Goat",40
"Buffalo",30
""")
df = pd.read_csv(data, sep=",")
meat_types = df['Meat Type'].tolist()
consumption = df['Consumption (in million tonnes)'].tolist()

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars = ax.bar(meat_types, consumption, color='skyblue', edgecolor='black')

# Set title, x-label and y-label
ax.set_title('Meat Consumption')
ax.set_xlabel('Meat Type')
ax.set_ylabel('Consumption (in million tonnes)')

# Add grid
ax.grid(True)

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Adding bar labels
ax.bar_label(bars)

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")