import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Frequency of exercising
exercise_freq = [2, 3, 4, 5, 3, 2, 1]

# Number of hours of sleep
sleep_hours = [6, 7, 8, 7, 6, 5, 4]

# Creating stack plot
plt.figure(figsize=(10, 6))
plt.stackplot(days, sleep_hours, exercise_freq, labels=['Sleep', 'Exercise'], colors=['skyblue', 'coral'])

plt.title("Exercise Frequency and Sleep Quality", fontsize=18)
plt.xlabel("Week Days", fontsize=14)
plt.ylabel("Hours or Frequency", fontsize=14)
plt.legend(loc='upper right')

plt.grid(True)
plt.tight_layout()

# Update the label of the area that contains the center point of the bounding box to 'A new Label', and make sure the rasterized state for this area is set to False.
bbox = plt.gca().get_position().get_points()
bbox[1] = [bbox[1][0], 0.5]
bbox[2] = [bbox[2][0], 0.5]
plt.gca().add_patch(plt.Rectangle((bbox[0][0], bbox[0][1]), bbox[1][0] - bbox[0][0], bbox[1][1] - bbox[0][1], fill=False, edgecolor='black', label='A new Label', rasterized=False))

plt.savefig("Edit_figure.png")