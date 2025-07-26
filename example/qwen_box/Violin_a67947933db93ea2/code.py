import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
north_atlantic_population = [200, 180, 190, 210, 220, 195, 205, 185, 192, 198]
south_pacific_population = [150, 160, 155, 170, 165, 145, 140, 148, 152, 158]
indian_ocean_population = [120, 110, 130, 118, 125, 135, 140, 128, 132, 138]
arctic_ocean_population = [80, 90, 85, 95, 100, 75, 78, 82, 88, 92]

# Data collection in list of lists
data = [north_atlantic_population, south_pacific_population, indian_ocean_population, arctic_ocean_population]

# Create a figure and axis 
fig, ax = plt.subplots()

# Creating labels
oceans = ['North Atlantic', 'South Pacific', 'Indian Ocean', 'Arctic Ocean']

# Creating violin plot
sns.violinplot(data=data, ax=ax)

# Set labels
ax.set_xticklabels(oceans)

# Setting the title
plt.title('Octopus Population Distribution in Oceans')

# Display the plot

plt.tight_layout()
plt.savefig("figure.png")

# Modify the color of the violins that contain the center point of the bounding box to #de60e9
for i in range(len(data)):
    for j in range(len(data[i])):
        if i == 1:
            ax.collections[i].set_facecolor('#de60e9')