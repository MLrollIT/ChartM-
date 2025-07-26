import matplotlib.pyplot as plt

# Genetic clustering scores dataset
clustering_scores = [0.36, 0.75, 0.42, 0.91, 0.63, 0.28, 0.87, 0.54, 0.69, 0.81, 0.71, 0.59, 0.95, 0.44, 0.60, 0.59, 0.71, 0.23, 0.69, 0.54, 0.76, 0.67, 0.82, 0.97, 0.26, 0.64, 0.58, 0.56, 0.59, 0.88, 0.29, 0.30, 0.66, 0.53, 0.65, 0.72, 0.50, 0.78, 0.49, 0.73]

# Creating histogram plot
plt.hist(clustering_scores, bins=10, color='skyblue', edgecolor='black')

# Add grid
plt.grid(True)

# Add labels and title
plt.xlabel('Clustering Scores')
plt.ylabel('Frequency')
plt.title('Genetic Clustering Scores Distribution')

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform((0.5, 0.5))

# Get the bar objects that contain the center point of the bounding box
bars = plt.gca().collections[0].get_paths()[0].vertices

# Adjust the opacity of the bars
for bar in bars:
    bar.set_alpha(0.5362)

# Apply a diagonal stripe pattern on the bars
for bar in bars:
    bar.set_edgecolor('black')
    bar.set_facecolor('skyblue')
    bar.set_hatch('/')

# Display plot
plt.tight_layout()
plt.savefig("figure.png")