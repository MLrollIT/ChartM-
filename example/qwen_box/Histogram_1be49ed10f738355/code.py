import matplotlib.pyplot as plt

# Data points for temperature ranges and frequencies
temperature_ranges = ['10-20', '20-30', '30-40', '40-50', '50-60']
frequencies = [15, 30, 45, 25, 10]

# Plotting the histogram
fig, ax = plt.subplots()

ax.bar(temperature_ranges, frequencies)

# Labeling the axes
ax.set_xlabel('Temperature Ranges (in degrees Celsius)')
ax.set_ylabel('Frequency')

# Setting the title
ax.set_title('Temperature and Species Distribution')

# Set the picker state of the bars that contain the center point of the bounding box to False
for bar in ax.patches:
    if bar.get_bbox().contains((20, 30)):
        bar.set_picker(True)
        bar.set_rasterized(True)

# Displaying the plot
plt.tight_layout()
plt.savefig("Edit_figure.png")