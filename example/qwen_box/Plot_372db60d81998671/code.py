from io import StringIO
import numpy as np

import matplotlib.pyplot as plt

# Given data
households = ['Household A', 'Household B', 'Household C']
water_consumption = [45, 80, 22]

# Create a figure and an axes
fig, ax = plt.subplots()

# Plot the data with specific style and markers
ax.plot(households, water_consumption, linestyle='--', color='blue', marker='o', markersize=10, linewidth=2, alpha=0.7)

# Set the labels for x and y axes
ax.set_xlabel('Households')
ax.set_ylabel('Water Consumption (litres)')

# Set the title of the plot
ax.set_title('Water Consumption of Different Households')

# Add a grid
ax.grid(True)
ax.set_facecolor('lightgray')

# Add legend for the line
ax.legend(['Water Consumption'], loc='upper right')

# Annotate each line at the end of the line with the corresponding legend label
for i, txt in enumerate(water_consumption):
    ax.annotate(txt, (households[i], water_consumption[i]))

# Add a tight layout
plt.tight_layout()

# Save the figure
plt.savefig('myplot.png')