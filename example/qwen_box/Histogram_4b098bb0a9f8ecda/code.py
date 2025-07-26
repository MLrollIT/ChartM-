import matplotlib.pyplot as plt

# Data points for Ocean Current Speeds Histogram
speed_intervals = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
frequency_of_currents = [2, 7, 12, 18, 23, 15, 10, 5, 3, 2]

fig, ax = plt.subplots()

# Create a bar chart
bar = ax.bar(speed_intervals, frequency_of_currents, color='lightseagreen')

# Set animated state of the bars that contain the center point of the bounding box to True
center_point = 25
for i, rect in enumerate(bar):
    if speed_intervals[i] == center_point:
        rect.set_animated(True)

# Set clipping state of those bars to True
for i, rect in enumerate(bar):
    if speed_intervals[i] == center_point:
        rect.set_clip_on(True)

# Add bounding box
bbox = dict(boxstyle="square", fc="white", ec="black", lw=2)
ax.text(center_point, 20, "Center Point", bbox=bbox)

# Add title and labels
ax.set_title("Ocean Current Speeds Distribution")
ax.set_xlabel('Speed Intervals (cm/s)')
ax.set_ylabel('Frequency of Currents')

# Save the figure
plt.savefig("Edit_figure.png")