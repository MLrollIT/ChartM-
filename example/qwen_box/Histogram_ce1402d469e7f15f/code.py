import matplotlib.pyplot as plt

# Depth Intervals
depth_intervals = ["0-100", "100-200", "200-300", "300-400", "400-500", 
                   "500-600", "600-700", "700-800", "800-900", "900-1000"]

# Frequency of Marine Life Occurances
marine_life_freq = [15, 28, 33, 41, 54, 62, 49, 37, 23, 9]

plt.figure(figsize=(10,7))
plt.bar(depth_intervals, marine_life_freq, color='blue')

# Add title and labels
plt.title('Distribution of Marine Life across Different Depth Zones in the Ocean')
plt.xlabel('Depth Intervals (meters)')
plt.ylabel('Frequency of Marine Life Occurrences')

# Modify the line width of the bars that contain the center point of the bounding box
for bar in plt.gca().get_children():
    if isinstance(bar, plt.Rectangle):
        if bar.get_bbox().get_width() == 440:
            bar.set_linewidth(1.03)
            bar.set_picker(True)

# Show the plot
plt.tight_layout()
plt.savefig("figure.png")