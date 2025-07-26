import matplotlib.pyplot as plt

# Data
elevation_ranges_meters = ['0-1000', '1000-2000', '2000-3000', '3000-4000', '4000-5000']
frequency = [25, 18, 12, 6, 3] 

# Create Histogram
plt.hist(elevation_ranges_meters, weights=frequency, bins=5, alpha=0.7, color='skyblue', edgecolor='black')

# Title and labels
plt.title('Planet Surface Elevation Mapping')
plt.xlabel('Elevation Ranges (in meters)')
plt.ylabel('Frequency of Elevation Data Points')

# Set picker state of the bars that contain the center point of the bounding box to True
for bar in plt.gca().patches:
    if bar.get_bbox().contains(plt.gcf().bbox.get_points()[1]):
        bar.set_picker(True)

# Show plot
plt.tight_layout()
plt.savefig("figure.png")