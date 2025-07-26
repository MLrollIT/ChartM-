import matplotlib.pyplot as plt
import seaborn as sns

# Define Data

slope_25_35 = [0.8, 1.2, 1.0, 1.1, 0.9, 1.3, 1.0, 0.9, 1.2, 1.1, 1.0, 1.3]
slope_35_45 = [1.5, 1.8, 1.6, 1.7, 1.9, 1.5, 1.7, 1.6, 1.8, 1.9, 1.6, 1.5]
slope_45_55 = [2.2, 2.4, 2.0, 2.1, 2.3, 2.5, 2.2, 2.1, 2.4, 2.3, 2.0, 2.2]
slope_55_65 = [2.8, 3.0, 2.7, 2.9, 2.6, 3.1, 2.8, 2.7, 3.0, 2.9, 3.1, 2.8]

# Store the data and labels together
data = [slope_25_35, slope_35_45, slope_45_55, slope_55_65]
labels = ['25-35 deg', '35-45 deg', '45-55 deg', '55-65 deg']

# Create the violin plot
plt.figure(figsize=(10,6))
sns.violinplot(data=data, palette="Set3")

# Set title and labels
plt.title('Avalanche Dynamics in Mountainous Regions')
plt.xlabel('Slope Inclination (degrees)')
plt.ylabel('Snow Slab Depth (meters)')
plt.xticks(ticks=range(4), labels=labels)

# Add an outline around the violins that contain the center point of the bounding box
for i in range(len(data)):
    plt.plot([i, i], [0, 3.5], color='#388b28', linewidth=1.63)

# Show plot
plt.tight_layout()
plt.savefig("figure.png")