import matplotlib.pyplot as plt

#Given data
elevation_ranges = ['1000-1100', '1100-1200', '1200-1300', '1300-1400', '1400-1500', '1500-1600', '1600-1700', '1700-1800']
frequency_samples = [12, 18, 25, 30, 28, 20, 15, 10]

# Creating the histogram
plt.figure(figsize=(10,6)) # To make sure the labels are readable
plt.bar(elevation_ranges, frequency_samples, color='green', alpha=0.7)

# Let's set up titles and labels
plt.title('Alien Planet Terrain Elevation Analysis')
plt.xlabel('Elevation Ranges (in meters)')
plt.ylabel('Frequency of Terrain Samples')

# Let's modify the labels of the bars that contain the center point of the bounding box
bbox = (1200, 1300, 1300, 1400)
plt.bar(elevation_ranges[bbox[0]:bbox[1]], frequency_samples[bbox[0]:bbox[1]], color='green', alpha=0.7, label='A new Label')
plt.bar(elevation_ranges[bbox[2]:bbox[3]], frequency_samples[bbox[2]:bbox[3]], color='green', alpha=0.7, label='A new Label')

# Let's update the line color for those same bars
bbox = (1200, 1300, 1300, 1400)
plt.bar(elevation_ranges[bbox[0]:bbox[1]], frequency_samples[bbox[0]:bbox[1]], color='green', alpha=0.7, label='A new Label', edgecolor='#464915')
plt.bar(elevation_ranges[bbox[2]:bbox[3]], frequency_samples[bbox[2]:bbox[3]], color='green', alpha=0.7, label='A new Label', edgecolor='#464915')

# Displaying the histogram
plt.tight_layout()
plt.savefig("figure.png")