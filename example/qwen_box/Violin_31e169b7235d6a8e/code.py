import matplotlib.pyplot as plt
import seaborn as sns

# Provided data
galaxies = ['Galaxy A'] * 10 + ['Galaxy B'] * 10 + ['Galaxy C'] * 10

star_formation_regions = [5000, 4800, 5100, 5200, 4900, 4950, 5050, 5150, 5300, 4850, 
                          7500, 7200, 7800, 7600, 7700, 7400, 7850, 7950, 7700, 7550,
                          4000, 4200, 3800, 4300, 4100, 3900, 4050, 3950, 4150, 4250]

# Initialising a figure
plt.figure(figsize=(9, 6))

# Creating violin plot 
sns.violinplot(x=galaxies, y=star_formation_regions)

# Adding title, y-axis label and grid
plt.title('Spatial distribution of Star Formation Regions across Galaxies')
plt.ylabel('Radial Distance from Galactic Center (light-years)')
plt.grid(True)

# Set the linestyle of all the lines in the violins which contains the center point of the bounding box to '--'
for violin in plt.violinplot(galaxies, star_formation_regions, showmeans=True, showextrema=False)[2]:
    violin.set_linestyle('--')

# Hide the visibility of the violins' box part by setting it to False
for violin in plt.violinplot(galaxies, star_formation_regions, showmeans=True, showextrema=False)[2]:
    violin.set_visible(False)

# Code to display the created plot

plt.tight_layout()
plt.savefig("figure.png")