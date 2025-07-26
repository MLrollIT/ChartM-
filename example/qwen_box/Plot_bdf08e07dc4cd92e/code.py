from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Define the data
data = {
    "Rose": [25, 30, 27, 40, 15],
    "Daisy": [15, 18, 20, 22, 50],
    "Lily": [10, 7, 5, 3, 25],
    "Sunflower": [35, 38, 40, 42, 80],
    "Orchid": [20, 45, 25, 50, 30]
}

# Define the x-axis values
x = np.arange(5)

# Define the line styles
styles = ['-', '--', '-.', ':', '-']

# Create a new figure
fig, ax = plt.subplots()

# Plot each line
for i, (species, growth) in enumerate(data.items()):
    ax.plot(x, growth, label=species, linestyle=styles[i], marker='o', markersize=5)

# Set the chart title and labels
ax.set_title('Growth Patterns of Different Plant Species')
ax.set_xlabel('Time')
ax.set_ylabel('Growth')

# Add a legend
ax.legend(loc='upper left')

# Remove grid
ax.grid(False)  # Changed from True to False

# Set background color to white
ax.set_facecolor('white')  # Changed from 'lightgray' to 'white'

# Save the figure
plt.tight_layout()
plt.savefig("myplot.png")