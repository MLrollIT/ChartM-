import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a dictionary for dreamland's terrain elevation data
dreamland_terrains = {
    'Sunset Valley' : [300, 310, 320, 325, 315, 330, 335, 340, 310, 325],
    'Misty Mountains' : [600, 610, 590, 570, 630, 605, 615, 620, 585, 595],
    'Crystal Lake' : [150, 155, 160, 145, 165, 140, 150, 155, 135, 160],
    'Whispering Woods' : [400, 410, 405, 395, 415, 420, 390, 400, 415, 415]
}

# Preprocess the data for seaborn by transforming the above dictionary into two lists: one for terrain and one for elevations
terrain = []
elevation = []
for k, v in dreamland_terrains.items():
    terrain.extend([k]*len(v))
    elevation.extend(v)

# Create a DataFrame from the lists
df = pd.DataFrame({'Terrain': terrain, 'Elevation': elevation})

# Making the plot
plt.figure(figsize=(10,6))
sns.violinplot(x="Terrain", y="Elevation", data=df)
plt.title("Elevation Distribution in Dreamland Terrains")

# Set the visibility of the box part of violin that contains the center point of the bounding box to False
plt.violinplot(df['Elevation'], showmeans=False, showmedians=False, showextrema=False)

plt.tight_layout()
plt.savefig("figure.png")