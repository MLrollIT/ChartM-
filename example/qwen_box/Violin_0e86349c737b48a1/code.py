import pandas as pd
# Necessary Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Data
crater_depths = {
    'Mare Serenitatis': [10, 12, 8, 16, 14, 11, 9, 13],
    'Crisium Basin': [18, 20, 22, 16, 19, 21, 17, 15],
    'Plato Crater': [14, 11, 12, 10, 13, 15, 9, 16]
}

# Prepare data for seaborn
data = []
labels = []
for label, depths in crater_depths.items():
    data.extend(depths)
    labels.extend([label]*len(depths))

# violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x=labels, y=data)
plt.title('Lunar Crater Depth Analysis')
plt.xlabel('Lunar Region')
plt.ylabel('Crater Depth (in meters)')

# Change the color of the violin enclosed by the bounding box to #053a33 and set its transparency to 0.42
violin = plt.gca().violinplot(data, labels=labels, showmeans=False, showmedians=False, showextrema=False)
violin['bodies'][1].set_facecolor('#053a33')
violin['bodies'][1].set_alpha(0.42)

plt.tight_layout()
plt.savefig("figure.png")