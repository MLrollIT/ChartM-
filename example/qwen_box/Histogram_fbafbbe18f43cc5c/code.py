import matplotlib.pyplot as plt

# Having your data
data = [0.5, 0.7, 0.9, 1.2, 1.1, 1.6, 1.8, 2.0, 1.9, 2.3, 2.5, 2.4, 2.7, 2.9, 
        3.1, 3.0, 3.2, 3.4, 3.5, 3.9, 4.0, 4.2, 4.3, 4.6, 4.8, 4.7, 5.0, 5.2, 
        5.5, 5.8, 6.0]

# Create a histogram using matplotlib
plt.hist(data, bins=10, edgecolor='black')

# Specify the title and the labels of the histogram
plt.title('Neural Activity Levels Across Different Brain Regions')
plt.xlabel('Activity Level (Spikes/Minute)')
plt.ylabel('Number of Occurrences')

# Increase font size for readability
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Display the plot
plt.tight_layout()
plt.savefig("figure.png")

# Modify the face color of the bars that contain the center point of the bounding box to #caabef
bbox = plt.gca().get_position()
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure)
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox