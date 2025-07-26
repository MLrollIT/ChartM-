# Necessary Libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
transportation_modes = ['Car', 'Bus', 'Bicycle', 'Walking']
data = [[350, 400, 330, 380, 360, 365, 350, 390, 400, 375], [100, 120, 110, 105, 98, 103, 108, 100, 112, 115], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Data Preparation
data_dict = dict(zip(transportation_modes, data))
df = pd.DataFrame(data_dict)

# Plot
plt.figure(figsize=(10,6))
sns.violinplot(data=df)

plt.title('Energy Consumption Patterns and Carbon Footprint of Different Transportation Modes')
plt.xlabel('Transportation Modes')
plt.ylabel('Energy Consumption & Carbon Footprint (kgCO2e)')

# Change the color of the violin that contains the center point of the bounding box to #ba3ace and set its transparency to 0.37
violin = plt.gca().violinplot(data, showmeans=True, showextrema=False, showmedians=True)
violin['bodies'][0].set_facecolor('#ba3ace')
violin['bodies'][0].set_alpha(0.37)

plt.tight_layout()
plt.savefig("figure.png")