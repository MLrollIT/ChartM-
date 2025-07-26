import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
shallow = [15, 10, 12, 17, 14, 11, 13, 16, 18, 14]
mid = [8, 12, 10, 15, 9, 11, 14, 8, 13, 12]
deep = [5, 7, 6, 9, 4, 8, 10, 6, 11, 7]

data = [shallow, mid, deep]
labels = ['Shallow', 'Mid', 'Deep']

# Create figure
fig, ax = plt.subplots()

# Create violin plot
sns.violinplot(data=data, ax=ax, rasterized=False, snap=True)

# Set labels
ax.set_xticklabels(labels)

# Set title and labels
plt.title('Distribution of Fish Species Counts in Different Zones')
plt.xlabel('Zones')
plt.ylabel('Fish Species Counts')

# Show plot

plt.tight_layout()
plt.savefig("figure.png")