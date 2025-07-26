import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
inner_rim = [4.2, 3.9, 4.5, 4.0, 4.2, 4.1, 3.8, 4.3, 4.4, 4.1]
mid_rim = [2.8, 3.1, 3.0, 2.9, 3.2, 3.3, 3.1, 3.0, 3.2, 2.7]
outer_rim = [1.5, 1.7, 1.4, 1.6, 1.8, 1.9, 1.6, 1.7, 1.5, 1.8]

# Combining the data and creating labels
densities = inner_rim + mid_rim + outer_rim
sectors = ['Inner Rim'] * len(inner_rim) + ['Mid Rim'] * len(mid_rim) + ['Outer Rim'] * len(outer_rim)

# Creating a data frame
df = pd.DataFrame({'Galactic Sector': sectors, 'Planet Densities': densities})

# Ploting the violin plot
plt.figure(figsize=(9, 6))
sns.violinplot(x='Galactic Sector', y='Planet Densities', data=df)
plt.title('Galactic Planet Density Distribution')

# Change the edge color of the violin that contains the center point of the bounding box to #cd21eb
plt.gca().violinplot([df[df['Galactic Sector'] == 'Mid Rim']['Planet Densities']], showmeans=True, showextrema=False, showmedians=True, widths=0.5, plot_properties={'color': '#cd21eb'}, cut=0)

plt.tight_layout()
plt.savefig("figure.png")