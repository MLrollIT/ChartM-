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

# Add a gold shadow effect to the bars that include the center point of the bounding box, with an offset of (2.12, 3.68)
bbox = plt.gca().get_position().bounds
bbox = [bbox[0] + 2.12, bbox[1] + 3.68, bbox[2], bbox[3]]
plt.gca().add_patch(plt.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], facecolor='gold', alpha=0.5))

# Show a annotation label for these bars using 'A new Label'
plt.annotate('A new Label', xy=(bbox[0], bbox[1]), xycoords='data', xytext=(bbox[0] + 2.12, bbox[1] + 3.68), textcoords='data', arrowprops=dict(facecolor='black', shrink=0.05), bbox=dict(boxstyle="square", fc="white", ec="black", alpha=0.5))

plt.tight_layout()
plt.savefig("Edit_figure.png")