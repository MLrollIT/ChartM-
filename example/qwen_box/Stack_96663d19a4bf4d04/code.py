import matplotlib.pyplot as plt

# Time intervals
time_intervals = [0, 100, 200, 300, 400, 500]

# Neural activity intensities for each brain region
frontal_cortex = [0.5, 1.2, 2.0, 2.5, 2.8, 3.0]
hippocampus = [0.3, 1.0, 1.8, 2.2, 2.6, 3.2]
amygdala = [0.2, 0.8, 1.5, 2.0, 2.3, 2.7]

# Preparing the stack plot
plt.stackplot(time_intervals, frontal_cortex, hippocampus, amygdala,
              labels=['Frontal Cortex','Hippocampus','Amygdala'],
              colors=['#6d904f','#fc4f30','#008fd5'])

# Assigning labels and title
plt.xlabel('Time Intervals (ms)')
plt.ylabel('Neural Activity Intensity')
plt.title('Neural Activity Mapping During Memory Recall Task')

# Adding legend
plt.legend(loc='upper left')

# Updating the transparency and face color of the area containing the center point of the bounding box
bbox = plt.gca().get_position().get_points()
bbox[0] = 100
bbox[1] = 2
bbox[2] = 100
bbox[3] = 2
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2] - bbox[0], bbox[3] - bbox[1], facecolor='#a7e997', alpha=0.3336))

# Display plot
plt.tight_layout()
plt.savefig("Edit_figure.png")