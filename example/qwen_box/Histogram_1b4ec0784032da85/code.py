import matplotlib.pyplot as plt
import numpy as np

# Set intervals, must be the same amount of elements
temperature_intervals = ["-2 to -1","-1 to 0","0 to 1", "1 to 2", "2 to 3", "3 to 4", "4 to 5", "5 to 6"]
intervals_freq = np.array([10, 15, 20, 30, 35, 25, 18, 12])

# Preparing data for histogram
temp_data = []
for i, interval in enumerate(temperature_intervals):
    lower, upper = map(float, interval.split(' to '))
    temp_data.extend(list(np.random.uniform(lower, upper, intervals_freq[i])))

# Create histogram
plt.hist(temp_data, bins=len(temperature_intervals), edgecolor='black')

# Set the labels and title
plt.xlabel("Temperature Intervals (in Celsius)")
plt.ylabel("Frequency of Temperature Intervals")
plt.title("Ocean Temperature Variability in the Arctic Ocean")

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")

# Modify the bars that contain the center point of the bounding box
bbox = plt.gca().get_position()
bbox = bbox.transformed(plt.gca().transAxes)
bbox = bbox.transformed(plt.gca().transData)
bbox = bbox.get_points()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] = 0.5
bbox = bbox.tolist()
bbox[0][0] = 0.5
bbox[0][1] = 0.5
bbox[1][0] = 0.5
bbox[1][1] =