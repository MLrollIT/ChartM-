from io import StringIO
import numpy as np

from io import StringIO
import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = StringIO("""
Region,Water_Pollution_Index
North America,50
Asia,80
Africa,70
Europe,40
""")
df = pd.read_csv(data, sep =",")

regions = df["Region"].tolist()
pollution_index = df["Water_Pollution_Index"].tolist()

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars = ax.bar(regions, pollution_index, color='skyblue', edgecolor='black')

# Set title, x-label and y-label
ax.set_title('Water Pollution Index by Region')
ax.set_xlabel('Region')
ax.set_ylabel('Water Pollution Index')

# Add grid
ax.grid(True, which='both')

# Set the background color of the plot
ax.set_facecolor('lightgray')

# Add legend
ax.legend(["Water Pollution Index"], loc='upper right')

# Annotate data values on the bars
ax.bar_label(bars)

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")