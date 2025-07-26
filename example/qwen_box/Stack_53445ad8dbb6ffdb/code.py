import matplotlib.pyplot as plt

# Clusters
clusters = [1, 2, 3]

# Data Points
blue_giants = [45, 60, 30]
red_giants = [35, 25, 45]
white_dwarfs = [20, 15, 25]

# Plot
fig, ax = plt.subplots()

ax.stackplot(clusters, blue_giants, red_giants, white_dwarfs, labels=['Blue Giants','Red Giants','White Dwarfs'], alpha=0.7)

# Labeling
plt.title('Density mapping of Galactic Clusters based on stellar types')
plt.xlabel('Clusters (1, 2, 3)')
plt.ylabel('Density of Clusters')

# Set the legend
plt.legend(loc='upper left')

# Update the label of the areas that contain the center point of the bounding box to 'A new Label'
bbox = ax.bbox_to_anchor([0.5, 0.5, 0.3, 0.3], transform=ax.transData)
bbox.update(dict(boxstyle='square', ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8)))

# Display the stack plot
plt.tight_layout()
plt.savefig("Edit_figure.png")