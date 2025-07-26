import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input data
depths = ['0m']*5 + ['50m']*5 + ['100m']*5 + ['200m']*5 + ['500m']*5 + ['1000m']*5 + ['2000m']*5 + ['3000m']*5 + ['4000m']*5
zones = ['Surface']*15 + ['Mesopelagic']*15 + ['Bathypelagic']*15
abundance = [1000, 1200, 800, 1100, 900, 600, 700, 800, 500, 650, 400, 450, 500, 350, 300, 200, 250, 300, 180, 220, 150, 180, 200, 120, 160, 100, 120, 150, 80, 110, 50, 60, 70, 40, 55, 30, 40, 50, 25, 35, 20, 25, 30, 15, 18]

# Create DataFrame
df = pd.DataFrame({'Depth': depths, 'Zone': zones, 'Abundance': abundance})

# Create violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x="Depth", y="Abundance", hue="Zone", data=df)
plt.title('Oceanic Microbe Abundance Distribution')
plt.xlabel('Depth')
plt.ylabel('Abundance (cells per ml)')

# Change the face color of the violin that contains the center point of the bounding box to #44f759
violin = plt.gca().violinplot(df, positions=[7.5], showmeans=False, showmedians=False, showextrema=False)
violin['bodies'][0].set_facecolor('#44f759')
violin['bodies'][0].set_rasterized(True)

plt.tight_layout()
plt.savefig("figure.png")