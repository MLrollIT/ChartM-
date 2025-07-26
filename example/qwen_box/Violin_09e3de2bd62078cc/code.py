import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the datasets
A = [0.34, 0.28, 0.42, 0.39, 0.25, 0.31, 0.37, 0.41, 0.29, 0.33]
B = [0.45, 0.39, 0.58, 0.47, 0.55, 0.42, 0.49, 0.51, 0.44, 0.48]
C = [0.61, 0.56, 0.49, 0.63, 0.58, 0.52, 0.59, 0.55, 0.57, 0.60]
D = [0.72, 0.68, 0.76, 0.69, 0.74, 0.71, 0.67, 0.73, 0.75, 0.70]
E = [0.83, 0.88, 0.79, 0.85, 0.81, 0.87, 0.82, 0.76, 0.84, 0.80]

# Prepare a cumulative data list and labels
data = [A, B, C, D, E]
labels = ['Galaxy A', 'Galaxy B', 'Galaxy C', 'Galaxy D', 'Galaxy E']

# Creates violin plot
plt.figure(figsize=(10,6))
sns.violinplot(data=data)
plt.title('Distribution of Cosmic Dust Levels in Five Different Galaxies')
plt.xlabel('Galaxy')
plt.ylabel('Cosmic Dust Level')

# Set labels
plt.xticks(range(len(data)), labels)

# Modify the clipping state of the violins that contain the center point of the bounding box to False
bbox = plt.gca().get_position().bounds
bbox = [bbox[0], bbox[1], bbox[2], bbox[1] + bbox[3]]
plt.gca().set_position(bbox)
plt.tight_layout()
plt.savefig("figure.png")