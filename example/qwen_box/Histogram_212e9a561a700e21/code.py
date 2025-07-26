import matplotlib.pyplot as plt
import numpy as np

# Data points for Insect Swarm Movement Dynamics Study
interval_limits = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])  # Include both ends of the last interval
frequency_of_insects = [10, 15, 20, 25, 20, 15, 10, 5, 3, 2]

# Simulate raw data based on the frequency of each interval
raw_data = np.repeat((interval_limits[:-1] + interval_limits[1:])/2, frequency_of_insects)

# Generate histogram
plt.figure(figsize=(10, 6))
plt.hist(raw_data, bins=interval_limits, edgecolor='black', color='lightgreen')
plt.xlabel('Speed Intervals (cm/s)')
plt.ylabel('Frequency of Insects')
plt.title('Insect Swarm Movement Dynamics: Speed Distribution')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Get the bounding box of the center point of the bounding box
bbox = plt.gca().bbox_to_transform(np.array([[interval_limits[5], interval_limits[5]], [interval_limits[5], interval_limits[5]]]))

# Get the bar objects that contain the center point of the bounding box
bars = plt.gca().collections[0].get_paths()
for bar in bars:
    if bar.contains_point(bbox.transform(np.array([[interval_limits[5], interval_limits[5]], [interval_limits[5], interval_limits[5]]]))):
        bar.set_edgecolor('#da9be9')
        bar.set_facecolor('#0204f8')
        bar.set_linewidth(0.80)
        bar.set_edgecolor('#ff80bf')
        bar.set_dashes([4, 4])

plt.savefig("figure.png")