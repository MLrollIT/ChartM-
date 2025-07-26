import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
full_sunlight = [10, 15, 13, 14, 12, 16, 13, 15, 14, 16, 13, 15, 16, 14, 17, 15, 13, 16, 12, 14, 15, 13, 16, 17, 15, 13, 14, 16, 18, 20]
partial_shade = [7, 9, 8, 10, 9, 8, 11, 9, 10, 8, 7, 9, 11, 10, 7, 9, 8, 10, 9, 11, 8, 7, 9, 8, 10, 11, 9, 10, 8, 9]
full_shade = [5, 4, 6, 5, 7, 6, 5, 4, 7, 6, 5, 7, 6, 5, 4, 6, 7, 5, 6, 4, 7, 5, 6, 7, 5, 4, 6, 7, 5, 6]

# Creating DataFrame
data = pd.DataFrame({
    'Full Sunlight': full_sunlight,
    'Partial Shade': partial_shade,
    'Full Shade': full_shade
})

# Melting the DataFrame from wide format to long format
data_melted = data.melt(var_name='Light Condition', value_name='Plant Height (cm)')

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Light Condition', y='Plant Height (cm)', data=data_melted)
plt.title('Growth Pattern of Plant Species under Different Light Conditions')
plt.tight_layout()

# Get the bounding box of the violin plot
bbox = plt.gca().get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())

# Get the center point of the bounding box
center_point = bbox.center

# Get the violins that contain the center point of the bounding box
violins = plt.gca().violinplot.get_paths()
violins = [v for v in violins if v.contains_point(center_point)]

# Change the linestyle of the violins that contain the center point of the bounding box to 'dashed'
for v in violins:
    v.set_linestyle('dashed')

# Set the rasterized state of the violins related to the same points to False
for v in violins:
    v.set_rasterized(False)

plt.savefig("figure.png")