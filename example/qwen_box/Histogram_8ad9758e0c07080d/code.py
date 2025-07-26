import matplotlib.pyplot as plt

# Depth Intervals in meters
depth_intervals = ["0-1000", "1000-2000", "2000-3000", "3000-4000", "4000-5000", "5000-6000", "6000-7000"]

# Frequency of Depth Measurements
frequency = [32, 48, 56, 62, 50, 38, 24]

# Creating histogram plot
plt.figure(figsize=(10,7))
plt.bar(depth_intervals, frequency, color='blue', edgecolor='black')

# Adding labels and title
plt.title("Depth Distribution in the Pacific Ocean", fontsize=20)
plt.xlabel("Depth Intervals (in meters)", fontsize=16)
plt.ylabel("Frequency of Depth Measurements", fontsize=16)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("figure.png")

# Set the rasterized state of the bars that contain the center point of the bounding box to False
plt.bar(depth_intervals, frequency, color='blue', edgecolor='black', rasterized=False)