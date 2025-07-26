import matplotlib.pyplot as plt
import numpy as np

# Data points for Galactic Clustering in Dark Matter Model
galactic_clustering_distances = [18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94]

# Creating histogram plot
plt.figure(figsize=(8, 6))
plt.hist(galactic_clustering_distances, bins='auto', color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Galactic Clustering Distances')
plt.ylabel('Frequency')
plt.title('Galactic Clustering in Dark Matter Model Distribution')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

# Get the bounding box of the center point
bbox = plt.gca().bbox_to_transform(np.array([[0.5, 0.5]]))

# Get the bar objects that contain the center point
bar_objects = plt.gca().collections[0].get_paths()

# Set the transparency of the bars that contain the center point
for bar_object in bar_objects:
    if bar_object.contains_point(bbox.transform(np.array([[0.5, 0.5]]))):
        bar_object.set_alpha(0.5096)
        bar_object.set_facecolor('skyblue')
        bar_object.set_edgecolor('black')
        bar_object.set_hatch('x')

plt.savefig("figure.png")