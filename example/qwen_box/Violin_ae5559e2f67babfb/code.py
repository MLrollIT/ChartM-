import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Star cluster ages
young_star_cluster_ages = [100, 110, 120, 105, 115, 112, 108, 125, 130, 118]
intermediate_star_cluster_ages = [500, 490, 510, 480, 495, 505, 515, 520, 485, 495]
old_star_cluster_ages = [1000, 980, 1020, 995, 1015, 990, 1005, 1025, 985, 1010]

# Combine all lists together
data = [young_star_cluster_ages, intermediate_star_cluster_ages, old_star_cluster_ages]
labels = ['Young', 'Intermediate Age', 'Old']

# Create the violin plot
plt.figure(figsize=(9, 6))
sns.violinplot(data=data)
plt.xticks([0, 1, 2], labels)

# Provide the title and labels
plt.title("Age Distribution of Star Clusters within the Milky Way Galaxy")
plt.xlabel("Star Cluster Age Group")
plt.ylabel("Age (Million Years)")

# Set the clipping for the violins that contain the center point of the bounding box to True
plt.setp(plt.violinplot(data), clip_on=True)

# Ensure that the rasterized state for these violins is set to False
plt.setp(plt.violinplot(data), rasterized=False)

plt.tight_layout()
plt.savefig("figure.png")