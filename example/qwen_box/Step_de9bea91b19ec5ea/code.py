# import the required libraries
import matplotlib.pyplot as plt

# Time points
time_points = [0, 5, 10, 15, 20]

# Neural activity data for each region
frontal_cortex = [75, 80, 85, 90, 95]
hippocampus = [60, 65, 70, 75, 80]
amygdala = [50, 55, 60, 65, 70]
thalamus = [40, 45, 50, 55, 60]

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the data with 'step' style for each region
ax.step(time_points, frontal_cortex, where='mid', label='Frontal Cortex')
ax.step(time_points, hippocampus, where='mid', label='Hippocampus')
ax.step(time_points, amygdala, where='mid', label='Amygdala')
ax.step(time_points, thalamus, where='mid', label='Thalamus')

# Set additional properties for the plot
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Neural Activity (Hz)')
ax.set_title('Neural Activity Mapping in Different Brain Regions During a Cognitive Task')
ax.legend(loc='upper left')
ax.grid(True)

# Overlay a dashed step line on the section of the step chart that contains the center point of the bounding box to create a glow effect
bbox = ax.bbox_to_anchor([0.5, 0.5, 0.1, 0.1])
ax.plot([bbox.x0, bbox.x0, bbox.x0 + bbox.width, bbox.x0 + bbox.width, bbox.x0], [bbox.y0, bbox.y0 + bbox.height, bbox.y0 + bbox.height, bbox.y0, bbox.y0], dashes=[15, 10], color='#0cb484', alpha=0.5)

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")