# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Seabed depth data for different locations
locations = ['A', 'B', 'C']
depths = [[1500, 1550, 1600, 1550, 1650, 1600, 1500, 1520, 1580, 1610],
          [1450, 1500, 1550, 1520, 1580, 1600, 1530, 1560, 1500, 1470],
          [1400, 1450, 1480, 1500, 1550, 1520, 1450, 1420, 1500, 1490]]

# Prepare data for seaborn
data = []
for location, depth in zip(locations, depths):
    data.extend([(location, value) for value in depth])

# Convert data to a DataFrame
import pandas as pd
df = pd.DataFrame(data, columns=['Location', 'Depth'])

# Create a violin plot
plt.figure(figsize=(10,6))
sns.violinplot(x="Location", y="Depth", data=df)

# Add title and labels
plt.title("Ocean Floor Seabed Topography Mapping")
plt.xlabel("Location")
plt.ylabel("Seabed Depth (in meters)")

# Set the clipping box for the violins that contain the center point of the bounding box
bbox = plt.Bbox([[245, 145], [245 + 409, 145 + 263]])
plt.violinplot(x="Location", y="Depth", data=df, clip_on=False, widths=0.8, showmeans=True, meanline=True, meanprops={"color":"black", "marker":"o", "markerfacecolor":"black", "markersize":8}, showextrema=False, showbox=False, showcaps=False, clip_on=False, clip_box=bbox)

# Add the bounding box to the plot
plt.gca().add_patch(plt.Rectangle((bbox.xmin, bbox.ymin), bbox.width, bbox.height, fill=False, edgecolor='black', linewidth=2))

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")