import matplotlib.pyplot as plt

# Settings for the dataset
depth_ranges = ["0-100", "100-500", "500-1000", "1000-2000", "2000-4000", "4000-6000", "6000-8000", "8000-10000"]
depth_measurements = [62, 48, 32, 20, 12, 6, 4, 2]

# Create the histogram
plt.hist(range(len(depth_ranges)), weights=depth_measurements, bins=len(depth_ranges), align='left', color='c', edgecolor='black')
  
# Set the title and labels
plt.xlabel('Depth Ranges in meters')
plt.ylabel('Frequency of Depth Measurements')
plt.xticks(range(len(depth_ranges)), depth_ranges)
plt.title('Distribution of Ocean Depths')

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")