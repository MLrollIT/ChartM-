import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chemical reactions:
reactions = ['Methane Oxidation', 'Ammonia Synthesis', 'Water Splitting']

# Reaction rates:
moles_per_litre_second = [
  [0.05, 0.04, 0.07, 0.06, 0.05, 0.06, 0.03, 0.08, 0.07, 0.05], # Methane Oxidation
  [0.02, 0.03, 0.01, 0.02, 0.03, 0.02, 0.02, 0.01, 0.03, 0.02], # Ammonia Synthesis
  [0.03, 0.02, 0.04, 0.03, 0.04, 0.03, 0.02, 0.05, 0.04, 0.03]  # Water Splitting
]

# Preparing data for violin plot
data = []
for reaction, rates in zip(reactions, moles_per_litre_second):
    for rate in rates:
        data.append([reaction, rate])

# Plot Settings
plt.figure(figsize=(10,6))
sns.violinplot(x=[item[0] for item in data], y=[item[1] for item in data])
plt.title('Violin plot of Reaction Rates in the Cosmos')
plt.xlabel('Chemical Reactions')
plt.ylabel('Reaction Rates (mol/L/s)')

# Change the color of the median line of the violin that contains the center point of the bounding box to #293201
plt.violinplot([item[1] for item in data], [item[0] for item in data], showmeans=True, showmedians=True, showextrema=False, widths=0.5, bw_method=0.5, points=100, scale='linear', cut=1, clip=False, vert=False, scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='linear', scale_hue=1, scale='