from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Define the time periods and corresponding traffic volumes
time_periods = ["Morning Rush Hour", "Afternoon Lull", "Evening Rush Hour", "Late Night"]
traffic_volumes = [12000, 6000, 14000, 2000]

# Convert the traffic volumes to a numpy array and reshape it for the heatmap
traffic_volumes_np = np.array(traffic_volumes).reshape(len(time_periods), 1)

# Create the figure and axis objects
fig, ax = plt.subplots()

# Create the heatmap using the traffic volumes data
# Use a grayscale colormap and set the alpha parameter to 0.7
im = ax.imshow(traffic_volumes_np, cmap='gray', alpha=0.7)

# Set the x and y ticks and their labels
ax.set_xticks(np.arange(1))
ax.set_yticks(np.arange(len(time_periods)))
ax.set_xticklabels(['Traffic Volume'])
ax.set_yticklabels(time_periods)

# Rotate the x tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over the traffic volumes data and create text annotations for each value
for i in range(len(time_periods)):
    text = ax.text(0, i, traffic_volumes_np[i, 0], ha="center", va="center", color="w")

# Set the title of the heatmap
ax.set_title("Traffic Volumes at Different Times of Day")

# Add a grid to the background
ax.grid(True)

# Set the background color to a light gray
ax.set_facecolor('lightgray')

# Adjust the layout to make sure everything fits properly
plt.tight_layout()

# Save the figure
plt.savefig("myplot.png")