import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = {
    "Fish": [150, 120, 140, 160, 130, 110, 170, 180, 125, 135],
    "Invertebrates": [80, 90, 100, 85, 95, 105, 110, 75, 85, 95],
    "Coral": [50, 60, 55, 65, 70, 45, 75, 65, 55, 50],
    "Algae": [40, 45, 50, 55, 60, 35, 65, 70, 40, 50]
}

# Create a dataframe
df = pd.DataFrame(data)

# Melt the data
df_melt = df.melt(var_name='Species', value_name='Richness')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Create violin plot
sns.violinplot(ax=ax, x="Species", y="Richness", data=df_melt)

# Set title and labels
ax.set_title('Species richness of marine organisms in a coral reef')
ax.set_xlabel('Species')
ax.set_ylabel('Richness')

# Modify the transparency of the violins that contain the center point of the bounding box to 0.34
violin = ax.collections[0]
violin.set_alpha(0.34)

# Show the plot

plt.tight_layout()
plt.savefig("figure.png")