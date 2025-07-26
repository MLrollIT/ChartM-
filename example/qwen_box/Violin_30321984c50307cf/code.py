# Required Libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Elevation Data
mars_elevation = [1200, 1300, 1100, 1400, 1250, 1350]
venus_elevation = [900, 950, 870, 920, 880, 930]
titan_elevation = [1600, 1550, 1650, 1500, 1620, 1560]

# Creating DataFrame
data = pd.DataFrame({
    'Planet': ['Mars'] * len(mars_elevation) + ['Venus'] * len(venus_elevation) + ['Titan'] * len(titan_elevation),
    'Elevation': mars_elevation + venus_elevation + titan_elevation
})

# Plotting
plt.figure(figsize=(9, 6))
sns.violinplot(x='Planet', y='Elevation', data=data)
plt.title('Planet Surface Elevation Mapping')
plt.xlabel('Planet')
plt.ylabel('Elevation (in meters)')

# Change the fill pattern of the violin that contains the center point of the bounding box to an O hatch pattern and update its color to #e5ed86
violin = plt.gca().violinplot(data['Elevation'], positions=[5], showmeans=False, showmedians=False, showextrema=False)
violin['bodies'][0].set_facecolor('#e5ed86')
violin['bodies'][0].set_hatch('O')

plt.tight_layout()
plt.savefig("figure.png")