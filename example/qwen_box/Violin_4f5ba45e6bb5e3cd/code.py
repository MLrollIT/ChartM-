import pandas as pd
# Necessary Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Data
rocky_surfaces = [45, 50, 42, 48, 38, 55, 43, 47, 52, 40]
sandy_dunes = [30, 35, 28, 32, 37, 29, 31, 36, 34, 33]
crater_interiors = [15, 20, 18, 17, 22, 16, 19, 21, 23, 14]
mountainous_regions = [70, 65, 72, 68, 75, 66, 71, 73, 69, 74]

# Combine data for plotting
data = [rocky_surfaces, sandy_dunes, crater_interiors, mountainous_regions]
labels = ['Rocky Surfaces', 'Sandy Dunes', 'Crater Interiors', 'Mountainous Regions']

# Seaborn violinplot
sns.set(style='whitegrid')
plt.figure(figsize=(10,6))
sns.violinplot(data=data, inner='quartiles')
plt.xticks([0, 1, 2, 3], labels)
plt.ylabel('Elevation Level (m)')
plt.title('Elevation Levels across Different Terrains on Mars')

# Adjust transparency of violin containing center point of bounding box
violin = plt.gca().violinplot(data, labels=labels, showmeans=True, showextrema=False)
violin['bodies'][2].set_alpha(0.42)

plt.tight_layout()
plt.savefig("figure.png")