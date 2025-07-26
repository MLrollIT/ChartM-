# Required Libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
renewable_energy = [12, 15, 18, 20, 22, 24, 26, 29, 33, 36, 38, 40, 42, 45, 48, 50, 53, 57, 60, 64, 68, 72, 76, 80, 85]
nonrenewable_energy = [80, 85, 88, 92, 95, 98, 102, 105, 110, 112, 115, 118, 120, 122, 124, 126, 128, 130, 133, 135, 138, 140, 142, 144, 146]
nuclear_energy = [5, 8, 10, 12, 14, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73]

# Combine Data
data = [renewable_energy, nonrenewable_energy, nuclear_energy]
labels = ['Renewable', 'Non-Renewable', 'Nuclear']

# Create Violin plot
plt.figure(figsize=(10,6))
sns.violinplot(data=data)
plt.xticks([0, 1, 2], labels)

# Title and Labels
plt.title('Global Energy Consumption by Source Over The Past 50 Years')
plt.xlabel('Energy Source')
plt.ylabel('Energy Consumption')

# Update fill pattern and color of the violin containing the center point of the bounding box
violin = plt.gca().violinplot(data, labels=labels, showmeans=True, showextrema=False)
violin['bodies'][1].set_hatch('/')
violin['bodies'][1].set_facecolor('#524cc6')

# Display plot
plt.tight_layout()
plt.savefig("figure.png")