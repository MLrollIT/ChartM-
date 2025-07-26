from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

# Define labels and sizes based on the given data
labels = 'Sofa', 'Bed', 'Dining Table', 'Coffee Table', 'Armchair', 'Wardrobe'
sizes = [20, 25, 15, 10, 20, 10]

# Create a new figure and axes
fig, ax = plt.subplots()

# Set the background color of the figure to white
fig.set_facecolor('white')  # Changed from 'gray' to 'white'

# Create the pie chart
ax.pie(sizes, labels=labels, autopct='%.0f%%', explode=(0, 0.14147942417002493, 0, 0, 0, 0), 
       textprops={'size': 'smaller'}, radius=0.5, shadow=True, pctdistance=0.85,
       colors=['red', 'blue', 'green', 'orange', 'purple', 'brown'])

# Add title, x and y axis labels
plt.title("Distribution of Furniture Type") 
plt.xlabel("Percentage")
plt.ylabel("Furniture Type")

# Add legend
plt.legend(labels, title="Furniture Type", loc="upper right") 

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")