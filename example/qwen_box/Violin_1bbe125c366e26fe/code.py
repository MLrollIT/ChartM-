import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Elevation Data
Valles_Marineris = [1200, 1300, 1250, 1350, 1400, 1100, 1150, 1250]
Olympus_Mons = [1600, 1700, 1800, 1750, 1650, 1550, 1700, 1850]
Hellas_Planitia = [900, 950, 1000, 1050, 1100, 950, 1000, 1050]

# Create data frame
data = {
    'Region': ['Valles Marineris']*len(Valles_Marineris) + ['Olympus Mons']*len(Olympus_Mons) + ['Hellas Planitia']*len(Hellas_Planitia),
    'Elevation': Valles_Marineris + Olympus_Mons + Hellas_Planitia
}

df = pd.DataFrame(data)

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Region', y='Elevation', data=df)
plt.title('Martian Terrain Elevation Mapping')

# Set clipping state and line width
for violin in plt.gca().violinplots()[0]:
    violin.set_clipping(True)
    violin.set_edgecolor('#773541')
    violin.set_edgewidth(2.64)

plt.tight_layout()
plt.savefig("figure.png")