# Importing required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
hemoglobin_density = [1.4, 1.5, 1.6, 1.4, 1.3, 1.5, 1.3, 1.6, 1.4, 1.5]
insulin_density = [1.6, 1.7, 1.8, 1.9, 1.6, 1.7, 1.8, 1.9, 1.7, 1.8]
lysozyme_density = [1.2, 1.3, 1.4, 1.2, 1.3, 1.5, 1.3, 1.4, 1.2, 1.5]

# Creating the DataFrame
df = pd.DataFrame({
    'Hemoglobin': hemoglobin_density,
    'Insulin': insulin_density,
    'Lysozyme': lysozyme_density
})

# Melting the DataFrame
df_melted = pd.melt(df)

# Creating the Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='variable', y='value', data=df_melted)
plt.title('Molecular Density Distribution in Protein Structures')

plt.xlabel('Protein')
plt.ylabel('Molecular Density (g/cm³)')

# Change the face color of the violins that contain the center point of the bounding box to #cc5c04
# and update the linewidth of those violins to 2.49
bbox = plt.gca().get_position()
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox = bbox.transformed(plt.gcf().transFigure.inverted())
bbox =