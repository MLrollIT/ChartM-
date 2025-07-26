from io import StringIO
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Define the data
region = ["North America", "Europe", "Africa"]
internet_users = [[250, 260, 270, 275, 280, 290, 295, 300, 305, 200, 205, 210],
                  [275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330],
                  [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
bars = []
for i, users in enumerate(internet_users):
    bar = ax.bar(np.arange(len(users)) + i/len(region), users, 
                 color=['skyblue', 'lightgreen', 'orange'][i], 
                 edgecolor='black', 
                 tick_label=range(1, len(users) + 1))
    bars.append(bar)

# Set title, x-label and y-label
ax.set_title('Internet Users Over Time')
ax.set_xlabel('Time (in years)')
ax.set_ylabel('Internet Users (in millions)')

# Add grid
ax.grid(True, which ='both')

# Set the background color of the plot to white
ax.set_facecolor('white')  # Modified line

# Add legend
ax.legend(region, loc='upper right')

# Add labels to each bar
for bar in bars:
    ax.bar_label(bar)

# Ensure the plot is displayed correctly with multiple plots in a single Notebook cell
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")