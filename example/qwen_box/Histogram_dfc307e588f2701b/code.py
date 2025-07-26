import matplotlib.pyplot as plt
import numpy as np

# Data points for the Ocean Floor Seabed Topography Mapping dataset
depth_intervals = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
measurement_frequencies = [2, 3, 5, 8, 10, 12, 15, 18, 20, 22, 24, 26, 28, 30, 32, 33, 31, 28, 25, 22, 18, 15, 12, 10, 8, 7, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8]

# preparing data for histogram
data = np.repeat(depth_intervals, measurement_frequencies)

#plotting
plt.figure(figsize=(10,5)) 
plt.hist(data, bins = np.arange(10,205,5), color ='lightblue', edgecolor ='gray')
plt.xlabel('Depth Intervals (meters)', fontsize = 12)
plt.ylabel('Frequency of Measurements', fontsize = 12)
plt.title('Ocean Floor Seabed Topography Mapping', fontsize = 14)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

# Add an outline to the bars that contain the center point of the bounding box
for i in range(2, 10):
    plt.axvline(x=i*5, ymin=0, ymax=1, color='black', linewidth=1.332, linestyle='--', alpha=0.5)
    plt.axvline(x=i*5, ymin=0, ymax=1, color='black', linewidth=1.332, linestyle='--', alpha=0.5)

plt.savefig("figure.png")