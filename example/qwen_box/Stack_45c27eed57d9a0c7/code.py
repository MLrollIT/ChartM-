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

# Change the face color of the area that contains the center point of the bounding box to #b0ddb5
bbox = plt.gca().collections[0].get_paths()[0].vertices
bbox[2] = [200, 2.5]
plt.gca().collections[0].set_paths([bbox])

# Display plot

plt.tight_layout()
plt.savefig("figure.png")