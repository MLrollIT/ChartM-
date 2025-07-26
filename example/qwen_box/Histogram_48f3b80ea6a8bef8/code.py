# Required Libraries
import matplotlib.pyplot as plt
import numpy as np

# Data
stress_levels = ['Low (0-3)', 'Moderate (4-7)', 'High (8-10)']
frequencies = [10, 25, 15]

# Create histogram
plt.bar(stress_levels, frequencies, color = ['green', 'yellow', 'red'])

# Add title and labels
plt.title('Distribution of Exam Stress Levels Among Students')
plt.xlabel('Stress Levels')
plt.ylabel('Number of Students')

# Modify the xlabel of the bars that contain the center point of the bounding box to 'A new Label' and set their rasterized state to False.
plt.bar(stress_levels[1], frequencies[1], label='A new Label', rasterized=False)

# Show Plot
plt.tight_layout()
plt.savefig("Edit_figure.png")