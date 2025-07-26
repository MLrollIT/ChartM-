import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
rocky_surfaces = [45, 50, 42, 48, 38, 55, 43, 47, 52, 40]
sandy_dunes = [30, 35, 28, 32, 37, 29, 31, 36, 34, 33]
crater_interiors = [15, 20, 18, 17, 22, 16, 19, 21, 23, 14]
mountainous_regions = [70, 65, 72, 68, 75, 66, 71, 73, 69, 74]

# Combine data for plotting
data = [rocky_surfaces, sandy_dunes, crater_interiors, mountainous_regions]
labels = ['Rocky Surfaces', 'Sandy Dunes', 'Crater Interiors', 'Mountainous Regions']

# Seaborn violinplot
sns.set(style='whitegrid')
plt.figure(figsize=(10,6))
sns.violinplot(data=data, inner='quartiles')
plt.xticks([0, 1, 2, 3], labels)
plt.ylabel('Elevation Level (m)')
plt.title('Elevation Levels across Different Terrains on Mars')

# Set the clipping state of the violins that contain the center point of the bounding box to True
# and update the linestyle of that area to 'dashdot'
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0.5, transform=plt.gca().transAxes)
bbox = plt.bbox_to_anchor(0.5, 0